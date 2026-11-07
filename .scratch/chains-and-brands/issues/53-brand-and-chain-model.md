# Brand and chain model

Type: grilling
Status: resolved
Blocked by: engine/12, engine/15  (What a business entity is; Predicate semantics)
Map: [chains-and-brands](../map.md)

## Question

What are a brand and a chain in the product, whose ownership does a brand page report (the brand owner, the operator, the franchisee), and how do franchises and licensing show up?

## Context

- Pivot proposal (handoff §2): "A chain is a brand with locations. Brand-level verdicts first, with the franchise rule from `docs/decisions.md` §4." Not decided.
- **Franchise rule** (decisions.md §4, still in force per ADR 0004): ownership is modeled at two levels, brand ownership and location operator; a search returns both verdicts. pre-launch-seeding.md:59 repeats it for restaurants.
- **Licensing**: a brand licensed to an operator (clothing especially) can't be expressed by the closed predicate set; the predicate question is in engine "Predicate semantics". This ticket decides what the brand page says about it.
- **GLOSSARY**: "ownership chain" is defined from "a local business" (ADR 0004 consequence: this ticket owns widening it). "Chain" (a set of locations) and "ownership chain" (a path of ownership links) also collide as words.
- **Public companies** (Chipotle, Walmart, Target, Home Depot) don't flag; how they read is in "Card wording and the how-this-works page".
- Which entity rows exist (brand, company, location) is fixed in engine "What a business entity is"; this ticket is the product meaning.
- Load `grilling` and `domain-modeling`.
- **From engine "What a business entity is"** (2026-11-05, [ADR 0005](../../../docs/adr/0005-brands-companies-locations-separate.md)): there is no `chain` entity type. Brands, companies and locations are separate rows; a brand row exists only for a name that spans several locations or is sold as a product. Whether chains v1 creates location rows at all is this ticket's call.
- **From "Claim producers and the claims door"** (2026-11-05; summary in evidence_layer_plan.md "Producers and the door"): if v1 keeps locations, store locators are read by `selector` producers. JSON endpoints are allowed when robots.txt permits them and they feed the public locator page. Each record is one document and an identity record for the location (name, address, phone); how a location links to its brand is engine "Predicate semantics". Claims from a brand's own site are `company_site` evidence, so `reported` until a second source agrees.
- **From "Predicate semantics"** (2026-11-05; role table in evidence_layer_plan.md §4 `claims`): a location's brands are `location_brands` identity rows (never a hop), and the store verdict follows `operated_by` to the operator, so the franchise rule's two verdicts exist in the graph. Company-run vs franchised is computed (glossary "Operator"). A brand's owner may be a company, fund, firm or family. **Licensing is not in v1**: the brand page reports the brand's owner, licensee-run stores are covered by `operated_by`, licensed products don't show.

## Comments

### Round 1 (2026-11-06)

Boundaries: share counting and a PE-controlled public company are engine "Owner kind" and "Category brand lists and brand-level checked"; card text is "Card wording and the how-this-works page"; pages are "Website pages and shareable cards"; categories are "Product categories".

- **Brand, not chain** (Q1): the spec, code and glossary say brand. A chain is a brand that sells at its own locations (Dunkin'); a product brand (Ray-Ban) uses the same page and model. Marketing copy may still say "chains". Brand's _Avoid_ line gains "chain (as its own kind of thing)".
- **One brand per consumer-facing name** (Q2): every name on a storefront, menu board or product label is its own brand row (LensCrafters, Pearle Vision, America's Best). A name that only groups brands is a company, never a brand (Luxottica Retail, Inspire Brands, Xponential Fitness). A brand and a company with the same name are two rows (Wendy's, The Wendy's Company). An old name (Dunkin' Donuts) is a former-name alias. The developer proposed, then dropped, a "parent company" term: a company can be owned and own at once, and `owned_by` edges already say who is above whom, so no role term or field is needed.
- **Brand pages at launch; a store map after** (Q3): launch has brand pages reporting the brand owner. The first follow-up after launch is a store map from brand store locators: each store's address and brand, with the brand's verdict labeled as the brand's and a line saying the store's operator isn't checked (a Dunkin' pin never reads "PE-owned"). No operators: franchise disclosures, franchisee research and the privacy question stay parked with local businesses. The store map goes in the map's "Not yet specified" beside "BDC lenders on brand pages". decisions.md §4 gets a note that v1 and the store map show the brand verdict. Facts the developer weighed: seeding stores costs about nothing in API money (selector code, not the LLM; no Places; locator data usually carries coordinates; open map tiles cost storage and bandwidth only); the ongoing cost is one locator config per brand and its upkeep; a few hundred thousand stores is small for Postgres with a geographic index. Operators would need Franchise Disclosure Document Item 20 lists (often naming individuals) and per-franchisee research, roughly $0.12 per entity per pass on Sonnet batch.

