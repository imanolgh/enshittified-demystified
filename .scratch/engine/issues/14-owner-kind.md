# Owner kind: storage, evidence and the fund–firm link

Type: grilling
Status: open
Blocked by: 07, 12  (Research: Form ADV and IRS exempt-org bulk data; What a business entity is)
Map: [engine](../map.md)

## Question

Where does an entity's owner kind live, how is it evidenced and ranked, who maps a quoted self-description onto the enum, and how are funds linked to their investment firm?

## Context

- ADR 0001:5,9,14 makes owner kind a sourced, ranked fact with a confidence (a category is verified only if the deciding owner kind is verified). The 7-predicate set (CLAUDE.md:30) can't express it; §4 has no column (evidence_layer_plan.md:88 is a comment only). Options: `entities.owner_kind` + an assertions table, or a new claim type (vocabulary decision).
- **Self-description → enum**: ADR 0001:9 / evidence_layer_plan.md:177 have the LLM extract the quote, but mapping "growth equity", "family office", "holding company" onto 9 kinds is classification. LLM emits enum + quote, or code applies a phrase table?
- **`pe_firm` definition vs ranks**: ADR 0001:10 defines it via Form ADV; ADR 0001:9 / evidence_layer_plan.md:177 let a rank-2/3 self-description set it.
- **Fund ↔ firm**: the chain walk stops at "pe_firm (fund or firm)" (ADR 0001:11) and the card "names the firm without adding a hop" (:13). Needs a relation outside the predicate set (`owned_by` would add a hop) and a rule on whether a fund inherits its firm's kind ("pe_firm" as a fund's kind is a misnomer).
- **Does a PE chain end at a fund or a firm?** GLOSSARY:7–8,15–16,19–20 count hops "to a private equity fund"; ADR 0001:11,13 keeps one row per (business, PE firm); research_flows.md:71 counts degree 2 to a firm.
- ADR 0003:13 says a source type joins only when a relationship takes evidence from it, yet `form_adv` and `irs_exempt_org` exist only for owner kind.
- **Field evidence** (added 2026-11-04): the category audit pilot found that `Any PE Funds` flags Trian, 3G, BDT and JAB as PE and misses L Catterton's main US adviser ([chains-and-brands/research/category-audit-pilot.md](../../chains-and-brands/research/category-audit-pilot.md) §5). It also raised whether a public company that a PE fund controls (Jersey Mike's) and a public company with a PE-fund 5%+ holder count as PE-owned and PE minority stake (§9).
- Form ADV and IRS exempt-org are in scope (map ruling 2026-10-26); facts from "Research: Form ADV and IRS exempt-org bulk data".
- **From "What a business entity is"** (2026-11-05, [ADR 0005](../../../docs/adr/0005-brands-companies-locations-separate.md)): owners now include a `family` entity (one person or a family owning in their own name; owner kind `family`). Trusts, ESOP trusts, nonprofits and government bodies are `company` rows carrying owner kind `trust`, `employee_owned`, `nonprofit` or `government`.
- **From "Claim producers and the claims door"** (2026-11-05; summary in evidence_layer_plan.md "Producers and the door"): Form ADV is an `etl` producer that emits identity records for advisers (CRD, SEC number, legal name, office address). If owner-kind evidence such as `Any PE Funds` is its own output rather than a claim, it rides in the same door call; its shape and storage are this ticket's.
- **From "Predicate semantics"** (2026-11-05; role table in evidence_layer_plan.md §4 `claims`): a fund is never the subject of `owned_by`, so the fund–firm link needs its own form here (an LP stake isn't a hop either). Owner-kind evidence is not a predicate. A brand's owner may now be a fund, firm or family directly (ADR 0005 amended).
- **From "Entity lifecycle"** (2026-11-06; notes in evidence_layer_plan.md §4 `entities`): code may change an entity's type from `company` to `investment_firm` or `fund` when a Form ADV identity record matches it (events row). A firm first created from a news quote as a company becomes an investment firm that way.
