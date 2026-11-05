# Predicate semantics

Type: grilling
Status: resolved
Blocked by: 12  (What a business entity is)
Map: [engine](../map.md)

## Question

For each predicate: what are its subject/object roles and direction, which predicates are ownership hops for the chain walk, do different ownership predicates corroborate each other, and how are franchises, employer→plan links and non-relation facts expressed?

## Context

- **Direction**: `operates_location_of(BrightSmiles → SmilePartners)` reads backwards (research_flows.md:56–57,72). Default: a role table in contracts; edge.from = claim.subject.
- **Corroboration across predicates**: Stage 5 groups by exact (subject, predicate, object) (evidence_layer_plan.md:190), so a press `acquired_by` and a portfolio `owned_by` for the same pair never corroborate — yet research_flows.md:71–72 treats them as verifying each other.
- **Franchises**: decisions.md:38 and pre-launch-seeding.md:54 require separate brand and operator verdicts; ADR 0001:13 counts `operates_location_of` as an ownership hop, so franchise links via it would make franchisee locations PE-owned. No predicate links location → brand. A2 accepts restaurants, so this can't wait for the national-brands launch (which is post-MVP: pre-launch-seeding.md:63 vs monetizationideas.md:34). ADR 0004 (2026-11-04) has since made chains and brands the launch product, so franchises are first-order; the product side is in chains-and-brands "Brand and chain model".
- **Licensing** (added 2026-11-04): a brand licensed to an operator (common in clothing: one company owns the brand, another makes or sells under it) can't be expressed with the closed predicate set. Is it a new predicate, a value on an existing one, or out of scope? The product side is in chains-and-brands "Brand and chain model".
- **Facts that aren't relations**: BDC fund-level totals (PIK %, non-accrual %; bdc-parser SKILL:16; research_flows.md:132); owner-kind evidence (see "Owner kind…"). CAFR asset-class allocations are out of scope.
- **Employer ↔ plan**: moved out 2026-11-04 (adr 0004 split) to retirement "Form 5500 ingestion and the headline exposure number" (deferred).
- **`holds_position`**: semantics never spelled out.
- Adding a predicate is a schema decision (CLAUDE.md:30) — this ticket is where it's made if needed.
- **From "What a business entity is"** (2026-11-05, [ADR 0005](../../../docs/adr/0005-brands-companies-locations-separate.md)): a brand owns nothing and a company owns it, and a location is run by one company at a time under zero or more brands. No predicate links a location to its brand(s). Brand → company and company → location need roles and direction here.
- **From "Schema conventions"** (2026-11-05; conventions in evidence_layer_plan.md §4; no on-demand research per decisions.md §15): "A2 accepts restaurants" no longer applies, since searches never start research. Franchises stay first-order because chains are the launch product (ADR 0004).

## Comments

### Round 1 (2026-11-05)

Boundaries: owner-kind evidence and the fund–firm link are "Owner kind: storage, evidence and the fund–firm link"; what ends a hop is "Conflict, succession and co-investors"; `value` is "Claim value schemas"; `renamed_from` is "Entity lifecycle"; brand page wording is chains-and-brands "Brand and chain model".

