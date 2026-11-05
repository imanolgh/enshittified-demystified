# Form ADV and IRS exempt-org ingestion

Type: grilling
Status: open
Blocked by: 07, 14  (Research: Form ADV and IRS exempt-org bulk data; Owner kind: storage, evidence and the fund–firm link)
Map: [engine](../map.md)

## Question

How are Form ADV and IRS exempt-org data ingested to set owner kinds (and fund→firm links) at rank 1?

## Context

- In scope by map ruling 2026-10-26 (without Form ADV no business can be verified PE-owned under ADR 0001:9–10,14).
- Neither has a roadmap step nor a deferred-list entry (build_roadmap.md:173); evidence_layer_plan.md:73,158 ("a fund triggers EDGAR/ADV connectors").
- Bulk format, private-fund-type field, adviser/fund identifiers, refresh cadence (from "Research: Form ADV and IRS exempt-org bulk data"); storage per "Owner kind…".
- Matching ADV advisers/funds and EO-BMF orgs to existing entities (resolution path).
- **From "Claim producers and the claims door"** (2026-11-05; summary in evidence_layer_plan.md "Producers and the door"): Form ADV is an `etl` producer. Each run checks the file header and reads columns by name before writing anything; one document per row; each claim quotes the whole data line; it emits identity records for advisers (and funds, from the archive); `producer_version` is a module constant.
