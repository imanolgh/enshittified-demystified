# What a business entity is

Type: grilling
Status: resolved
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

## Comments

**2026-11-05 grilling, round 1** (developer accepted all four recommendations):
1. Entity types: `business` is replaced by `brand` (a consumer-facing name; owns nothing), `company` (a legal entity that owns, is owned or operates) and `location` (one physical site). Brands and locations are the stable lookup targets; companies are the owners and operators that change. No `chain` type. Chains v1 may leave locations empty ("Brand and chain model" decides).
2. Family owners: a `family` entity type, one person or a family owning in their own name, named only as the source names them, no personal identifiers, never searchable as a person. Trusts and ESOP trusts are `company` rows with owner kind `trust` / `employee_owned`.
3. Identifiers: an `entity_identifiers` table, one row per (entity, scheme, value), citing its source document, closed scheme list, a strong identifier held by one entity only. `place_id` is the one scheme with no document (ADR 0003). Names stay in `entity_aliases`; domain moves to identifiers.
4. Vocabulary: one shared GLOSSARY term, **industry**, for both products. Ticket 54 picks the chains launch values and any website label.
GLOSSARY.md: added Brand, Company, Location, Family, Industry.

**2026-11-05 grilling, round 2** (developer accepted all six recommendations):
5. `rollup` is dropped as an entity type; a rollup is a `company` row, and whether a page calls it a rollup is wording. A government body that owns something is a `company` row with owner kind `government`. Types: `brand, company, location, family, investment_firm, fund, retirement_plan, insurer`.
6. Identifier schemes (closed list): `cik`, `ticker`, `ein`, `crd`, `sec_file_number` (801-, 802-, 814-), `private_fund_id` (805-), `domain`, `phone`, `place_id`, `npi`. Strong (one entity only): cik, ein, crd, sec_file_number, private_fund_id, place_id, npi; a second holder is a resolution or merge signal. Weak (may repeat): ticker, domain, phone. Added later: SoS entity number, license number, plan EIN+PN when their efforts start; trademark serial only if USPTO is adopted. History of changed values goes to "Entity lifecycle". `alias_type` = `dba | legal_name | former_name`.
7. `entity_addresses`: entity, kind (`site | principal_office | mailing`), structured fields, source document. Registered-agent addresses never stored as an entity's address. Places-formatted addresses never stored. `jurisdiction` = place of formation from a filing, companies, funds and investment firms only.
8. Location identity: one place where one company at a time serves customers, under zero or more brands. Same address is not same location; one location can carry several brands; a new operator keeps the location; a move is a new location. A `brand` row exists only for a name spanning several locations or sold as a product.
9. Canonical name: ranked pick from sourced names. Companies, funds, firms, families: official filing > own site > own press release > news, newest wins a tie. Brands and locations: own site first, then the same order. Input name shows until a document gives one. Every name kept as an alias with its source; Places names never stored.
10. Industries: zero or more per brand, company or location, from one closed list in code. Assigned by code from where the entity came in (brand list, intake column, NPPES taxonomy), recorded with that origin; never by the LLM, never a claim. None means fan-out runs its default set. The engine allows several; "Product categories" decides the display.

**2026-11-05 grilling, round 3** (developer accepted all; asked for and got a plain recap of what Q1, Q2 and Q5 decided before saying yes):
11. Which address shows: the Q9 name ranking applies to addresses. Normalization stays with "Entity resolution algorithm".
12. ADR 0005 written for the entity split.
13. Doc edits: evidence_layer_plan.md §4 rewritten; research_flows.md:34 one-line fix; research_flows.md:148 left to "Claim value schemas".
14. New ticket 64, "USPTO trademark data: adopt as a source?", blocking "Category brand lists and brand-level checked".
15. Resolution plan approved.

## Answer

Resolved 2026-11-05 by grilling (rounds above). The record lives in [ADR 0005](../../../docs/adr/0005-brands-companies-locations-separate.md) (the split, family, dropped types), `docs/evidence_layer_plan.md` §4 (identifiers, addresses, names, industries) and `GLOSSARY.md` (Brand, Company, Location, Family, Industry).

- **What a "business" is:** no longer an entity type. It splits into `brand` (a name sold at several locations or on products; owns nothing), `company` (a legal entity that owns, is owned or runs locations; includes trusts, ESOP trusts, nonprofits, government bodies) and `location` (one place where one company at a time serves customers, under zero or more brands; a new operator keeps it, a move starts a new one). `rollup` is dropped (a rollup is a company); no `chain` type.
- **Family owners:** a `family` entity, one person or a family owning in their own name, named as sources name them, no identifiers, never searchable as a person. "No person entities" now means no individual profiles.
- **Types:** `brand, company, location, family, investment_firm, fund, retirement_plan, insurer`.
- **Identity data:** `entity_identifiers` (closed schemes `cik, ticker, ein, crd, sec_file_number, private_fund_id, domain, phone, place_id, npi`; strong ones held by one entity only; each row cites its document except `place_id`); `entity_addresses` (`site | principal_office | mailing`, structured, sourced; no registered-agent or Places addresses); `jurisdiction` = place of formation for companies, funds and firms; `alias_type` = `dba | legal_name | former_name`.
- **Canonical name and address:** picked by code. Companies, funds, firms and families rank official filing first; brands and locations rank their own site first; newer wins a tie; input name until a document gives one; nothing from Places.
- **Industry:** the one GLOSSARY term for line of business across both products. Zero or more per brand, company or location, from one closed list in code, assigned by code from where the entity came in, never by the LLM, never a claim. Chains values and display: "Product categories".
- **Left to other tickets** (context lines added): location→brand link ("Predicate semantics"); typing a quoted name ("Entity resolution algorithm"); which types get a category ("Category precedence and storage"); closing a moved location and identifier history ("Entity lifecycle"); family, trust and government owner kinds ("Owner kind"); new table names and the industry `origin` value set ("Schema conventions"); locations in chains v1 ("Brand and chain model"); NPI on company or location ("Local business identity and resolution"); USPTO adoption (ticket 64).
