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
