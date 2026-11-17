# What the product says about owners that aren't PE

Type: grilling
Status: open
Blocked by: none
Map: [non-pe-owners](../map.md)

## Question

What does the add-on do with conglomerates, brand licensors and short-term owners: keep the verdict PE-only and add facts that code computes, add new owner kinds or categories, or widen the verdict to judge ownership beyond PE? And which of those does "tracked categories" mean?

## Context

- Charted 2026-11-16. **Not worked until the developer unparks this map.**
- The developer's phrase was "add these additional corporate categories that are tracked". The glossary has two words for this: an **owner kind** (what sort of owner: conglomerate, public company, family) and a **category** (the verdict a brand gets: PE-owned, conglomerate-owned, no PE evidence found). "Industry" is the line of business, and "category" never appears on the site (chains "Product categories: vocabulary and assignment"). This ticket settles which one the add-on changes, and the glossary follows.
- Options put to the developer while charting (not decided):
  - (a) **Describe, don't judge.** The verdict stays PE-only. These owners are named correctly as owners, and nothing new is added.
  - (b) **Facts that code computes, verdict stays PE-only.** The card gains lines code works out from evidence: every past owner with years, "the name's owner licenses it out; another company makes the product", how many times the brand changed owners in N years.
  - (c) **Widen the verdict.** The headline judges harmful ownership in general. Takes a new ADR superseding parts of ADR 0001 and ADR 0004, and changes every card.
  - Claude recommended (b): the risk is a Nestlé-flipped or licensing-shell brand reading "No PE evidence found" and readers taking it as a clean result, and (b) answers that with facts a quote can prove, without a judgment no quote can back.
- Invariants any answer must keep: categories are computed by code from owner kinds and chains, never by the LLM (ADR 0001); no manual review (ADR 0002); `no_evidence_found` is a first-class outcome; the product never calls anything independent outside the future Certified Independent badge (GLOSSARY).
- What v1 does today with these owners: the map's Notes.
- Two counting questions in chains "Launch industries" touch this and are decided there for v1: owners whose Form ADV says no PE funds (Atairos, Meritage), and a public holding company holding a 13D stake (Icahn Enterprises at Monro, about 17%, no Form ADV) ([industry-screen findings](../../chains-and-brands/research/industry-screen.md) counting questions 1 and 2).

## Hands on

- "What 'conglomerate' means", "Brand licensors and licensees on the brand page", "Past owners on the brand card" and "Short-term owners: what counts and what the card shows" all wait on this answer.
