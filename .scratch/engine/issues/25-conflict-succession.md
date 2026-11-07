# Conflict, succession and co-investors

Type: grilling
Status: open
Blocked by: 15  (Predicate semantics)
Map: [engine](../map.md)

## Question

When do two ownership claims conflict, when is a later claim a change of owner (succession), how are co-investors told apart from conflicts, and what happens with undated claims?

## Context

- ADR 0001:12: a hop is control unless a quote states <50% or "minority". ADR 0001:15: a new controlling-owner claim ends the prior hop. ADR 0002:10: conflict = different controlling owners over overlapping dates; co-investors are not conflicts. → Two co-investors with no stated stakes are both "control", hence a conflict, which ADR 0002 says they aren't.
- Most portfolio and roster claims have no date: rules for undated vs dated claims, event_date vs retrieved_at.
- **Several non-PE control chains** (family + conglomerate): conflict or precedence?
- **Conflicts on non-ownership predicates**: two filings with different `lends_to` principal or allocation % (ADR 0002 defines conflict only for controlling owners).
- **"sources disagree" — fact state or business category?** GLOSSARY:79–81 and CLAUDE.md:26 describe a fact state with links to each source; evidence_layer_plan.md:122 and ADR 0001:20 make it a business category; edge confidence has no disagree value. Storage options: conflicts table, edge status, or computed from claims at read time.
- **From "Predicate semantics"** (2026-11-05; role table in evidence_layer_plan.md §4 `claims`): `acquired_by` and `owned_by` claims for the same pair are one ownership hop, published as `owned_by`; `acquired_by` gives the start date. `operated_by` is a separate hop kind, so a new operator of a location (a franchise resale) is succession on `operated_by`.
- **From "ExtractedClaim and the extraction result envelope"** (2026-11-06): claims carry `event_date_precision` (`year|month|day`); a year-only date is the first day of that year with precision `year`. How precision affects "overlapping dates" and which claim is later is this ticket's.
- **From "Claim value schemas"** (2026-11-06; schemas in evidence_layer_plan.md §4 `claims`): `acquired_by` carries `deal_status` (`announced|completed`); only `completed` backs a hop, and a later `completed` claim for the same pair takes over from an announcement. A deal called off after announcement, two sources with the same as-of date that disagree, and stakes that change over time are this ticket's.
- **From "Funds and their investment firm"** (2026-11-07; ADR 0001 amended; notes in evidence_layer_plan.md §4): hops to a fund and to the firm that manages it, or to two funds of one firm, count as one owner: they never end each other as a succession and never count as sources disagreeing, and a sale to the same firm's continuation fund changes no category. A fund has one manager at a time: a newer `managed_by` claim naming a different firm ends the older edge (events row) by the values-over-time as-of-date rule. The mechanics of both are this ticket's.
