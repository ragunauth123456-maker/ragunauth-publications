# Physical Limits of AI: Research Verification Toolkit

Companion to Ragunauth Ramsaroop's September 2026 white paper, *The Physical Limits of Artificial Intelligence*. This directory supplies an importable n8n evidence-review workflow, transparent scenario arithmetic, and automated integrity checks. It is not a simulation of grid constraints, a new forecast, or a claim that superintelligence exists.

## Files
- `n8n/evidence-review.workflow.json`: a six-node, no-credentials workflow. It queries Crossref for new scholarly metadata across electricity/grid demand, water/cooling, critical minerals, and advanced AI/superintelligence.
- `test-workflow.cjs`: offline fixture tests for node wiring, deduplication, DOI validation, review flags, markdown output, and zero automatic publication.
- `verify_scenarios.py`: independent arithmetic checks corresponding to Appendix A in the paper.

## Editorial protection
Crossref search results are unverified metadata leads. Read original studies and relevant institutional releases before writing new assertions. Record full source title, publication date, date of underlying measurements, study population, limitations, access date and editorial decision. Do not equate data-centre demand with AI-only demand. Treat AGI and ASI as conditional scenarios, without assigned arrival dates or invented power consumption.

This workflow does not access private documents, send messages, write GitHub files, change the website, or update the PDF. The output is a review packet inside an n8n execution. Its scheduled trigger is configured for 07:30 America/Guyana but stays inactive until a human explicitly enables the imported workflow. No API keys or secret tokens are stored.

## Local validation
1. Execute `node test-workflow.cjs` from this directory.
2. Execute `python verify_scenarios.py`. Confirm its numerical outputs against the white paper.
3. In an n8n 2.x instance, import `n8n/evidence-review.workflow.json`. Run the manual trigger. Inspect the Review Packet node's markdown output.
4. Validate network access to `api.crossref.org`. API queries use the official Crossref Works endpoint and public bibliographic metadata.
5. After verifying outcomes, use the instance UI to enable the daily trigger. Record who reviews each proposed source and which claim it informs.

## Evidence baseline and links
- IEA, *Key Questions on Energy and AI* (16 April 2026): https://www.iea.org/reports/key-questions-on-energy-and-ai
- IEA, *Global Critical Minerals Outlook 2026*: https://www.iea.org/reports/global-critical-minerals-outlook-2026
- International AI Safety Report 2026: https://internationalaisafetyreport.org/
- Crossref REST API reference: https://api.crossref.org/
- n8n source repository: https://github.com/n8n-io/n8n
- n8n documentation: https://docs.n8n.io/
- Energy-system-model reference, **not executed**: https://github.com/PyPSA/pypsa-eur

n8n is a source-available, self-hostable product under the Sustainable Use License, not OSI open source. This research workflow is a separate original artifact and does not incorporate n8n source code.

## Research and release status
Created 25 September 2026. The workflow's automated tests test logic and structure, not external scientific truth. No AI or ASI arrival probability is estimated. External publication stays under human editorial control.
