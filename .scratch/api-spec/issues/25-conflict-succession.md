# Conflict, succession and co-investors

Type: grilling
Status: open
Blocked by: 15  (Predicate semantics)
Map: [api-spec](../map.md)

## Question

When do two ownership claims conflict, when is a later claim a change of owner (succession), how are co-investors told apart from conflicts, and what happens with undated claims?

## Context

- ADR 0001:12: a hop is control unless a quote states <50% or "minority". ADR 0001:15: a new controlling-owner claim ends the prior hop. ADR 0002:10: conflict = different controlling owners over overlapping dates; co-investors are not conflicts. → Two co-investors with no stated stakes are both "control", hence a conflict, which ADR 0002 says they aren't.
- Most portfolio and roster claims have no date: rules for undated vs dated claims, event_date vs retrieved_at.
- **Several non-PE control chains** (family + conglomerate): conflict or precedence?
- **Conflicts on non-ownership predicates**: two filings with different `lends_to` principal or allocation % (ADR 0002 defines conflict only for controlling owners).
- **"sources disagree" — fact state or business category?** GLOSSARY:79–81 and CLAUDE.md:26 describe a fact state with links to each source; evidence_layer_plan.md:122 and ADR 0001:20 make it a business category; edge confidence has no disagree value. Storage options: conflicts table, edge status, or computed from claims at read time.
