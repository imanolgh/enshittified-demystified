# USPTO trademark data: adopt as a source?

Type: grilling
Status: open
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
