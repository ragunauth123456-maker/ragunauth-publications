const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const workflow = JSON.parse(fs.readFileSync(path.join(__dirname, 'n8n', 'evidence-review.workflow.json'), 'utf8'));
const byName = n => workflow.nodes.find(x => x.name === n);
assert.equal(workflow.active, false, 'Workflow must never auto-activate on import');
assert.equal(workflow.settings.timezone, 'America/Guyana');
assert.equal(workflow.nodes.length, 6);
const names = workflow.nodes.map(n => n.name);
assert.equal(new Set(names).size, names.length);
assert.equal(byName('Daily 07:30 Guyana').parameters.rule.interval[0].triggerAtHour, 7);
assert.equal(byName('Daily 07:30 Guyana').parameters.rule.interval[0].triggerAtMinute, 30);
assert(!workflow.nodes.some(n => /github|email|slack|wordpress/i.test(n.type)), 'No auto-publication node');
const define = new Function(byName('Define Source Queries').parameters.jsCode)();
assert.equal(define.length, 4);
for (const q of define) {
  const u = new URL(q.json.url);
  assert.equal(u.hostname, 'api.crossref.org');
  assert.equal(q.json.review_state, 'metadata_search_only');
}
const fixture = { DOI:'10.5555/example-2026',title:['Synthetic fixture on cooling and energy'],
  publisher:'Test Publisher', published:{'date-parts':[[2026,9,25]]},
  type:'journal-article', abstract:'<b>Illustrative</b> metadata only' };
const inputs = [{json:{message:{items:[fixture,{...fixture}, {DOI:'bad-doi',title:['Reject me']}]}}},
  ...Array.from({length:3},()=>({json:{message:{items:[]}}}))];
const normalize = new Function('$input', '$', byName('Normalize Research Leads').parameters.jsCode)(
  {all:()=>inputs}, name=>({all:()=>{ assert.equal(name,'Define Source Queries');return define; }})
);
assert.equal(normalize.length,1,'Duplicate and invalid DOI records must be removed');
assert.equal(normalize[0].json.doi,'10.5555/example-2026');
assert.equal(normalize[0].json.published,'2026-09-25');
assert.equal(normalize[0].json.review_status.startsWith('UNVERIFIED'),true);
assert(!normalize[0].json.abstract_excerpt.includes('<b>'));
const packet = new Function('$input', byName('Prepare Review Packet').parameters.jsCode)(
  {all:()=>normalize});
assert.equal(packet.length,1);
assert.equal(packet[0].json.approval_state,'awaiting_human_review');
assert.equal(packet[0].json.lead_count,1);
assert(packet[0].json.markdown.includes('https://doi.org/10.5555/example-2026'));
assert(packet[0].json.markdown.includes('\n## '),'Reviewer packet must contain real newlines');
console.log('PASS: n8n workflow wiring, trigger timezone, Crossref URLs, DOI filtering, source sanitization, review gate and reviewer packet.');