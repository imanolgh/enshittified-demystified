# Entity resolution algorithm

Type: grilling
Status: open
Blocked by: 12, 06, 09  (What a business entity is; Research: NPPES bulk file and API; Research: Google Places terms, pricing and a free geocoder)
Map: [api-spec](../map.md)

## Question

What is the resolution algorithm end to end: lookup order, when Google Places is called and what may be stored from it, normalization, scoring and thresholds, tiebreakers, and the fuzzy-search engine?

## Context

- **Lookup order differs in every doc**: evidence_layer_plan.md:149–150 (Places → census → NPPES API, Places on every row); research_flows.md:30–31 (Places → NPPES API, no census; 2,000 rows × ~$0.017); build_roadmap.md:101 (census → Places → NPPES API, misses only); stack_fastapi.md:39 (Places → NPPES → SoS/OpenCorporates). CLAUDE.md:31 / decisions.md:86: Places lazy only, never bulk.
- **What may be stored from Places**: ADR 0003:12 says place_id only, yet evidence_layer_plan.md:53,149 and research_flows.md:30,34 write canonical name and address; ADR 0002:14 tiebreaks on phone.
- **Places budget**: daily $ cap and behavior when hit.
- **Thresholds/bands** (link / ambiguous / create) are settings with no values (evidence_layer_plan.md:153; build_roadmap.md:75; research_flows.md:33 uses 0.94 → link). Is a single below-threshold candidate a create or an ambiguous?
- **Normalization** (suffixes LLC/PLLC/DDS/DMD, Dental↔Dentistry, &↔and, Unicode folding), **scorer** (which rapidfuzz scorer, field weights, blocking keys at census scale), **tiebreaker order** (address standardizer, phone normalization).
- **Fuzzy engine**: Meilisearch (evidence_layer_plan.md:39,152; stack_fastapi.md:26,39) vs pg_trgm + rapidfuzz (build_roadmap.md:75,167). Not in compose or pyproject. Phase 5's Meilisearch item was ruled into this ticket.
- **Can a user disambiguate in A2?** B2 lets a user pick a plan (research_flows.md:146); for businesses ADR 0002:14 says "couldn't confirm".
- **Ambiguous retry trigger**: after each NPPES/SoS/board refresh (ADR 0002:14) — confirm.
- Jev role 4 (entity-match confidence) is out of scope (Jev ruled out 2026-10-26).
