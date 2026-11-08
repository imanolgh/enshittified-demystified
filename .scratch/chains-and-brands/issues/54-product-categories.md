# Product categories: vocabulary and assignment

Type: grilling
Status: open
Blocked by: 52, engine/12  (Research: Category audit pilot; What a business entity is)
Map: [chains-and-brands](../map.md)

## Question

What is a product category (term, list, storage), which categories launch, can a brand sit in several, and are search by product type and a country filter in version 1?

## Context

- "Category" collides with `BusinessCategory` (ADR 0001); the engine term for verticals is fixed in engine "What a business entity is". This ticket names the chains-and-brands list and its GLOSSARY entry.
- Pivot proposal, **not decided**: about 8 to 10 categories and roughly 1,000 chains and brands at launch; healthcare chains (Aspen Dental, VCA and similar) as one category, which keeps part of the dentist and vet story with no census; avoid leading with appliances (PE probably rare; Worse on Purpose says appliances and grocery stores are next for it).
- The audit (pilot first) supplies % PE, BDC overlap and affiliate availability per category; the selection test (~20% PE or higher, at least three affiliate categories) is a proposal.
- Search by product type and a country filter were both requested repeatedly (handoff §5).
- **From engine "What a business entity is"** (2026-11-05, [ADR 0005](../../../docs/adr/0005-brands-companies-locations-separate.md)): the engine term is **industry** (GLOSSARY), one closed list in code shared by both products, zero or more per brand, company or location, assigned by code and never by the LLM. This ticket picks the chains values, the website label and whether a brand shows several.
- **From "Predicate semantics"** (2026-11-05; role table in evidence_layer_plan.md §4 `claims`): licensing is not in the predicate set for v1. If this ticket adds a category built on licensing (such as apparel), reopen it in engine "Predicate semantics" (a `licensed_to` brand → company predicate was the option turned down).
- **From "Brand and chain model"** (2026-11-06): category lists hold brands, and a brand is a name a consumer sees on a storefront, menu board or product label. A rollup whose practices keep their own names (AEG Vision, if so) is a company, not a brand, so eyewear's rollup rows need a ruling here. A brand page reports the owner of the brand's US business; whether v1 has a country filter stays here.
- **From "Research: Full category audit (ten remaining candidates)"** (2026-11-07; findings in research/category-audit-full.md): numbers now exist for 13 categories (10 new plus the pilot's 3). By brand row after Form ADV: dental 50%, vet 52%, car washes 53%, women's apparel 38%, restaurants and gyms 30%, mattresses 27%, pet stores 19%, eyewear and cookware 13%, supplements 10%, dollar and discount 8%, pharmacies 3%. Brand-direct affiliate programs cluster in mattresses and cookware (10 each). Several lists are composites or have fewer than 30 brands; counting choices are in findings §7.
- **From engine "Funds and their investment firm"** (2026-11-07; ADR 0001 amended): the developer would like users to see which apartments and houses are owned or run by PE; that is a separate parked [housing map](../../housing/map.md) (ADR 0004 amended). **Landlord brands** are a candidate category here: landlords that own the homes they rent under their own name, such as single-family rental companies (Invitation Homes, Progress Residential, FirstKey Homes; owners from memory, to be confirmed by an audit like the others, about 340k tokens). Whether they are in v1, and whether property managers such as Greystar are included (their page would report the manager's owner, not the building's), is this ticket's.
- **From engine "Category precedence and public companies"** (2026-11-07; ADR 0001 amended): a public company now reads PE minority stake when a PE firm's stake comes from a 13D or from a 13G not filed under Rule 13d-1(b), so the audits' strict counts become the rule once each holder's filing box is checked: restaurants 12 of 30 (Restaurant Brands for Burger King and Popeyes, Wendy's), gyms 10 of 30 (Life Time), pharmacies 2, dollar and discount 4, mattresses 9. Large fund managers' passive 13Gs never count.
