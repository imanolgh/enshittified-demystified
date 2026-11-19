# Map: Community notes (parked)

Label: wayfinder:map · Tracker: local markdown (`docs/agents/issue-tracker.md`) · Charted 2026-11-18 from chains "Source-link submissions"

**Parked by ADR 0004 (amended 2026-11-18).** Reader discussion on brand pages, after the chains-and-brands v1 launch and after the launch backend's accounts exist. Unparking it is a developer decision. Don't work this map's frontier, research tickets included, until then.

## Destination

`.scratch/community-notes/spec.md`: a build spec for threaded, tagged discussion on brand pages by people with free accounts, links allowed and no uploads, on top of the [engine](../engine/map.md), [chains-and-brands](../chains-and-brands/map.md) and [launch backend](../launch-backend/map.md) specs. It must be complete enough that Claude can build it without asking a design question, with `docs/`, `GLOSSARY.md` and the ADRs consistent with it (scope ruled 2026-11-18).

## Notes

- The engine map Notes apply here too: authorship, skills, how to resolve, no application code.
- **Origin** (developer, 2026-11-18, while turning down reader link submissions in chains "Source-link submissions"): a "Community Notes" section where people dispute a piece of evidence, linking outside documents and tagging their comment ("Source Dispute", "Ownership Dispute"); also a place to discuss product quality, whether products degraded, where to find older versions from before a PE acquisition, and alternatives; Reddit-style threads (a quality thread, an ownership dispute thread, a source dispute thread, an alternatives thread); real people only, "no bots whatsoever"; no file uploads ("a real security concern"); affiliate links for alternatives commenters name.
- **Founding rule** (ruled 2026-11-18): notes are never evidence. Nothing in a note becomes a claim, a source or a receipt, and no note changes a verdict. A linked document reaches the data only through a normal operator batch, the same route as the chains "Report a mistake" form (decisions.md §15; ADR 0002). Notes sit visually apart from the brand card, under a line such as "Readers' notes. Not part of our ownership findings."
- **Account model** (developer, 2026-11-18): reading never needs an account; a free account is needed only to comment; paid features in later builds run on the same accounts (launch backend map).
- **Claude's cautions recorded while charting:** no method keeps out every bot (email plus an invisible check stops most; phone or ID checks get close to none but add friction); comment moderation collides with ADR 0002's "every publication decision automated"; reader comments about quality need a clear legal line beside the verdict; rewriting users' links with affiliate codes changes their words and falls under FTC disclosure, so show the site's own labeled link beside a comment instead; "Community Notes" is X's product name, so the name on the site is chosen in this map.
- **Research tickets:** findings go to `.scratch/community-notes/research/<slug>.md`, primary sources only; bot rules as in the chains-and-brands Notes; no OpenAI models.

## Decisions so far

None yet.

## Not yet specified

- **Notifications:** replies and mentions by email, and how often.
- **Reputation:** whether long-standing members earn standing (karma, badges).
- **Notes as a demand signal:** whether busy threads on brands outside the data feed the demand log (engine "Search and the demand log").
- **Deleting a commenter's account:** what happens to their notes; overlaps launch backend "Accounts: sign-in, stored data and deletion".

## Out of scope

- **Any change to chains and brands v1.**
- **File uploads:** ruled out in chains "Source-link submissions".
- **Notes as evidence:** this map's founding rule.
- **Paid features:** the [launch backend map](../launch-backend/map.md).
- Everything the [engine map](../engine/map.md) rules out of scope.
