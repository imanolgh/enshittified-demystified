# NPPES census load and census match

Type: grilling
Status: open
Blocked by: 06, engine/12, engine/19, engine/30, 49  (Research: NPPES bulk file and API; What a business entity is; Entity resolution algorithm; Rosters, portfolio pages and the registry; Local business identity and resolution)
Map: [local-businesses](../map.md)

## Question

How is the NPPES census loaded and refreshed, and how does the census match join roster locations to census entities?

## Context

- **Load**: finding the file (name changes monthly), monthly full vs weekly incrementals, deactivations → entity status + events, upsert key, streaming with polars, which taxonomies/enumeration types (from "Research: NPPES bulk file and API" and "What a business entity is").
- **Census match algorithm** (build_roadmap.md:99–101; research_flows.md:16–17): matching roster brand names against NPPES legal names, address normalization, many-to-one cases; deterministic code or LLM; how often it re-runs (after each roster crawl?).
- Must the roster label become an alias of the census entity (else "doc mentions subject alias" fails)?
- What a match publishes (`operates_location_of` claim? via which producer — see "Claim producers…") and what an unmatched census entity shows ("no PE evidence found (checked {date})" vs not-yet-checked — see "What 'checked' means…").
- NPPES API: when called beyond census misses.
- **NPPES: entity, hint, or claim?** (moved here from engine "Claim producers and the claims door", 2026-11-04) build_roadmap.md:88 (census → entities + aliases); research_flows.md:34 ("a hint for retrieval, not a claim") vs :72 (NPPES other-name counted as a verifying source); connector-dev SKILL:18 (ETL → claims). Because NPPES self-verifies, an alias field alone would publish a verified link.
