---
name: bdc-parser
description: Build and maintain app/source_connectors/bdc_soi.py, the BDC Schedule of Investments parser (the `parser` producer). Use when parsing BDC 10-K/10-Q filings, Schedule of Investments rows, joint-venture schedules, or fixing a parse failure on a specific BDC's filing layout.
---

# BDC Schedule of Investments parser

The design is settled in engine "BDC discovery and Schedule of Investments parsing" (`.scratch/engine/issues/36-bdc-discovery-and-soi.md`, 2026-11-16) and summarized in `docs/evidence_layer_plan.md` §5 "BDC connector and Schedule parser". Facts about real filings: `.scratch/engine/research/bdc-filing-facts.md` and `edgar-bdc.md`. Anything those don't answer goes to the developer.

## Input
- A BDC 10-K or 10-Q (or an amendment that carries a tagged Schedule) already stored as a parent document: the primary Inline XBRL `.htm`. Never PDFs, never the SEC BDC data set (`soi.tsv`) as a source.
- Only filings since the BDC began Inline XBRL tagging (August 2022 to May 2023 by BDC). Untagged filings are not read.

## Rows
- One table row that carries a holding's tags (`ix:nonFraction` facts in a context with `InvestmentIdentifierAxis`) is one holding.
- Values come from that row's tags, with their `scale` (3 → `scale` 1000, 6 → 1000000) and stored in full units with `currency`. Field mapping: `lends_to` and `holds_position` value models in evidence_layer_plan.md §4 `claims`.
- The hidden identifier string only groups a row's tags and keys the row's child document within the filing. Never quote it and never use it as a name: it sometimes names a different company than the visible row.
- Each row becomes a child document. Its `raw_text` is the row's visible cells in order, with the name and description cells copied down from the borrower's first row where the filer left them blank (Ares Capital style, also across page breaks). The claim quotes the whole `raw_text`.

## Claims
- Loan rows → `lends_to` (lender → borrower). Equity rows (common, preferred, units, warrants) → `holds_position`. An equity row under "Control investments" also gives `owned_by` (company → BDC) with `stake_basis: voting` and no `stake_pct`.
- `event_date` = the Schedule's period end. `affiliation` comes from section headings or footnote markers (filers never tag it per holding).
- Name as written: the name cell after the copy-down, minus footnote markers ("(13)", "(4)(10)") and tranche words the filer appends ("- Funded Revolver"). Keep spelling, punctuation and entity suffixes: they are resolution signals.
- Two names joined by "and" or "&", each ending in an entity suffix (Inc., LLC, L.P., Corp., Ltd.), give one claim per company with the same quote.
- A trailing parenthesis comes off the name (one inside a name, "Activate Holdings (US) Corp.", stays). f/k/a or fka → also a `renamed_from` claim with `former_name`. dba, aka or a bare parenthesis → `value.other_name` as written ("dba Dental365"), never an ownership claim.
- The lender is the BDC (a `fund`). A joint-venture schedule tagged inside the 10-Q is read with the venture as the lender: emit a `fund` identity record for the venture, named as written (schedule heading or identifier ending, e.g. "Emerald JV LP"). The BDC's own row for its stake gives `holds_position` (BDC → venture). Untagged EX-99 venture schedules are not read.
- No fund-level totals (PIK %, non-accrual %). No LLM anywhere in this module.

## Outcomes per Schedule
Report one outcome for the BDC's own Schedule and for each venture schedule:
- A row fails when its shown numbers differ from its tags after scaling, it has no name after the copy-down, or the door rejects its claim.
- **clean**: no failed rows and the rows' fair values add up to the tagged total within the filer's rounding. Claims publish; pairs missing from it end their edges.
- **partial**: failed rows at or below the threshold setting, or totals off. Claims publish; no edge ends from it; operational alert.
- **failed**: above the threshold. Nothing publishes; the read is `unreadable` (never `no_evidence_found`); operational alert asking for a parser fix.

## Layouts
- Generic rules first: a blank name cell copies down; a trailing "(n)" is a footnote marker; a heading or footnote matching the fixed phrase list sets affiliation; the parser knows where the BDC's own Schedule ends and venture schedules begin.
- Per-filer overrides only where the generic rules fail, each in code with a real fixture from that filer added first (CLAUDE.md: fixture first, then the fix).

## Fixtures and the cross-check
- Fixtures in `tests/fixtures/bdc_soi/`: at least Ares Capital (blank name cells), PennantPark Floating Rate (tranche words in the name cell, venture rows marked only by their text), Blackstone Private Credit Fund (venture schedules, heading-based affiliation), one more venture schedule, and one 10-K Item 1 for the adviser read.
- Cross-check (CLAUDE.md definition of done): for each fixture filing, the parser's holdings match the SEC BDC data set's rows for that filing on holding count and fair value per holding, matched by identifier. The match bar lives in engine "Testing and acceptance". No hand-checked rows.

## Boundaries
- Every CLAUDE.md invariant holds: contract types only, the claims door only, no DB writes of its own, nothing in `app/core/`.
- Discovery (the `etl` producer), the daily filing check and the adviser read (the `llm` producer on Item 1) live outside this module.
