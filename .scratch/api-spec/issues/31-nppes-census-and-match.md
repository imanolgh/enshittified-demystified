# NPPES census load and census match

Type: grilling
Status: open
Blocked by: 06, 12, 19, 30  (Research: NPPES bulk file and API; What a business entity is; Entity resolution algorithm; Rosters, portfolio pages and the registry)
Map: [api-spec](../map.md)

## Question

How is the NPPES census loaded and refreshed, and how does the census match join roster locations to census entities?

## Context

- **Load**: finding the file (name changes monthly), monthly full vs weekly incrementals, deactivations → entity status + events, upsert key, streaming with polars, which taxonomies/enumeration types (from "Research: NPPES bulk file and API" and "What a business entity is").
- **Census match algorithm** (build_roadmap.md:99–101; research_flows.md:16–17): matching roster brand names against NPPES legal names, address normalization, many-to-one cases; deterministic code or LLM; how often it re-runs (after each roster crawl?).
- Must the roster label become an alias of the census entity (else "doc mentions subject alias" fails)?
- What a match publishes (`operates_location_of` claim? via which producer — see "Claim producers…") and what an unmatched census entity shows ("no PE evidence found (checked {date})" vs not-yet-checked — see "What 'checked' means…").
- NPPES API: when called beyond census misses.
