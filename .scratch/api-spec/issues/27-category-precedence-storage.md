# Category precedence and storage

Type: grilling
Status: open
Blocked by: 14, 25  (Owner kind: storage, evidence and the fund–firm link; Conflict, succession and co-investors)
Map: [api-spec](../map.md)

## Question

What is the full precedence among business categories, which entity types get a category, and are categories (and separation degrees) stored or computed on read?

## Context

- Only two precedence rules exist: PE beats non-PE; minority PE beats non-PE (ADR 0001:11–12,20; ADR 0002:11). No order among non-PE categories, nor for sources_disagree / owner_type_not_confirmed vs a verified PE chain on another path.
- **Storage**: ADR 0001:13 implies a stored (business, PE firm) row with separation degree; columns undefined. Is the category itself stored (with checked_at and the deciding chain) or computed on read? Recompute bookkeeping after an owner-kind change (async fan-out above N businesses). Where does formerly-PE history live? (evidence_layer_plan.md:194; build_roadmap.md:61,73)
- **Which entity types get a category**: businesses only, or rollups and brands too (an A2 search for a DSO)?
- Several chains to the same PE firm → separation degree = minimum (default).
