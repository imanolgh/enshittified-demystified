# What would change this

Type: grilling
Status: resolved
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

## Comments

### Round 1 (2026-11-18)

- **Placement and making** (Q1): a "What would change this" section right after the verdict and the pending deal on every brand card, "Not yet checked" included; one to three lines filled in by code from fixed templates with the brand's own names, firms, stakes and dates; no AI-written text; templates live in code with tests, and their wording is a product decision for the developer.
- **Templates** (Q2), all that apply, in this order:
  - PE-owned, verified: "A document showing {firm} sold its stake, or a source saying it no longer owns {brand}, would change this."
  - PE-owned or PE minority, reported: "This rests on 1 source. A second independent source or an official filing would verify it. A source saying otherwise would show that sources disagree."
  - PE minority stake: "{firm} holds {x}%. A stake over 50% would make this PE-owned. A filing showing 5% or less would end it."
  - Public company, no PE: "A Schedule 13D from a private equity firm, or a private equity firm gaining more than half the votes, would change this."
  - Family, cooperative or another non-PE owner: "A document showing a private equity firm bought all or part of {owner} or {brand} would change this."
  - Owner type not confirmed: "A filing, or {owner}'s own description saying what kind of owner it is, would settle this."
  - USPTO guard: "A source linking {registered owner} to {listing company} would settle this."
  - No PE evidence found: "A document naming a private equity owner would change this."
  - Sources disagree: "A filing, or a statement from {party} saying who holds the majority, would settle this."
  - Pending deal: "When the deal closes, this becomes {category}. If it's called off, or hasn't closed by {date}, it drops off."
  - No source since a date: "A current source showing {owner} still owns {brand} would restore it."
  - Not yet checked: "The check finishes when {n} more sources finish: {names}."
  - No line guesses ("may be sold soon") or comments on quality.
- **Next check** (Q3): "Next check due {Mon YYYY}" shows once engine "Retrieval fan-out, tracked entities and refresh cadence" sets the cadence; left off until then.
- **Send a source** (Q4): if "Source-link submissions" allows submissions, the section ends with "Know a source we haven't read? Send the link."; decided there.

## Answer

Resolved 2026-11-18 in a grilling session (one round, recorded under Comments).

- A "What would change this" section after the verdict and pending deal on every brand card: one to three code-generated lines from the twelve fixed templates above, in that order, using the brand's own names, firms, stakes and dates; never a guess or a quality comment; templates in code with tests, wording changes decided by the developer.
- "Next check due {Mon YYYY}" once a refresh cadence exists.
- A "Send the link" invitation only if "Source-link submissions" allows submissions.
- Docs: none changed; no glossary or ADR change.

Handed on:
- "Website pages and shareable cards": the section's place on the card (after the verdict and pending deal).
- engine "Retrieval fan-out, tracked entities and refresh cadence": the card needs each brand's next scheduled check date.
- "Source-link submissions": the "Send the link" placement.
- engine "Brand card, receipt and edge shapes" (amended): the card shape gains the generated lines.
- "The how-this-works page": may explain that these lines are generated from fixed rules.

### Amended 2026-11-18 (from "Source-link submissions")

- Readers can't submit links in v1, so the "Send the link" line is never used. The section ends instead with "Think this is wrong? Tell us.", linking to the private "Report a mistake" form.
