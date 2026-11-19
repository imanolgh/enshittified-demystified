# Map: Launch backend (parked)

Label: wayfinder:map · Tracker: local markdown (`docs/agents/issue-tracker.md`) · Charted 2026-11-18 from the developer's question about tickets for monetization strategies

**Parked by ADR 0004 (amended 2026-11-18).** The account layer added after chains and brands v1 launches. v1 launches public and anonymous. Unparking this map is a developer decision. Don't work its frontier, research tickets included, until then.

## Destination

`.scratch/launch-backend/spec.md`: a build spec for the account layer on top of the [engine](../engine/map.md) and [chains-and-brands](../chains-and-brands/map.md) specs: accounts, follows and paid alerts when a followed brand changes hands, the free/paid line and prices, billing, the recurring digest and the founding-member beta. It must be complete enough that Claude can build it without asking a design question, with `docs/` (`monetizationideas.md` rewritten for chains, since it is canonical for prices), `GLOSSARY.md` and the ADRs consistent with it (scope ruled 2026-11-18).

## Notes

- The engine map Notes apply here too: authorship, skills, how to resolve, no application code.
- Raised by the developer on 2026-11-18 ("is there a ticket or tickets left for monetization strategies?"). Before this map, accounts, follows, paid alerts and billing were "a later map" on chains-and-brands and the "Launch backend" candidate on the engine map.
- **v1 launches without accounts** (ruled 2026-11-18; reaffirmed the same day in chains "The how-this-works page" after the developer briefly asked for paid alerts at launch: "we want to remove as much friction as possible from people using the site, and not having any sort of sign up or login is much better"): pages are public and anonymous ("Website pages and shareable cards"). Accounts, follows and paid alerts come after launch from this map, so the founding-member beta starts when this map's work ships, not at launch as `monetizationideas.md` §3A planned. Nothing in v1 changes.
- **Account model** (developer, 2026-11-18, chains "Source-link submissions"): reading never needs an account; a free account is needed only to comment (community notes); paid features in later builds run on the same accounts.
- **What's already decided:**
  - The money model (ADR 0004; decisions.md §14): search is free and never metered; paid alerts tell a user when a followed brand changes hands; product industries carry affiliate links.
  - Evidence is free (decisions.md §7; `monetizationideas.md` §1): brand cards, receipts, chains and alternatives are never paywalled or metered.
  - Affiliate links and alternatives ("Alternatives and affiliate links", 2026-11-17): a brand's own program or a retailer program, never for PE brands, no paid placement in v1.
- **What's stale in `monetizationideas.md`:** its alert prices ($19–29/yr insurance framing, Premium ~$8/mo or ~$79/yr, founding price ~$5/mo or $49/yr), its follows of local businesses, its metro digest, its retirement monitor and deep-dive (deferred with the retirement map), and its "priority on-demand research" perk (on-demand research removed, decisions.md §15). Its reasoning (event frequency, insurance framing, the gentle downgrade, no bait-and-switch) is the starting point for this map's tickets.
- **Research tickets:** findings go to `.scratch/launch-backend/research/<slug>.md`, from the providers' and products' own pages; same bot rules as the chains-and-brands research (robots.txt read before the first request to every host, refused requests stop the worker, budgets with a margin against the harness count).

## Decisions so far

None yet.

## Not yet specified

- **Research/Pro tier:** market-wide reports for journalists, lawyers and investors (BDC loan-book changes, rollup dossiers; `monetizationideas.md` §3). Waits for graph depth; reuses accounts and billing.
- **B2B data and API licensing:** the long-run revenue line `monetizationideas.md` names (journalists, academics, pension committees, litigation funders).
- **Legal before billing:** terms of service, a privacy policy, US auto-renewal and cancellation rules, email consent. Separate from chains "Legal review before launch".
- **Rewriting `monetizationideas.md`** for chains and brands once prices and the beta settle.

## Out of scope

- **The retirement brief and deep-dive:** the parked [retirement map](../retirement/map.md).
- **Certified Independent:** a post-launch badge granted only by automated checks of official records (ADR 0001, ADR 0002); its paid-badge contradiction is engine "Product-doc contradictions".
- **Affiliate links and alternatives:** settled in chains "Alternatives and affiliate links".
- **Any change to chains and brands v1:** ruled 2026-11-18.
- Everything the [engine map](../engine/map.md) rules out of scope.
