# Owner kind: storage, evidence and the fund–firm link

Type: grilling
Status: open
Blocked by: 07, 12  (Research: Form ADV and IRS exempt-org bulk data; What a business entity is)
Map: [api-spec](../map.md)

## Question

Where does an entity's owner kind live, how is it evidenced and ranked, who maps a quoted self-description onto the enum, and how are funds linked to their investment firm?

## Context

- ADR 0001:5,9,14 makes owner kind a sourced, ranked fact with a confidence (a category is verified only if the deciding owner kind is verified). The 7-predicate set (CLAUDE.md:30) can't express it; §4 has no column (evidence_layer_plan.md:88 is a comment only). Options: `entities.owner_kind` + an assertions table, or a new claim type (vocabulary decision).
- **Self-description → enum**: ADR 0001:9 / evidence_layer_plan.md:177 have the LLM extract the quote, but mapping "growth equity", "family office", "holding company" onto 9 kinds is classification. LLM emits enum + quote, or code applies a phrase table?
- **`pe_firm` definition vs ranks**: ADR 0001:10 defines it via Form ADV; ADR 0001:9 / evidence_layer_plan.md:177 let a rank-2/3 self-description set it.
- **Fund ↔ firm**: the chain walk stops at "pe_firm (fund or firm)" (ADR 0001:11) and the card "names the firm without adding a hop" (:13). Needs a relation outside the predicate set (`owned_by` would add a hop) and a rule on whether a fund inherits its firm's kind ("pe_firm" as a fund's kind is a misnomer).
- **Does a PE chain end at a fund or a firm?** GLOSSARY:7–8,15–16,19–20 count hops "to a private equity fund"; ADR 0001:11,13 keeps one row per (business, PE firm); research_flows.md:71 counts degree 2 to a firm.
- ADR 0003:13 says a source type joins only when a relationship takes evidence from it, yet `form_adv` and `irs_exempt_org` exist only for owner kind.
- Form ADV and IRS exempt-org are in scope (map ruling 2026-10-26); facts from "Research: Form ADV and IRS exempt-org bulk data".
