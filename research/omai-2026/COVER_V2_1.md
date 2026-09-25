# Omai 2026 white-paper cover fix, edition 2.1

The edition 2.0 cover contained a wide gold-tinted vertical overlay across the
subtitle, publication description, and third metric card.

Cause: the PDF renderer did not honor the CSS polygon clip-path on the
cover's :before pseudo-element. It rendered the pseudo-element background
as a rectangular panel instead.

Fix: remove the wide :before overlay rule in render_whitepaper.py.
Retain the base navy-to-teal background, gold top-left rail, gold title
accent, and high-contrast body text. Edition 2.1 updates the footer label.

The rebuilt PDF contains 36 tagged A4 pages. All 30 mechanical audits pass.
Pages 2-36 have identical extracted text apart from the edition label.
The audited PDF and its complete amended source package are available
in the ChatGPT conversation, not uploaded to this public repository.

Edition 2.1 PDF SHA-256:
aca1497ab9e387902f22a886ffcdababc37a4602c62a2a6a495c5eefc22cef2c

This is a presentation-only correction. The technical findings are unchanged.
