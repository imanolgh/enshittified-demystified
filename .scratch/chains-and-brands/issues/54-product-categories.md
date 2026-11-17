# Product categories: vocabulary and assignment

Type: grilling
Status: resolved
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
- **From engine "Extraction prompt rules"** (2026-11-15; GLOSSARY Brand): a brand's owner is whoever owns its name, never a licensee, so KitchenAid cookware made by Meyer is Whirlpool's brand. The extraction prompt claims a licensor when a page says "licensed" or "used under license", but a licensee's brand list that never says so still gives the licensee as owner: Meyer's "Our Brands" page lists KitchenAid, Rachael Ray, Ayesha Curry and Farberware, none of its five pages in the test set mentions licensing, and the category audit itself recorded Meyer as "Owner (cookware)" of Farberware and Rachael Ray. The brand page then shows the licensee as a co-owner, and a PE-owned licensee would make the licensed brand read PE-owned, which is false. This ticket decides whether licensing-heavy categories (cookware, women's apparel) launch and whether a licensed product line ("KitchenAid cookware") is a listed brand.

## Answer

Resolved 2026-11-16 in a grilling session (two rounds plus Q11, recorded under Comments). The launch list split off to [81 Launch industries](81-launch-industries.md), which waits on [80 Research: Industry screen](80-research-industry-screen.md) (resolved the same day) and new [82 Research: Where PE owns consumer brands](82-research-where-pe-owns-consumer-brands.md).

- **Term:** **industry** everywhere (code, docs, glossary, site); browse pages are industry pages, nav label "Industries"; "product category" and "category page" retired; the site never says "category".
- **Storage and assignment:** the engine's closed industry list in code (engine "What a business entity is"); a brand's industries come only from the industry brand lists that include it ("Category brand lists and checked" builds them); never from a document, the extraction LLM or the search model.
- **Several industries:** a brand appears on every industry page it belongs to, and its page names all of them.
- **Search:** matching (typo-tolerant over brand names, former and other names, company and owner names listing their brands, a word list per industry) plus a meaning part when matching finds little, by an embedding model or an LLM such as DeepSeek (the developer is open to an LLM), chosen in engine "Search and the demand log"; whatever does it only ranks and suggests.
- **Country filter:** none in version 1; the site states it covers brands' US businesses.
- **Landlord brands:** screened (25% strict); property managers ruled out.
- **Licensed product lines** are never separate brands ("KitchenAid cookware" is the KitchenAid brand, Whirlpool's).
- **Rollups** are never industry page entries; they show on a brand page when they own the brand; what a search for a rollup shows goes to engine "Graph endpoint and non-brand output shapes".
- **Glossary:** Industry entry amended, new entry Industry page, Rollup reworded to cover every industry ("local businesses that keep their own names").
- **Docs changed:** GLOSSARY.md, ADR 0004 and decisions.md §14 wording, evidence_layer_plan.md `entity_industries` note, the map.

Handed on:
- "Launch industries": the launch list and labels, the screen's five counting questions, the licensing gap if cookware launches.
- "Category brand lists and checked": industry lists are the only way a brand gets an industry; rollups are not entries; whether brands outside the launch industries are seeded (Walgreens).
- "Alternatives and affiliate links": regional availability of alternatives (the country-filter request).
- "Card wording and the how-this-works page": the brand page names every industry; the site states it covers US businesses.
- engine "Search and the demand log": the search method (already recorded there).
- engine "Graph endpoint and non-brand output shapes": what a search for a rollup's own name shows.

## Comments

### 2026-11-16 grilling session

Kept whole at first; the launch list was split off in round 1 (Q2 revised).

**Round 1** (all six accepted, Q2, Q4 and Q6 as revised):
- Q1 The word: **industry** everywhere (code, docs, glossary, website); the site's browse pages are industry pages, nav label "Industries"; "product category" and "category page" retired from the docs (ADR 0004 wording amended); the site never uses the word "category".
- Q2 Launch list (revised after the developer asked where the thirteen audited industries came from, answered: the 2026-11-02 pivot proposal's candidates, measured by the two audits, nobody screened outside them; and raised bowling alleys from an article, not audited): split off new grilling ticket [81 Launch industries](81-launch-industries.md), blocked by new [80 Research: Industry screen](80-research-industry-screen.md): the top ~10 brands in twelve new candidate industries (bowling and family entertainment, golf, ski resorts, child care, hair salons, funeral homes, collision repair, oil change and auto service, home services franchises, urgent care, physical therapy, landlord brands), about 1.2M tokens, launched 2026-11-16 as four background workers; full audits for any at about 20% PE or higher. Claude's first eight-industry proposal is recorded on 81, not decided.
- Q3 Several industries: a brand appears on every industry page it belongs to, and its page names all its industries.
- Q4 Search (revised twice: the developer asked for smarter search than string matching, then said they are open to an LLM such as DeepSeek helping; recorded on engine "Search and the demand log"): version 1 search has matching (typo-tolerant over brand names, former and other names, company and owner names listing their brands, and a fixed word list per industry) and a meaning part when matching finds little ("teeth cleaning", "pizza", an unseeded "Red Lobster"), by an embedding model or an LLM such as DeepSeek, chosen in "Search and the demand log". Boundary: it only ranks and suggests, never stores, labels or assigns anything.
- Q5 Country filter: none in version 1; the site states it covers brands' US businesses; regional availability of alternatives goes to "Alternatives and affiliate links".
- Q6 Landlord brands (revised): in the screen like any candidate; property managers such as Greystar ruled out (a manager's page would report the manager's owner, not the building's).

**Round 2 and Q11** (all accepted as recommended, with the rollup wording added to Q10):
- Q7 Licensed product lines: never a separate brand; "KitchenAid cookware" is the KitchenAid brand, its page names Whirlpool, Meyer doesn't appear; "Launch industries" revisits the licensee gap if a licensing-heavy industry launches.
- Q8 Rollups: industry pages list brands only; a rollup shows on a brand page when it owns the brand; a search for a rollup's own name goes to engine "Graph endpoint and non-brand output shapes". (The developer asked what a rollup is; answered with Heartland Dental against Aspen Dental, plus PetVet, Everstory, Sun Auto and Troon.)
- Q9 Assignment: a brand's industries come only from the industry brand lists that include it; nothing else assigns one.
- Q10 Glossary: new entry Industry page; Industry's Avoid line adds "product category" and the entry says a brand can belong to several; Rollup reworded from "local practices" to "local businesses that keep their own names", because the screen used it for funeral homes, golf clubs and auto shops.
- Q11 (the developer asked how the screen's industries were chosen; answered: Claude named them from general knowledge plus the bowling example, no scan): new research ticket 82 "Research: Where PE owns consumer brands" (portfolio pages of 50 to 100 PE firms, BDC borrower sectors, screens of anything new; roughly 1 to 2M tokens); "Launch industries" waits on it too. The developer wants to run it right after this ticket.
