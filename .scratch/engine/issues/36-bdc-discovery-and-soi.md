# BDC discovery and Schedule of Investments parsing

Type: grilling
Status: open
Blocked by: 08, 16  (Research: EDGAR access, BDC identification and SoI formats; Claim value schemas and values over time)
Map: [engine](../map.md)

## Question

How is the BDC universe discovered, which filings are loaded, how are Schedules of Investments turned into `lends_to` claims, and who is the lender?

## Context

- Ruled 2026-10-26: the `bdc_soi` parser is the only source of SoI `lends_to` claims, no LLM fallback; failing rows rejected; above a per-filing failure-rate threshold the filing is withheld + operational alert (ADR 0002). Threshold and row tolerance unvalued.
- **Input format**: build_roadmap.md:11,117 ("PDF parser", "open each filing PDF") vs bdc-parser SKILL:11 ("PDF or filing HTML"); EDGAR filings are mostly HTML; inline XBRL may replace table parsing (bdc-parser SKILL:26) — from "Research: EDGAR access…".
- **Who lends to whom**: build_roadmap.md:119 and pre-launch-seeding.md:117 show "…sponsor ← lends_to ← BDC"; research_flows.md:134 and decisions.md:20 have the BDC lending to the portfolio company (the DSO). Lender entity = the BDC or its adviser?
- Several tranches per borrower: claim per row vs edge per borrower.
- Include non-traded/private BDCs? 10-Q handling, amendments; "in thousands" scaling inside the cross-check.
- **History at launch**: diffs need the prior quarter (research_flows.md:162) — latest filing only, or one prior too?
- Fund-level totals (PIK %, non-accrual %) need a non-relation fact form ("Predicate semantics").
- `parse_soi` (research_flows.md:131) vs `bdc_soi` naming.
- **From "Claim producers and the claims door"** (2026-11-05; summary in evidence_layer_plan.md "Producers and the door"): the BDC parser is the `parser` producer. A claim quotes the row's parsed-table text; if the parser reads DERA `soi.tsv`, each holding is a bulk row and quotes its whole data line. Per-record failures raise alerts; the per-filing withhold rule stays with this ticket and "Citation verification rules".
- **From "Predicate semantics"** (2026-11-05; role table in evidence_layer_plan.md §4 `claims`): equity rows in a Schedule (common units, warrants, preferred) emit `holds_position` (fund → company), never an ownership hop. Open here: whether a row in the Schedule's "control investments" section should also yield `owned_by`. Fund-level totals (PIK %, non-accrual %) are no longer emitted; they moved to the retirement map.
- **From "ExtractedClaim and the extraction result envelope"** (2026-11-06): an unparseable Schedule section or filing is a parse failure with an alert, never `no_evidence_found` (ADR 0002 and the bdc-parser skill corrected). A Schedule that parses cleanly with no row for a borrower counts as read: no lending evidence in that filing.
- **From "Claim value schemas"** (2026-11-06; schemas in evidence_layer_plan.md §4 `claims`): `lends_to` and `holds_position` value fields follow the SEC tags: `instrument`, `reference_rate`, `spread_pct`, `interest_rate_pct`, `pik_rate_pct`, `floor_pct`, `principal`, `cost`, `fair_value`, `currency`, `scale`, `non_accrual`, `maturity_date`, `affiliation` (from the Issuer Affiliation axis or the section heading). Mapping them from `soi.tsv`, XBRL and HTML tables is this ticket's. A BDC is a `fund` recognized by its `814-` file number.
