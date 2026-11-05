# Local business identity and resolution

Type: grilling
Status: open
Blocked by: engine/12, engine/19, 06, 48  (What a business entity is; Entity resolution algorithm; Research: NPPES bulk file and API; Research: Rollup rosters for omitted medical specialties)
Map: [local-businesses](../map.md)

## Question

For the local product, which NPPES records become entities, how do local verticals map to NPPES taxonomy codes, where do coordinates come from, and where do the census and the NPPES API sit in entity resolution?

## Context

Split out of engine tickets on 2026-11-04 (ADR 0004: the engine is shared, local is parked). The bullets below were moved word for word.

From "What a business entity is":
- **NPPES scope**: Type 2 orgs only, or Type 1 individuals too? Solo practices often have only Type 1, and persons are not entities (build_roadmap.md:88; research_flows.md:15; pre-launch-seeding.md:82).
- **Geocoding**: the map needs coordinates; Places is lazy-only and may be place_id-only (ADR 0003:12). Pick a free geocoder or rule coordinates out of the engine (see "Research: Google Places terms, pricing and a free geocoder").
- **Taxonomy mapping**: the business vertical vocabulary (term fixed in engine "What a business entity is") needs a mapping to NPPES taxonomies. The mapping includes optometry (`152W*`), confirmed as Tier 1 on 2026-10-31. "Research: Rollup rosters for omitted medical specialties" feeds which specialties join.

From "Entity resolution algorithm":
- **Census and NPPES API in the lookup order**: the doc contradictions are listed in engine "Entity resolution algorithm" (Lookup order bullet); this ticket places the census and the NPPES API once that ticket fixes the general order.
- **Ambiguous retry trigger**: after each NPPES/SoS/board refresh (ADR 0002:14) — confirm.
- **From engine "What a business entity is"** (2026-11-05, [ADR 0005](../../../docs/adr/0005-brands-companies-locations-separate.md)): `npi` is an `entity_identifiers` scheme; whether it sits on the company (the PLLC) or the location is this ticket's call. SoS entity number and license number join the scheme list when local unparks. A local practice is a location run by a company; a single-site independent has no brand row.
