# Omai Gold 2026 PEA: white-paper audit

Audit date: 24 September 2026. Prepared for Ragunauth Ramsaroop.
Scope: independent desk review of the Omai Gold Mines Corp. release dated
19 August 2026, based on its 31 July 2026 preliminary economic assessment.

## What was repaired in the revised paper

1. Source citations now point to actual bibliography anchors. The audited
   36-page PDF has 131 internal in-text bibliography links, 140 contents
   link rectangles, and 28 external link annotations.
2. The report adds a second royalty cross-check and site-cost-per-ounce
   reconciliation without altering the issuer's published figures.
3. The published 3,900-dollars-per-ounce price case prints "9.411"
   under an FCF column denominated in US-dollar millions. Its interpretation
   as 9,411 million is explicit and remains subject to model confirmation.
4. Tables, appendix placement, headings and final-page flow were repaired.
5. Figure creation and PDF publishing use script-relative paths rather
   than environment-specific /mnt/data paths.

## Reproducible arithmetic

Run `python research/omai-2026/audit_metrics.py` from the repository root.
The test uses only the public source's disclosed totals and Table 2.
The corresponding full source bundle delivered in the conversation includes
the edited manuscript, six figures, PDF build script and 29-check QA script.

## Unresolved issuer-data reconciliation

The August PEA reports US$1,456 million in life-of-mine royalties.
US$266/oz times 6,326,775 payable ounces implies US$1,683 million.
US$10.74/t times 156.67 million ore tonnes implies US$1,683 million.
The approximate US$227 million gap requires the full underlying cost model.
No independent finding of accounting error is made.

The same release's site, cash-cost and AISC aggregate totals do not fully
reproduce the quoted unit measures with one common life-of-mine denominator.
The complete technical report and annual financial model remain prerequisites
for a definitive reconciliation.

## Reproducibility and provenance

Source: https://omaigoldmines.com/omai-project/preliminary-economic-assessment/
The source CSV transcribes Table 2. The 3,900 FCF entry is annotated above.
Audited PDF SHA-256:
ab8a3752a7f4828dbdba59c9866daa1132112d488ca2558644dd1e3804510d65

This folder does not contain the complete edited PDF or represent third-party
engineering certification. The finished PDF and complete source archive were
delivered separately to the requester. Do not treat this project's PEA
resources as established mineral reserves.
