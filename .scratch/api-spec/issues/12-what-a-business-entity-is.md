# What a business entity is

Type: grilling
Status: open
Blocked by: 06, 09  (Research: NPPES bulk file and API; Research: Google Places terms, pricing and a free geocoder)
Map: [api-spec](../map.md)

## Question

What real-world thing does a `business` entity represent — a physical location, an NPI organization record, or a legal entity — and what identity data does an entity carry?

## Context

- evidence_layer_plan.md:89 gives one `place_id` and one `npi` per entity; research_flows.md:16–17 matches roster *locations* to census *organizations*; :32 shows a PLLC plus a management LLC for one clinic; SoS lists legal entities; an NPI org may span several sites. The census match and the map both depend on this.
- **NPPES scope**: Type 2 orgs only, or Type 1 individuals too? Solo practices often have only Type 1, and persons are not entities (build_roadmap.md:88; research_flows.md:15; pre-launch-seeding.md:82).
- **Person data / family owners**: "no person entities" (evidence_layer_plan.md:88) vs owner kinds `family, trust, employee_owned` and category `family_owned` (ADR 0001:5,20) — what node is a family owner? NPPES authorized officials and SoS officers are resolution signals but not entities.
- **Identity columns**: entities have no address, city, state, zip, lat/lng, phone, website, yet ADR 0002:14 tiebreaks on address/phone/NPI. Identifiers missing: EIN+PN (plans), CIK, CRD/SEC adviser numbers, SoS entity number, vet license/premises number. Columns on `entities` or an `entity_identifiers` table?
- **Geocoding**: the map needs coordinates; Places is lazy-only and may be place_id-only (ADR 0003:12). Pick a free geocoder or rule coordinates out of the engine (see "Research: Google Places terms, pricing and a free geocoder").
- **Canonical name/address precedence** across NPPES, SoS, roster, license board (Places content may not be storable).
- **Business vertical vocabulary** (dental, vet, funeral, HVAC…): the intake CSV and "category-aware" fan-out depend on it (evidence_layer_plan.md:145,158; research_flows.md:39; decisions.md:34–36; pre-launch-seeding.md:26–40); there is no enum or column, and the word "category" collides with ADR 0001's BusinessCategory. Needs a GLOSSARY term and a mapping to NPPES taxonomies.