### Round 2 (2026-11-06)

- **Franchise note** (Q4, option a): every brand page carries the same note, such as "This page reports who owns the brand. A store can be run by a different company, such as a franchisee." No per-brand operating-model facts (those would need a new kind of sourced fact). Exact text: "Card wording and the how-this-works page".
- **Licensed-run brands** (Q5, option a): a brand whose stores another company runs under license (BJ's Optical, Target Optical) reads like any brand: the page reports the brand's owner, and the Q4 note covers who runs the stores.
- **Rollups** (Q6): a rollup whose practices keep their own names (AEG Vision, if so) is a company, never a brand on a category list; in v1 it appears only where it owns a brand. A rollup that puts its name on its offices (MyEyeDr.) is a brand. Locally named practices are locations and come with the parked local-business work, with the rollup's roster naming each practice's operator. Eyewear's list: "Product categories" and "Category brand lists and brand-level checked".
- **US owner** (Q7): a brand page reports the owner of the brand's US business (Pizza Hut: LongRange Capital, though Yum China holds mainland China). Owners elsewhere don't show in v1. A country filter is "Product categories".
- **Glossary** (Q8): **Ownership chain** becomes "The ordered list of owners from a brand (or, later, a location) up through each owner above it, ending at the first private equity owner or at the top owner, e.g. Dunkin' → Inspire Brands → Roark Capital. A brand can have more than one chain." (ending at the top matches ADR 0001's walk; fund vs firm stays with "Owner kind"). **Separation degree** starts "from a brand (or, later, a location)". The category entries that still say "business" change in "Category precedence and storage".

## Answer

Resolved 2026-11-06 in a grilling session (two rounds, recorded under Comments).

- **Brand, not chain.** The spec, code and glossary say brand. A chain is a brand that sells at its own locations; a product brand uses the same page and model. Marketing copy may say "chains".
- **What a brand is.** Every name on a storefront, menu board or product label is its own brand row (LensCrafters, Pearle Vision, America's Best). A name that only groups brands is a company (Luxottica Retail, Inspire Brands). A brand and a same-named company are two rows (Wendy's, The Wendy's Company). An old name is a former-name alias. No "parent company" term: `owned_by` edges already say who owns whom.
- **Rollups.** A rollup that puts its name on its offices (MyEyeDr.) is a brand. One whose practices keep their own names is a company, never on a category list, and in v1 appears only where it owns a brand. Its practices come with the parked local work.
- **Whose ownership a brand page reports:** the owner of the brand's US business (Pizza Hut: LongRange Capital, though Yum China holds mainland China), walked up its ownership chain under ADR 0001.
- **Franchises.** Launch has brand pages only, with no locations and no operators. Every brand page carries the same franchise note (a store can be run by a different company, such as a franchisee); no per-brand operating-model facts. The first follow-up after launch is a **store map** from brand store locators: address and brand per store, the brand's verdict labeled as the brand's, and a line saying the store's operator isn't checked. Operators (franchise disclosures, franchisee research) stay parked with local businesses.
- **Licensing.** A brand whose stores another company runs under license (BJ's Optical) reads like any brand: the page reports the brand's owner and the franchise note covers who runs the stores.
- **Glossary:** Brand's _Avoid_ gains "chain (as its own kind of thing)"; **Ownership chain** and **Separation degree** now start from a brand (or, later, a location), and a chain ends at the first private equity owner or the top owner.
- No ADR (launch sequencing is easy to reverse; ADR 0004 unchanged).

Handed on:
- "Product categories": eyewear's rollup rows, a country filter.
- "Category brand lists and brand-level checked": lists hold consumer-facing brand names only.
- "Card wording and the how-this-works page": the franchise note, store-pin wording, owner labels.
- "Website pages and shareable cards": no store pages at launch, whether owners get pages.
- engine "Rosters, portfolio pages and the registry": launch needs portfolio pages; locator selectors are for the store map.
- engine "Entity resolution algorithm": no location matching at launch.
- engine "Category precedence and storage": brand categories only at launch; the glossary's category entries.
- engine "Card and graph shapes": one verdict per card at launch.
- local-businesses map: franchisee operators for chain stores.
