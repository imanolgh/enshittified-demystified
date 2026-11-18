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
- **From chains "USPTO trademark data: adopt as a source?"** (2026-11-17): USPTO is not adopted for v1; the whole question moved here, because licensing is its main value. Open here if USPTO is taken up: adoption and access (bulk files need a USPTO.gov account, the bulk API an ID.me check, the TSDR API its own key), whether it self-verifies as an official filing (recording is "ministerial"; Jersey Mike's owner field disagrees with a 2019 assignment; cancelled registrations keep frozen owners), which facts it supports (registered owner of a live mark; recorded sales of a name, with dates; not security interests, which name collateral agents), one source type (`uspto`, ADR 0003) or two, whether a serial or registration number becomes an identifier, and how marks are matched to brands when unrelated owners share a word mark. It fixes the licensee gap only with a precedence rule: the registered owner of a live mark outranks a brand list that never says who owns the name. Findings: chains [research/uspto-trademarks.md](../../chains-and-brands/research/uspto-trademarks.md).
- **From chains "Licensed names in v1"** (2026-11-18; "USPTO trademark data: adopt as a source?" amended): USPTO joins v1 narrowly, as one licensing check per brand in seven licensing-prone industries, a reported owner fact and a guard against false PE (an unlinked registered owner stops a list-fact chain from making the brand PE). Still here: USPTO for every brand, as an official filing, recorded sales of names, and showing licensees. A list-grounded owner fact is set aside in v1 only by licensing evidence (a licensor's or licensee's license statement, "used under license"). Accepted trade-off: some PE-owned product brands registered to an unlinked IP subsidiary read "owner type not confirmed".
- **From chains "Licensed names in v1"** (2026-11-18): v1 now stores licensees as `licensed_to` claims (brand → company; never a hop, never shown) and marks brand-owner claims with `basis` (`listing` or `license_grant`). Showing licensees on the brand page is still this ticket's question.

