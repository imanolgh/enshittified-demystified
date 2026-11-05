# Brand and chain model

Type: grilling
Status: open
Blocked by: engine/12, engine/15  (What a business entity is; Predicate semantics)
Map: [chains-and-brands](../map.md)

## Question

What are a brand and a chain in the product, whose ownership does a brand page report (the brand owner, the operator, the franchisee), and how do franchises and licensing show up?

## Context

- Pivot proposal (handoff §2): "A chain is a brand with locations. Brand-level verdicts first, with the franchise rule from `docs/decisions.md` §4." Not decided.
- **Franchise rule** (decisions.md §4, still in force per ADR 0004): ownership is modeled at two levels, brand ownership and location operator; a search returns both verdicts. pre-launch-seeding.md:59 repeats it for restaurants.
- **Licensing**: a brand licensed to an operator (clothing especially) can't be expressed by the closed predicate set; the predicate question is in engine "Predicate semantics". This ticket decides what the brand page says about it.
- **GLOSSARY**: "ownership chain" is defined from "a local business" (ADR 0004 consequence: this ticket owns widening it). "Chain" (a set of locations) and "ownership chain" (a path of ownership links) also collide as words.
- **Public companies** (Chipotle, Walmart, Target, Home Depot) don't flag; how they read is in "Card wording and the how-this-works page".
- Which entity rows exist (brand, company, location) is fixed in engine "What a business entity is"; this ticket is the product meaning.
- Load `grilling` and `domain-modeling`.
- **From engine "What a business entity is"** (2026-11-05, [ADR 0005](../../../docs/adr/0005-brands-companies-locations-separate.md)): there is no `chain` entity type. Brands, companies and locations are separate rows; a brand row exists only for a name that spans several locations or is sold as a product. Whether chains v1 creates location rows at all is this ticket's call.
