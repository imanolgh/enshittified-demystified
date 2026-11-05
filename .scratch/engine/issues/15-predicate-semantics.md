# Predicate semantics

Type: grilling
Status: open
Blocked by: 12  (What a business entity is)
Map: [engine](../map.md)

## Question

For each predicate: what are its subject/object roles and direction, which predicates are ownership hops for the chain walk, do different ownership predicates corroborate each other, and how are franchises, employer→plan links and non-relation facts expressed?

## Context

- **Direction**: `operates_location_of(BrightSmiles → SmilePartners)` reads backwards (research_flows.md:56–57,72). Default: a role table in contracts; edge.from = claim.subject.
- **Corroboration across predicates**: Stage 5 groups by exact (subject, predicate, object) (evidence_layer_plan.md:190), so a press `acquired_by` and a portfolio `owned_by` for the same pair never corroborate — yet research_flows.md:71–72 treats them as verifying each other.
- **Franchises**: decisions.md:38 and pre-launch-seeding.md:54 require separate brand and operator verdicts; ADR 0001:13 counts `operates_location_of` as an ownership hop, so franchise links via it would make franchisee locations PE-owned. No predicate links location → brand. A2 accepts restaurants, so this can't wait for the national-brands launch (which is post-MVP: pre-launch-seeding.md:63 vs monetizationideas.md:34). ADR 0004 (2026-11-04) has since made chains and brands the launch product, so franchises are first-order; the product side is in chains-and-brands "Brand and chain model".
- **Licensing** (added 2026-11-04): a brand licensed to an operator (common in clothing: one company owns the brand, another makes or sells under it) can't be expressed with the closed predicate set. Is it a new predicate, a value on an existing one, or out of scope? The product side is in chains-and-brands "Brand and chain model".
- **Facts that aren't relations**: BDC fund-level totals (PIK %, non-accrual %; bdc-parser SKILL:16; research_flows.md:132); owner-kind evidence (see "Owner kind…"). CAFR asset-class allocations are out of scope.
- **Employer ↔ plan**: moved out 2026-11-04 (adr 0004 split) to retirement "Form 5500 ingestion and the headline exposure number" (deferred).
- **`holds_position`**: semantics never spelled out.
- Adding a predicate is a schema decision (CLAUDE.md:30) — this ticket is where it's made if needed.
