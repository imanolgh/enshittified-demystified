# Short-term owners: what counts and what the card shows

Type: grilling
Status: open
Blocked by: 83, 85, 89  (What the product says about owners that aren't PE; Research: How often consumer brands change owners; Past owners on the brand card)
Map: [non-pe-owners](../map.md)

## Question

What counts as a short-term owner, what threshold makes it one, and what does the brand card say about it?

## Context

- Charted 2026-11-16. **Not worked until the developer unparks this map.**
- The developer's words: "public companies that have short term interests and end up having no stake in the product 5 years out".
- Meanings put to the developer while charting (not decided):
  - (i) A company that buys a brand and resells it within a few years (Nestlé and Nature's Bounty; Newell's divestitures).
  - (ii) Activist or hedge-fund holders of a public parent's shares who push for cuts and then sell (Trian at Wendy's, Elliott at PepsiCo).
  - (iii) Quarterly pressure from public shareholders in general.
  - Claude recommended (i) and (ii), which leave a paper trail (deal releases, 13D filings), over (iii), which applies to every listed company and no document proves.
- v1 rules this touches:
  - Above a public company, only a PE-kind firm's 13D, or a 13G not filed under Rule 13d-1(b), creates a minority stake; a 13D or 13G amendment reporting 5% or less ends the hop (ADR 0001). An activist that reports PE funds on Form ADV (Trian) already counts as PE; one that doesn't is an other investment fund and changes nothing.
  - Hop endings and the 18-month staleness window are about evidence, not hold length (engine "Edge lifecycle: ending, retraction and staleness").
- Any threshold ("resold within N years", "N owner changes in M years") is computed by code from dated hops, so it needs start and end dates the sources give; how often those exist comes from "Research: How often consumer brands change owners".
- Builds on the periods stored by "Past owners on the brand card".
