# What "conglomerate" means

Type: grilling
Status: open
Blocked by: 83, 86  (What the product says about owners that aren't PE; Research: Conglomerates among brand owners)
Map: [non-pe-owners](../map.md)

## Question

What is a conglomerate in the glossary, does a listed conglomerate such as PepsiCo keep reading "public company" because its ticker wins, and what evidence sets the kind when no filing exists?

## Context

- Charted 2026-11-16. **Not worked until the developer unparks this map.**
- v1: `conglomerate` is one of the twelve owner kinds, with the category `conglomerate_owned` (ADR 0001; GLOSSARY "Owner kind"), but the glossary never defines it. It has no rank-1 source; the starting term table maps only the word "conglomerate" and lists "holding company" as unclear (engine "Owner kind: storage, evidence and the PE-firm test", round 2). A ticker from an SEC filing is rank 1 for `public_company`, so a public conglomerate reads public company (same ticket, Q4).
- Consequence in v1: the kind lands only on private groups that use the word about themselves (Hyundai Department Store Group behind Zinus). PepsiCo and Kraft Heinz read public company (verified); Nestlé reads public company only as reported, because it files nothing with the SEC.
- Among controlling co-owners with no stated stakes, the order is investment funds, public company, conglomerate, employee-owned, trust, family, cooperative, nonprofit, government (engine "Category precedence and public companies").
- Edge cases to settle: Berkshire Hathaway (public, owns Dairy Queen and unrelated businesses); Icahn Enterprises (public holding company holding 13D stakes, no Form ADV; its v1 count is decided in chains "Launch industries"); Houchens Industries (ESOP that owns businesses in several industries); a family-controlled public company (L'Oréal, Estée Lauder); a private group (Koch, Hyundai Department Store Group).
- The answer to "What the product says about owners that aren't PE" decides whether the kind matters to a verdict or only to how an owner is labeled.
- Facts: "Research: Conglomerates among brand owners".
