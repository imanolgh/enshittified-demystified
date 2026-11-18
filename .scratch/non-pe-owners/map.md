# Map: Non-PE owners (parked)

Label: wayfinder:map · Tracker: local markdown (`docs/agents/issue-tracker.md`) · Charted 2026-11-16 from the developer's question about conglomerates, brand licensors and short-term owners

**Parked by ADR 0004 (amended 2026-11-16).** A post-launch add-on to chains and brands, not part of v1. Unparking it is a developer decision. Don't work this map's frontier, research tickets included, until then.

## Destination

`.scratch/non-pe-owners/spec.md`: a build spec for an add-on to chains and brands, built after v1 launches, that sets how the product tracks and shows three kinds of owner on brand pages: conglomerates (PepsiCo, Kraft Heinz, Nestlé), brand licensors (Authentic Brands Group, Marquee Brands, WHP Global) and short-term owners (an owner that buys a brand and holds no stake in it a few years later). It sits on top of the [engine](../engine/map.md) and [chains-and-brands](../chains-and-brands/map.md) specs. It must be complete enough that Claude can build it without asking a design question, with `docs/`, `GLOSSARY.md` and the ADRs consistent with it (scope ruled 2026-11-16).

## Notes

- The [engine map](../engine/map.md) Notes apply here too: authorship, skills, how to resolve, no application code. So do the [chains-and-brands map](../chains-and-brands/map.md) Notes on competitor sites.
- Raised by the developer on 2026-11-16: "do we have any mention for other company entities like conglomerates, im thinking things like pepsico, kraft, nestle, etc. or even brand management firms that license brands, or public companies that have short term interests and end up having no stake in the product 5 years out". Ruled the same day: a future add-on, not v1, with its own map.
- **v1 stays as specified** (ruled 2026-11-16). Nothing in chains and brands v1 changes for this map. v1 already keeps what the add-on needs: ended hops stay stored as ended edges (engine "Edge lifecycle: ending, retraction and staleness"), and documents are written once and never deleted (engine "Document storage, fetch log and last-confirmed"), so a later prompt version can re-read them.
- **What v1 already does with these owners** (read 2026-11-16):
  - **Conglomerates.** `conglomerate` is an owner kind with the category `conglomerate_owned` (ADR 0001). No official filing proves it, and the starting term table maps only the word "conglomerate" to it (engine "Owner kind: storage, evidence and the PE-firm test", round 2). A ticker from an SEC filing beats a self-description, so PepsiCo and Kraft Heinz read `public_company`. Nestlé files nothing with the SEC (it is absent from EDGAR's `company_tickers.json` on 2026-11-16, while PepsiCo, Kraft Heinz, Unilever and General Mills are present), so it reads public company only as `reported`, from its own "listed on" wording. The glossary lists the kind but never defines it. Among controlling co-owners with no stated stakes, public company ranks above conglomerate (engine "Category precedence and public companies").
  - **Brand licensors.** A brand's owner is whoever owns the name, never a licensee (GLOSSARY "Brand"). The extraction prompt claims the licensor and gives the licensee nothing (engine "Extraction prompt rules", Q2). Licensed-run brands read like any brand (chains "Brand and chain model", Q5), and licensed product lines are never brands (chains "Product categories: vocabulary and assignment", Q7). Licensing is not a predicate in v1 (engine "Predicate semantics", Q6). No owner kind fits a licensor.
  - **USPTO trademark data** (chains "USPTO trademark data: adopt as a source?", 2026-11-17): not adopted for v1; the question moved to "Brand licensors and licensees on the brand page".
  - **Short-term owners.** The card's history shows only "formerly PE-owned {years}" (engine "Brand card, receipt and edge shapes"), read from `entity_pe_owner_periods`, which holds PE periods only (engine "Category storage and recompute"). Above a public company, only a PE-kind firm's 13D, or a 13G not filed under Rule 13d-1(b), creates a minority stake (ADR 0001). Nothing measures how long an owner held a brand.
- **Product motivation:** `docs/painpoints.md:153-158` and `docs/marketgaps.md:12` call ownership-type nuance (PE vs conglomerate vs family) the moat. Reddit's recurring corrections (Gerber is Fiskars', Marmot is Newell's) are the evidence.
- **Research tickets:** findings go to `.scratch/non-pe-owners/research/<slug>.md`, every claim cited to a primary source. Same rules as chains "Research: Where PE owns consumer brands".

## Decisions so far

None yet.

## Not yet specified

- **Coverage and "checked":** if the add-on adds required sources (licensee filings, for example), whether a brand needs them before it reads "No PE evidence found", and what it shows while they are still running (engine "What 'checked' means and coverage states").
- **Re-reading stored documents:** a new prompt version that claims licensees, or descriptions of non-PE owners, would re-read documents already stored. Its cost, order and trigger.
- **Company pages** for conglomerates and licensors, such as a page listing every brand Authentic Brands owns. Waits on engine "Graph endpoint and non-brand output shapes".
- **Card wording and the how-this-works page** for whatever the tickets add, on top of chains "Card wording and the how-this-works page".

## Out of scope

- **Any change to chains and brands v1:** ruled 2026-11-16 while charting. v1 keeps the data the add-on needs (Notes).
- Everything the [engine map](../engine/map.md) rules out of scope, including paid secondary sources (PitchBook, Preqin, CB Insights).
