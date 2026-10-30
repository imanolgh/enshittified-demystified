# SoS and vet license board connectors

Type: grilling
Status: open
Blocked by: 11, 12, 47  (Research: SoS and vet license boards in the launch states; What a business entity is; Pick the second launch state)
Map: [api-spec](../map.md)

## Question

What do the launch-state SoS connector and vet license board connectors fetch, what does one document represent, and what do they yield (identity, aliases, claims)?

## Context

- SoS rarely states ownership: which record fields map to which claims or aliases? Mergers/name changes → `renamed_from`? Registered agent/officers as resolution signals only (no person entities).
- Vet boards: premises vs individual licenses decides whether a vet census is possible (from "Research: SoS and vet license boards in the launch states"); bulk vs scrape; refresh cadence (none given); identity only or claims?
- Both feed resolution tiebreakers and the ambiguous-retry trigger (ADR 0002:14).
