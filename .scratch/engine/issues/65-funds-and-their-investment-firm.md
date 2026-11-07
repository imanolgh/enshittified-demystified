# Funds and their investment firm

Type: grilling
Status: open
Blocked by: 14  (Owner kind: storage, evidence and the PE-firm test)
Map: [engine](../map.md)

## Question

How is a fund linked to the investment firm that runs it without adding an ownership hop, does a PE ownership chain end at the fund or at the firm (and so which one the separation degree counts to), and does a fund take its firm's owner kind?

## Context

- Split from "Owner kind: storage, evidence and the PE-firm test" on 2026-11-06 (developer ruling, to keep each ticket to one session).
- **Fund ↔ firm**: the chain walk stops at "pe_firm (fund or firm)" (ADR 0001:11) and the card "names the firm without adding a hop" (:13). Needs a relation outside the predicate set (`owned_by` would add a hop) and a rule on whether a fund inherits its firm's kind ("pe_firm" as a fund's kind is a misnomer).
- **Does a PE chain end at a fund or a firm?** GLOSSARY:7–8,15–16,19–20 count hops "to a private equity fund"; ADR 0001:11,13 keeps one row per (business, PE firm); research_flows.md:71 counts degree 2 to a firm.
- **From "Predicate semantics"** (2026-11-05; role table in evidence_layer_plan.md §4 `claims`): a fund is never the subject of `owned_by`, so the fund–firm link needs its own form here (an LP stake isn't a hop either). Owner-kind evidence is not a predicate. A brand's owner may now be a fund, firm or family directly (ADR 0005 amended).
- **From "Entity lifecycle"** (2026-11-06): code may change an entity's type from `company` to `fund` or `investment_firm` when a Form ADV identity record matches it, with an events row.
- **Facts** from "Research: Form ADV and IRS exempt-org bulk data": fund-level rows (fund name, `805-` private fund id, `Fund Type` = "Private Equity Fund", and the fund-to-adviser link) are only in the historical archive through 2024; funds reported after 2025 appear only in per-adviser IAPD PDFs. Quotes often name the firm, not the fund ("Roark Capital acquired Subway").
- A brand's owner may be a fund, firm or family named directly (ADR 0005 amended by "Predicate semantics").
- **From "Owner kind: storage, evidence and the PE-firm test"** (2026-11-07; ADR 0001 amended; table in evidence_layer_plan.md §4 `owner_kind_evidence`): owner kind lives in `owner_kind_evidence` rows and is computed onto `entities.owner_kind`. Form ADV `Any PE Funds = Y` sits on the adviser (the firm); whether a fund takes its firm's kind, and what a fund described as "a private equity fund" means, are this ticket's. A BDC is `other_investment_fund` from its `814-` number.
