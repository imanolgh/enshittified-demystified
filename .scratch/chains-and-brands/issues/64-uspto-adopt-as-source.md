# USPTO trademark data: adopt as a source?

Type: grilling
Status: resolved
Map: [chains-and-brands](../map.md)

## Question

Does the engine adopt USPTO trademark data as a source, and if so: as which source type or types (ADR 0003), does it self-verify as an official filing, which facts may it support (brand → owning company only, or more), and does a mark's serial or registration number become an `entity_identifiers` scheme?

## Context

- Raised 2026-11-05 while resolving engine "What a business entity is": no ticket owned the three questions "Research: USPTO trademark data as an official source" left open (adoption, self-verification, source-type count).
- Findings ([research/uspto-trademarks.md](../research/uspto-trademarks.md)): one "last recorded owner" per mark, updated only by six recorded document types and without validity checks; changes in a separate Assignment database (one record per document; security interests recorded, owner unchanged); in 8 spot checks the registered owner never named the PE sponsor (sponsor-owned brands sat in "IP Holder" or franchisor subsidiaries; stock acquisitions left no record); Jersey Mike's owner field disagrees with a 2019 assignment; bulk files and APIs need a USPTO.gov sign-in or keys (ID.me for the bulk API).
- ADR 0005: a brand owns nothing and a company owns it, so a mark's owner could evidence a brand → company link.
- ADR 0003:13: a value joins `SourceType` only when a relationship takes evidence from it.
- "Category brand lists and brand-level checked" lists "USPTO if adopted" among the sources a check runs; it waits on this ticket.
- Load `grilling` and `domain-modeling`.

## Comments

### Round 1 (2026-11-17)

- **Adoption** (Q1, option c): not in v1. Facts weighed (from "Research: USPTO trademark data as an official source"): the registered owner named the PE sponsor in 0 of 8 spot checks, and in 5 of 8 it was a brand-level IP subsidiary (for Subway, Arby's and Crunch no other primary source links it upward); stock acquisitions leave no record; recording is ministerial, Jersey Mike's owner field disagrees with a 2019 assignment, and cancelled registrations keep frozen owners; access needs a USPTO.gov account, an ID.me check for the bulk API, or a TSDR key; recorded sales of a name do carry seller, buyer and date. USPTO's main value is licensing, and it fixes the licensee gap only with a precedence rule (the registered owner of a live mark outranks a brand list that never says who owns the name), which belongs to the licensing design. Options turned down: a narrow v1 lookup for licensing-heavy industries, a broad lookup as a required source for every brand, and never.

## Answer

Resolved 2026-11-17 in a grilling session (one round, recorded under Comments).

- **USPTO is not a v1 source.** No `SourceType` value, no official-filing status, no identifier scheme, and no place on any brand's required list for "checked".
- **The question moves** to the parked non-PE owners map, "Brand licensors and licensees on the brand page", with every sub-question this ticket held (self-verification, facts supported, source-type count, identifier, access, matching marks to brands) and the precedence rule USPTO would need.
- **v1's licensee gap stays open** for "Category brand lists and checked" or a change to engine "Extraction prompt rules", without USPTO.
- Docs: `evidence_layer_plan.md` §4 `entity_identifiers` note updated (no trademark serial in v1). No ADR, no glossary change.

Handed on:
- non-PE owners "Brand licensors and licensees on the brand page": the USPTO question in full.
- "Category brand lists and checked": no USPTO on the required list; the v1 licensee gap. This was its last open blocker.

### Amended 2026-11-18 (from "Licensed names in v1", round 1)

- **USPTO joins v1, narrowly.** One licensing check per brand in the seven licensing-prone launch industries (cookware, clothing and shoes, beauty products, personal care, home furnishings, sporting goods and outdoor gear, pet food and supplies; about 210 brands): the live registration for the brand's name in that industry's goods classes, nothing recorded when several live registrants match. The registered owner is a **reported** owner fact (not an official filing: recording is ministerial). One source type, `uspto` (ADR 0003). No identifier scheme; the serial number is in the document's address.
- **Its use is a guard against false PE, never an override:** when a brand's only chain to private equity starts with a list fact and USPTO names a different, unlinked company as the name's owner, that chain cannot make the brand PE-owned or PE minority stake; the brand reads "owner type not confirmed" until a source links the two.
- **Accepted trade-off (developer, 2026-11-18):** some PE-owned product brands whose name is registered to an unlinked IP-holding subsidiary may read "owner type not confirmed" instead of "PE-owned" until a source links the two companies. A false "PE-owned" is the worse error, so the guard errs toward "not confirmed".
- **Why reopened:** the licensee gap ("Licensed names in v1") has a name-owner document for only about half of licensed names (2 of 5 in cookware), and USPTO names the registered owner of nearly every live mark.
- **Still with the parked non-PE owners map:** USPTO for every brand, USPTO as a self-verifying official filing, recorded sales of names with dates, and showing licensees.
- Access (a TSDR API key; how to search by mark name; whether ID.me is needed) goes to a task ticket for the developer.
