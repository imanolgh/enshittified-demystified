# Brand licensors and licensees on the brand page

Type: grilling
Status: open
Blocked by: 83, 84  (What the product says about owners that aren't PE; Research: Brand licensors and where licensees are stated)
Map: [non-pe-owners](../map.md)

## Question

Does a brand licensor get its own owner kind, does a brand page show the licensee that makes or sells the product, and if so, what predicate and evidence carry the license and how is the gap closed where a licensee's own brand list makes it look like the owner?

## Context

- Charted 2026-11-16. **Not worked until the developer unparks this map.**
- The licensing facts put to the developer while charting (not decided): (i) the name's owner is a licensing company, which v1 already shows; (ii) who actually makes or sells the product, the licensee; (iii) both. Claude recommended (iii), because the licensee makes the product the shopper holds.
- v1 rules this ticket would change or extend:
  - A brand's owner is whoever owns the name, never a licensee (GLOSSARY "Brand").
  - The prompt claims the licensor and gives the licensee nothing; IP holding companies are claimed as written (engine "Extraction prompt rules", Q2 and Q7).
  - Licensing is not a predicate in v1; a `licensed_to` brand → company predicate was the option turned down (engine "Predicate semantics", Q6). Adding a predicate is a schema decision for the developer (CLAUDE.md), recorded here as an amendment to that ticket's role table, the way the housing map records the location → `owned_by` role it would add.
  - Licensed-run brands read like any brand, with the franchise note covering who runs the stores (chains "Brand and chain model", Q5). Licensed product lines are never brands (chains "Product categories: vocabulary and assignment", Q7).
- The known gap: a licensee's brand list that never says "licensed" gives the licensee as owner. Meyer's "Our Brands" page lists KitchenAid, Rachael Ray, Ayesha Curry and Farberware, and none of its pages in the test set mentions licensing (chains "Product categories", context). For v1, chains "Launch industries" revisits it only if a licensing-heavy industry launches.
- An owner kind for licensors would need a term in the owner-kind term table and a decision on its category, which hangs on "What the product says about owners that aren't PE".
- Stored documents can be re-read by a later prompt version (map Notes), so licensee claims can be backfilled from what v1 fetched.
- Facts: "Research: Brand licensors and where licensees are stated".
