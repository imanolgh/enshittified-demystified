# What would change this

Type: grilling
Status: open
Blocked by: none
Map: [chains-and-brands](../map.md)

## Question

What does the "what would change this" line say on each brand card, and by what rules does code generate it from the brand's evidence?

## Context

- Split off "Card wording" on 2026-11-18 (round 1 Q0).
- From the Worse on Purpose review (pivot handoff §5), a proposal: code generates "what would change this" on every card, so a disputed verdict points at the evidence that would flip it instead of an argument.
- Voice rules ("Card wording", round 1 Q1): no AI-written prose; computed text only; plain words; never "independent", "not PE-owned" or "PE-backed".
- Inputs code has: the category and its deciding chain, each hop's confidence ("Verified by {n} independent sources", "Reported by 1 source"), unconfirmed hops, pending deals, owners of unconfirmed kind, the USPTO guard, the checked date and the required source list ("Brand-level checked: required sources and freshness").
- Examples to settle: a reported PE-owned brand ("A second independent source or an official filing would verify this"), "Owner type not confirmed" ("A filing or statement saying what kind of owner {company} is would settle its category"), "No PE evidence found" ("A document naming a private equity owner would change this; we re-check on a schedule"), a pending deal, the USPTO guard ("A source linking {company} to {company}").
- **From "Card wording"** (2026-11-18): confidence reads "Verified by {n} independent sources", "Verified by an official filing ({type})" or "Reported by 1 source"; verdicts carry the deciding owner's name; every checked card has a "What we checked" section the generated line can point to.

