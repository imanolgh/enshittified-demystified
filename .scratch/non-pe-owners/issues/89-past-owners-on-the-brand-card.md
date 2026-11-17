# Past owners on the brand card

Type: grilling
Status: open
Blocked by: 83  (What the product says about owners that aren't PE)
Map: [non-pe-owners](../map.md)

## Question

Does the brand card list every past owner with the years it held the brand, or only past PE owners as v1 does, and where are non-PE ownership periods stored?

## Context

- Charted 2026-11-16. **Not worked until the developer unparks this map.**
- v1: the card's history section is "formerly PE-owned {years}" only (engine "Brand card, receipt and edge shapes"). It reads `entity_pe_owner_periods`, one row per brand, PE owner and period, whose ended rows are the history (engine "Category storage and recompute"). A non-PE owner's ended hop stays stored as an ended edge (engine "Edge lifecycle: ending, retraction and staleness") but nothing shows it.
- The example: Nature's Bounty. Nestlé bought it in 2021 and agreed on 2026-09-01 to sell it to Yellow Wood Partners. After closing, the v1 card shows the PE years and Yellow Wood, and Nestlé's years disappear.
- Questions inside this one: how far back history goes; whether an owner whose hop only went unconfirmed (18 months with no confirming source, ADR 0001) appears; how a spin-off reads; whether a derived table of all owner periods replaces or sits beside `entity_pe_owner_periods`; whether the public changelog changes (engine "Events and the public changelog").
- The answer to "What the product says about owners that aren't PE" decides whether history beyond PE is a fact the card shows at all.
- "Short-term owners: what counts and what the card shows" builds on whatever this ticket stores.
