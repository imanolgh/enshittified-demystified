# Claim value schemas and values over time

Type: grilling
Status: resolved
Blocked by: 15, 05, 08  (Predicate semantics; Research: Form 5500 bulk data contents; Research: EDGAR access, BDC identification and SoI formats)
Map: [engine](../map.md)

## Question

What typed `value` schema does each predicate carry, and how are values that change over time (quarterly loan marks, annual allocations) represented given claims are append-only?

## Context

- `value` is "deliberately shapeless" (python-types-primer.md:74) but code needs fixed keys: `stake_pct`/`stake_type` for the minority rule (ADR 0001:12); principal, rate/spread, PIK, fair value, non-accrual, currency, "in thousands" scale, period end for BDC claims and the numeric cross-check (bdc-parser SKILL:13; evidence_layer_plan.md:186); allocation %/$ and as-of date for `allocates_to`.
- **Values over time**: each 10-Q yields a new claim for the same loan; research_flows.md:162 says "non-accrual/PIK deltas (claim updates…)" — contradicts append-only (CLAUDE.md:25). Which claim's value does the edge display?
- **BDC / interval-fund entity typing**: a BDC is a public company that is also a fund; research_flows.md:129,148 use `type=fund(PC)` and "interval-fund/BDC flags" that don't exist (evidence_layer_plan.md:87).
- Facts from the Form 5500 and EDGAR research tickets.
- **From "Predicate semantics"** (2026-11-05; role table in evidence_layer_plan.md §4 `claims`): values per predicate: `owned_by`/`acquired_by` (stake in `value`; `acquired_by`'s date is the start, `owned_by`'s confirms the hop as of its document's date, so what `owned_by`'s `event_date` holds is this ticket's), `operated_by` (none expected), `lends_to` (loan terms), `holds_position` (BDC equity rows: instrument, cost, fair value), `allocates_to` (parked with the retirement map). BDC fund-level totals moved to the retirement map.
- **From "Entity lifecycle"** (2026-11-06; notes in evidence_layer_plan.md §4 `entities`): `renamed_from` carries `value.former_name` (the old name as quoted) and no object; its schema joins this ticket's list.
- **From "ExtractedClaim and the extraction result envelope"** (2026-11-06): `ExtractedClaim.value` is validated against the predicate's schema defined here; a value that fails drops that item (logged). Dates are `event_date` (first day of the period) plus `event_date_precision` (`year|month|day`), so a year-only date stays a year.

## Comments

### Round 1 (2026-11-06)

Boundaries: how a stake changes the control rule is "Category precedence and storage"; conflicts and succession are "Conflict, succession and co-investors"; when a loan's edge ends is "Edge lifecycle"; how numbers in quotes are parsed and checked is "Citation verification rules".

- **Ownership value** (Q1): `owned_by` and `acquired_by` carry optional `stake_pct` (0–100), `stake_type` (`majority|minority`, only when the document uses the word) and `stake_basis` (`voting|economic`; Jersey Mike's: Blackstone "~76.5% voting"). How the basis feeds ADR 0001's "under 50%" rule: "Category precedence and storage".
- **Deal status** (Q2, option a): `acquired_by` gains `deal_status` (`announced|completed`); `event_date` is the announcement or closing date to match. Only `completed` backs an ownership hop; an announced deal is a pending deal (fit for the deal feed). A later `completed` claim for the same pair takes over; a called-off deal is "Conflict, succession…"'s; display is "Card wording…" and "Events and the public changelog".
- **`owned_by` date** (Q3): the "as of" date the quote states is `event_date`; otherwise null, and the hop counts as confirmed on the document's date (publication vs retrieval: "Document storage, fetch log and last-confirmed").
- **BDC rows** (Q4): `lends_to` value: `instrument` (as written), `reference_rate`, `spread_pct`, `interest_rate_pct`, `pik_rate_pct`, `floor_pct`, `principal`, `cost`, `fair_value`, `currency`, `scale`, `non_accrual`, `maturity_date`, `affiliation` (`non_affiliate|affiliate|control`, from the Issuer Affiliation axis or the section heading; 1940 Act: affiliate 5–25% voting, control over 25%). `holds_position` value: `instrument`, `units`, `cost`, `fair_value`, `currency`, `scale`, `affiliation`. `event_date` = the Schedule's period end (day precision). Amounts in full units with `currency`, plus `scale` (1, 1,000, 1,000,000) from the table's "(in thousands)" header for the numeric cross-check. Rates are percent numbers (5.25 = 5.25%). All optional except `currency` when an amount is present.
- **Values over time** (Q5): claims are never updated; each filing is a new claim. The edge shows the newest accepted claim's value by as-of date (`event_date`, else the document's date); older claims are history. Same as-of date → the later-filed document wins (a 10-Q/A). Same-date disagreements: "Conflict, succession…"; a loan missing from the next Schedule: "Edge lifecycle"; non-accrual flips as alert events: "Events and the public changelog". research_flows' "claim updates" corrected.
- **BDC typing** (Q6): a BDC is a `fund`; "is a BDC" is computed from an `sec_file_number` starting `814-`, no flag. Interval funds parked with the retirement map. A BDC's owner kind: "Owner kind".
- **Others** (Q7): `renamed_from` `{former_name}` required; `operated_by` none; `allocates_to` defined when the retirement map unparks.

## Answer

Resolved 2026-11-06 in a grilling session (one round, recorded under Comments).

- One Pydantic model per predicate (`extra="forbid"`) that `ExtractedClaim` and code producers validate against:
  - `owned_by`/`acquired_by`: `stake_pct`, `stake_type`, `stake_basis`; `acquired_by` adds `deal_status` (`announced|completed`), and only `completed` backs a hop.
  - `lends_to`: loan terms, amounts (full units + `currency` + `scale`), `non_accrual`, `maturity_date`, `affiliation`.
  - `holds_position`: `instrument`, `units`, `cost`, `fair_value`, `currency`, `scale`, `affiliation`.
  - `renamed_from`: `former_name`.
  - `operated_by`: none.
  - `allocates_to`: deferred to the retirement map.
- **Dates:** `owned_by`'s `event_date` is the stated as-of date, else the document's date confirms it; BDC rows use the period end.
- **Values over time** are new claims, never edits. The edge shows the newest accepted claim by as-of date, and the later-filed document wins a tie.
- **A BDC** is a `fund` recognized by its `814-` file number.
- No new ADR, no glossary change.

Handed on:
- "Citation verification rules": number checks, the `stake_type` word.
- "Conflict, succession and co-investors": deal status, called-off deals, same-date disagreements, stake changes.
- "Edge lifecycle": the newest claim gives the value, loan exits.
- "Category precedence and storage": `stake_basis`, completed deals only.
- "Events and the public changelog": non-accrual flips, pending deals in the feed.
- "BDC discovery and Schedule of Investments parsing": field mapping.
- "Document storage, fetch log and last-confirmed": the document date.
- "Owner kind": a BDC's owner kind.
- chains "Card wording and the how-this-works page": pending deals.
- retirement "Form 5500 ingestion and the headline exposure number": `allocates_to`.
