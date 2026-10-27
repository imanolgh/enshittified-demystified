# BDC discovery and Schedule of Investments parsing

Type: grilling
Status: open
Blocked by: 08, 16  (Research: EDGAR access, BDC identification and SoI formats; Claim value schemas and values over time)
Map: [api-spec](../map.md)

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
