# What a business entity is

Type: grilling
Status: open
Blocked by: 09  (Research: Google Places terms, pricing and a free geocoder)
Map: [engine](../map.md)

## Question

What real-world thing does a `business` entity represent — a physical location, an NPI organization record, or a legal entity — and what identity data does an entity carry?

## Context

- evidence_layer_plan.md:89 gives one `place_id` and one `npi` per entity; research_flows.md:16–17 matches roster *locations* to census *organizations*; :32 shows a PLLC plus a management LLC for one clinic; SoS lists legal entities; an NPI org may span several sites. The census match and the map both depend on this.
- **Person data / family owners**: "no person entities" (evidence_layer_plan.md:88) vs owner kinds `family, trust, employee_owned` and category `family_owned` (ADR 0001:5,20) — what node is a family owner? NPPES authorized officials and SoS officers are resolution signals but not entities.
- **Identity columns**: entities have no address, city, state, zip, lat/lng, phone, website, yet ADR 0002:14 tiebreaks on address/phone/NPI. Identifiers missing: EIN+PN (plans), CIK, CRD/SEC adviser numbers, SoS entity number, vet license/premises number. Columns on `entities` or an `entity_identifiers` table?
- **Canonical name/address precedence** across NPPES, SoS, roster, license board (Places content may not be storable).
- **Business vertical vocabulary** (dental, vet, funeral, HVAC…): the intake CSV and "category-aware" fan-out depend on it (evidence_layer_plan.md:145,158; research_flows.md:39; decisions.md:34–36; pre-launch-seeding.md:26–40); there is no enum or column, and the word "category" collides with ADR 0001's BusinessCategory. Needs a GLOSSARY term. Chains and brands need the same kind of term for product categories (restaurants, gyms…); which categories launch is decided in chains-and-brands "Product categories: vocabulary and assignment".
- **Brands and chains** (ADR 0004): the active product looks up national brands and chains. Is a brand or a chain its own entity, separate from the company that owns it and from its locations, and what identity data does it carry? The product rules (brand-level verdicts, franchises, licensing) are in chains-and-brands "Brand and chain model"; this ticket fixes what the engine stores.
- **Moved out 2026-11-04 (ADR 0004 split)**: NPPES scope (Type 1 vs Type 2), the NPPES taxonomy mapping (incl. optometry) and geocoding for the map are in local-businesses "Local business identity and resolution". Ticket 48 (medical rosters research) now blocks that ticket, not this one.
