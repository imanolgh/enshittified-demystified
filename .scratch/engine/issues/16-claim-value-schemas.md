# Claim value schemas and values over time

Type: grilling
Status: open
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
