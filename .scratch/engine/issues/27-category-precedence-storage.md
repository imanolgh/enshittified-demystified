# Category precedence and storage

Type: grilling
Status: open
Blocked by: 14, 25  (Owner kind: storage, evidence and the fund–firm link; Conflict, succession and co-investors)
Map: [engine](../map.md)

## Question

What is the full precedence among business categories, which entity types get a category, and are categories (and separation degrees) stored or computed on read?

## Context

- Only two precedence rules exist: PE beats non-PE; minority PE beats non-PE (ADR 0001:11–12,20; ADR 0002:11). No order among non-PE categories, nor for sources_disagree / owner_type_not_confirmed vs a verified PE chain on another path.
- **Storage**: ADR 0001:13 implies a stored (business, PE firm) row with separation degree; columns undefined. Is the category itself stored (with checked_at and the deciding chain) or computed on read? Recompute bookkeeping after an owner-kind change (async fan-out above N businesses). Where does formerly-PE history live? (evidence_layer_plan.md:194; build_roadmap.md:61,73)
- **Which entity types get a category**: businesses only, or rollups and brands too (an A2 search for a DSO)?
- Several chains to the same PE firm → separation degree = minimum (default).
- **From "What a business entity is"** (2026-11-05, [ADR 0005](../../../docs/adr/0005-brands-companies-locations-separate.md)): the candidate types are now `brand`, `company` and `location` (no `business` or `rollup`). The franchise rule needs a brand verdict and an operator verdict, so more than one type may need a category.
- **From "Schema conventions"** (2026-11-05; conventions in evidence_layer_plan.md §4; no on-demand research per decisions.md §15): the "A2 search for a DSO" example now means a search for a seeded rollup company; searches never start research.
- **From "Predicate semantics"** (2026-11-05; role table in evidence_layer_plan.md §4 `claims`): a store has two verdicts: the brand verdict walks brand → owner; the store verdict walks location → `operated_by` → operator → owners. Hops are `owned_by` and `operated_by`; `lends_to`, `holds_position` and `allocates_to` never are. A brand's chain may skip the operating company, so separation degree can be one lower than reality.
