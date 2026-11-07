---
name: bdc-parser
description: Build and maintain app/source_connectors/bdc_soi.py — the BDC Schedule of Investments parser. This is the ONE component fully delegated to Claude Code (build_roadmap.md Step 21). Use when parsing BDC 10-K/10-Q filings, Schedule of Investments tables, or fixing parse failures on a specific fund's filing format.
---

# BDC Schedule of Investments Parser (the delegated exception)

You own this module's implementation. The developer owns acceptance: they review your emitted claims against the actual filing PDFs, not your code. Optimize for reviewable correctness, not elegance.

## Requirements (fixed)
- Input: a BDC 10-K/10-Q already retrieved to storage (PDF or filing HTML) + its `documents` row.
- Parse the Schedule of Investments table(s) — pdfplumber for text/layout, camelot for table structure; handle multi-page tables, repeated headers, footnote markers, subtotal rows.
- Equity rows in the Schedule (common units, warrants, preferred) emit `holds_position` (BDC fund → company), never an ownership claim, so a warrant can't become a control hop (engine "Predicate semantics", 2026-11-05). Whether a "control investments" row also yields `owned_by` is engine "BDC discovery and Schedule of Investments parsing".
- Output per portfolio row: an `ExtractedClaim` with predicate `lends_to` (BDC fund → borrower), `value` carrying the `lends_to` fields from evidence_layer_plan.md §4 (engine "Claim value schemas", 2026-11-06): `instrument`, `reference_rate`, `spread_pct`, `interest_rate_pct`, `pik_rate_pct`, `floor_pct`, `principal`, `cost`, `fair_value`, `currency`, `scale`, `non_accrual`, `maturity_date`, `affiliation`; `event_date` is the Schedule's period end — and a `quote` reproducing the row's text verbatim from the parsed-table text stored on the document.
- **Numeric cross-check (hard requirement): the principal amount in the quote must equal the structured value, or the claim is not emitted.** Above a per-filing failure-rate threshold (a setting), emit no claims for that filing, mark it unparseable (a parse failure, never `no_evidence_found`), and log an operational alert (ADR 0002).
- Unparseable table/section → a parse failure with an operational alert, never `no_evidence_found` (engine "ExtractedClaim and the extraction result envelope", 2026-11-06). Only a Schedule that parsed cleanly can show no lending evidence for a borrower. Never guess a row. Never interpolate.
- Fund-level facts (total PIK %, non-accrual %) are NOT emitted: they moved to the retirement map with fund health (engine "Predicate semantics", 2026-11-05).
- Borrower names go out raw for `resolve_entity` — do not "clean" them beyond whitespace; suffixes like "LLC"/"Holdings" are resolution signals.

## Fixtures & acceptance loop
- Maintain ≥3 fixture filings from BDCs with visibly different table formats in `tests/fixtures/bdc_soi/`; add a new fixture for every new format that breaks in production (fixture first, then fix — per conformance-tests skill).
- Conformance test: fixture → expected row count ± tolerance, spot-assert 5 known rows per fixture (borrower, principal, rate), zero claims failing the numeric cross-check.
- For developer review, produce a side-by-side acceptance report per fixture: `page/row → emitted claim` for 20 sampled rows, so they can check against the PDF quickly. Iterate on their corrections; expect 2–3 rounds per new format.

## Boundaries
- This module still obeys every CLAUDE.md invariant: contract types only, claims door only, no DB writes of its own, no touching `app/core/`.
- Format chaos is expected; scope creep is not. If a fund's filing needs a fundamentally different strategy (e.g., XBRL structured data available), propose it with trade-offs — the developer decides.
