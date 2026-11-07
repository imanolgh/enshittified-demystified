# Form ADV and IRS exempt-org ingestion

Type: grilling
Status: open
Blocked by: 07, 14, 65  (Research: Form ADV and IRS exempt-org bulk data; Owner kind: storage, evidence and the PE-firm test; Funds and their investment firm)
Map: [engine](../map.md)

## Question

How are Form ADV and IRS exempt-org data ingested to set owner kinds (and fund→firm links) at rank 1?

## Context

- In scope by map ruling 2026-10-26 (without Form ADV no business can be verified PE-owned under ADR 0001:9–10,14).
- Neither has a roadmap step nor a deferred-list entry (build_roadmap.md:173); evidence_layer_plan.md:73,158 ("a fund triggers EDGAR/ADV connectors").
- Bulk format, private-fund-type field, adviser/fund identifiers, refresh cadence (from "Research: Form ADV and IRS exempt-org bulk data"); storage per "Owner kind…".
- Matching ADV advisers/funds and EO-BMF orgs to existing entities (resolution path).
- **From "Claim producers and the claims door"** (2026-11-05; summary in evidence_layer_plan.md "Producers and the door"): Form ADV is an `etl` producer. Each run checks the file header and reads columns by name before writing anything; one document per row; each claim quotes the whole data line; it emits identity records for advisers (and funds, from the archive); `producer_version` is a module constant.
- **From "Entity lifecycle"** (2026-11-06; notes in evidence_layer_plan.md §4 `entities`): a Form ADV identity record that matches an entity typed `company` changes it to `investment_firm` (adviser) or `fund` (private fund) by code, with an events row.
- **From "Owner kind: storage, evidence and the PE-firm test"** (2026-11-07; ADR 0001 amended; table in evidence_layer_plan.md §4 `owner_kind_evidence`): the Form ADV ETL emits rank-1 `owner_kind_evidence` rows for advisers with `Any PE Funds = Y` (quote = the whole data line); `N` emits nothing. The IRS exempt-org file emits rank-1 `nonprofit` rows matched by EIN. Rows ride in the same door call as the identity records.
- **From "Funds and their investment firm"** (2026-11-07; ADR 0001 amended; notes in evidence_layer_plan.md §4): (1) archive fund rows give fund identity records (name, `805-` id), a `managed_by` claim to the adviser, and rank-1 evidence from the fund's `Fund Type` (Private Equity → `private_equity`, Real Estate → `real_estate`, Venture Capital → `venture_capital`, hedge, securitized asset, liquidity → `other_investment_fund`, Other Private Fund → none). (2) For each firm in the graph, read its current IAPD Form ADV PDF for its fund list (names and `805-` numbers as text; type checkboxes not readable), typing funds and linking them; cadence is this ticket's. (3) Group a firm's adviser registrations into one `investment_firm` from Schedule D Section 7.A (related advisers); whether the bulk files carry it, and how current, is this ticket's; joint-venture advisers (FS/KKR Advisor) stay their own firm. (4) A firm's kind from the monthly counts by fund type: any PE fund → `private_equity`, all real estate or all VC → that kind, any other mix → `other_investment_fund`; `Y` on any registration counts. This ticket is no longer blocked by "Funds and their investment firm".
