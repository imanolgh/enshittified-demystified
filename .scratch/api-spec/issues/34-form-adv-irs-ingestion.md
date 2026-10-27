# Form ADV and IRS exempt-org ingestion

Type: grilling
Status: open
Blocked by: 07, 14  (Research: Form ADV and IRS exempt-org bulk data; Owner kind: storage, evidence and the fund–firm link)
Map: [api-spec](../map.md)

## Question

How are Form ADV and IRS exempt-org data ingested to set owner kinds (and fund→firm links) at rank 1?

## Context

- In scope by map ruling 2026-10-26 (without Form ADV no business can be verified PE-owned under ADR 0001:9–10,14).
- Neither has a roadmap step nor a deferred-list entry (build_roadmap.md:173); evidence_layer_plan.md:73,158 ("a fund triggers EDGAR/ADV connectors").
- Bulk format, private-fund-type field, adviser/fund identifiers, refresh cadence (from "Research: Form ADV and IRS exempt-org bulk data"); storage per "Owner kind…".
- Matching ADV advisers/funds and EO-BMF orgs to existing entities (resolution path).