- **Direction** (Q1): every claim reads as a sentence from subject to object (`Subway acquired_by Roark`, `Fund lends_to Borrower`). A role table in `contracts.py` names both sides; an edge's from side is the claim's subject. `operates_location_of` is renamed `operated_by` (`location operated_by company`), so every ownership predicate points from the thing owned up to its owner and the chain walk follows from → to.
- **One hop, two predicates** (Q2): `acquired_by` and `owned_by` are evidence for the same ownership hop and corroborate each other. The published edge is `owned_by`; an `acquired_by` claim supplies the start date, an `owned_by` claim confirms the hop as of its document's date. `operated_by` is a different hop kind and never corroborates `owned_by`.
- **A brand's owner** (Q3, option b): a brand's owner may be a company, fund, investment firm or family, so "Roark Capital acquired Subway" can link the brand straight to Roark. The chain may skip the operating company and show a separation degree one lower than reality. ADR 0005's line becomes "a brand owns nothing; its owner is usually a company". Brand-vs-company resolution of a name stays with "Entity resolution algorithm".
- **Location → brand** (Q4, option a): identity data, not a predicate. Code producers (store locators, rosters) write `location_brands` rows (location, brand, source document, producer), like industries: never a claim, never a hop, no confidence label. The brand verdict walks brand → owner; the store verdict walks location → `operated_by` → operator. Code tells a company-run store (operator in the brand owner's chain) from a franchised one.
- **Money predicates** (Q5): `lends_to` is fund → company (a BDC loan row). `holds_position` is investor → company or fund: a holdings-table position that is neither a loan nor stated ownership (BDC equity rows such as common units, warrants, preferred now; CAFR fund commitments later), which keeps a BDC warrant from becoming a control hop. `allocates_to` is retirement plan or insurer → fund, kept in the vocabulary and parked with the retirement map. None is an ownership hop. BDC fund-level totals (PIK %, non-accrual %) go to the retirement map; the bdc-parser skill drops them. Whether a "control investments" row also yields `owned_by` is "BDC discovery and Schedule of Investments parsing".
- **Licensing** (Q6, option a): not in v1. The brand page reports the brand's owner; licensee-run stores are covered by `operated_by`; licensed products don't show. Revisit when "Product categories" adds a category built on licensing, such as apparel.

### Round 2 (2026-11-05)

- **Role table** (Q7):

  | Predicate | Subject | Object | Ownership hop |
  |---|---|---|---|
  | `owned_by`, `acquired_by` | brand, company, investment_firm, insurer | company, fund, investment_firm, family | yes |
  | `operated_by` | location | company | yes |
  | `lends_to` | fund | company | no |
  | `holds_position` | fund, retirement_plan, insurer | company, fund | no |
  | `allocates_to` | retirement_plan, insurer | fund | no |
  | `renamed_from` | set by "Entity lifecycle" | | no |

  A location is only operated, never owned. A fund is never the subject of `owned_by` (the fund–firm link is "Owner kind…"; an LP stake isn't a hop). A family is never owned and never runs a location directly. An investment firm or insurer can be owned.
- **Mismatches** (Q8): after names are resolved, a claim whose subject or object type the table doesn't allow is `rejected` with `sanity_check_failed` (no new reason). The resolver only considers the types the predicate allows; when both fit (a brand and a company named "Subway" in `acquired_by`), the choice is "Entity resolution algorithm"'s, and where this runs is "Claim identity"'s.
- **Glossary** (Q9): new entry **Operator** ("The company that runs a location. A franchisee is the operator of its stores. A location is company-run when its operator is in the brand owner's ownership chain, and franchised when it isn't." Avoid: manager, franchisee as the general term). **Hop** reworded: "One link between two neighbours in an ownership chain: an owner above what it owns, or the operator above a location." Widening "Ownership chain" stays with "Brand and chain model".
- **`location_brands`** (Q10): `id, location_id, brand_id, source_document_id, producer, producer_version`; source document required (code producers only); unique on (location, brand, document); several brands per location (a Taco Bell/KFC combo store has two rows). Identity records gain a list of brand names, matched to brand entities by "Entity resolution algorithm". A store that changes brand gets a new row from a newer document; how the old row stops counting is "Entity lifecycle"'s.

## Answer

Resolved 2026-11-05 in a grilling session (two rounds, recorded under Comments).

- **Direction.** Every claim reads as a sentence from subject to object, and an edge's from side is the claim's subject. `operates_location_of` is renamed **`operated_by`** (`location operated_by company`), so every ownership predicate points from the thing owned up to its owner.
- **Role table** (in `contracts.py`):

  | Predicate | Subject | Object | Ownership hop |
  |---|---|---|---|
  | `owned_by`, `acquired_by` | brand, company, investment_firm, insurer | company, fund, investment_firm, family | yes |
  | `operated_by` | location | company | yes |
  | `lends_to` | fund | company | no |
  | `holds_position` | fund, retirement_plan, insurer | company, fund | no |
  | `allocates_to` | retirement_plan, insurer | fund | no |
  | `renamed_from` | set by "Entity lifecycle" | | no |

  After resolution, a claim whose entity types don't fit is `rejected` with `sanity_check_failed`. The resolver only considers the types a predicate allows.
- **One hop, two predicates.** `acquired_by` and `owned_by` back the same ownership hop and corroborate each other. The published edge is `owned_by`; `acquired_by` supplies the start date, `owned_by` confirms the hop as of its document's date. `operated_by` is a separate hop kind.
- **A brand's owner** may be a company, fund, investment firm or family (ADR 0005 amended: "its owner is usually a company"). The chain may skip the operating company.
- **Location → brand** is identity data: `location_brands (id, location_id, brand_id, source_document_id, producer, producer_version)`, written only by code producers, unique on (location, brand, document), several per location. Never a claim, never a hop. Identity records gain a list of brand names.
- **Franchise rule.** The brand verdict walks brand → owner. The store verdict walks location → `operated_by` → operator → owners. A store is company-run when its operator is in the brand owner's chain, franchised when it isn't.
- **Money predicates.** `lends_to`: a BDC loan row. `holds_position`: a holdings-table position that is neither a loan nor stated ownership (BDC equity rows now, CAFR fund commitments later). `allocates_to`: parked with the retirement map. None is a hop.
- **Not in the predicate set:** BDC fund-level totals (moved to the retirement map), owner-kind evidence ("Owner kind…"), licensing (not in v1; revisit when "Product categories" adds a category built on licensing).
- **Glossary:** new **Operator**; **Hop** reworded to include the operator above a location.
- No new ADR; ADR 0001 (hop list) and ADR 0005 (brand owner, location → brand) amended in place.

Handed on:
- "Entity lifecycle": `renamed_from`, retiring old `location_brands` rows.
- "Owner kind…": the fund–firm link, owner-kind evidence.
- "Claim value schemas": per-predicate values, including what `owned_by`'s date means.
- "Claim identity" and "Entity resolution algorithm": role-table filtering and brand-vs-company names.
- "Citation verification rules": the type-mismatch sanity check.
- "Conflict, succession and co-investors" and "Edge lifecycle": hops built from two predicates, operator changes.
- "Category precedence and storage" and "Card and graph shapes": two verdicts per store.
- "Rosters, portfolio pages and the registry": rosters write `operated_by` claims and `location_brands` rows.
- "BDC discovery and Schedule of Investments parsing": equity rows, "control investments" rows.
- chains-and-brands "Brand and chain model" and "Product categories".
