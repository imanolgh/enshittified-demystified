# Source-link submissions

Type: grilling
Status: resolved
Blocked by: engine/17  (Claim producers and the claims door)
Map: [chains-and-brands](../map.md)

## Question

Can a user submit a URL as evidence, which then goes through normal retrieval, extraction and citation checks with no manual review, and if so with what limits?

## Context

- Pivot proposal (handoff §5), **not decided**. It relaxes the ruling that community submissions are not in the MVP (decisions.md:79; stack_fastapi.md:68; build_roadmap.md:173).
- ADR 0002 (no manual review) still holds: a submission could only trigger retrieval of a public document, never assert a fact itself.
- Open: which domains are allowed (public primary sources only, CLAUDE.md), whether a submitted URL counts toward source independence, abuse and cost limits (each one costs extraction money), and what the submitter sees.
- **From "Claim producers and the claims door"** (2026-11-05; summary in evidence_layer_plan.md "Producers and the door"): there is no HTTP door for claims. A submission is a URL to fetch; the fetched page becomes a stored document and goes through a producer like any other.
- **From "What would change this"** (2026-11-18): if submissions are allowed, the card's "What would change this" section ends with "Know a source we haven't read? Send the link." That placement is only used if this ticket says yes.

## Comments

### Round 1 (2026-11-18)

- **First proposal, turned down:** links for brands already in the data, read automatically in a weekly batch under caps. The developer: "i don't want people adding their own documents", proposing instead a "Community Notes" section: Reddit-style threads on brand pages by real people only, tagged (source dispute, ownership dispute, quality, older versions, alternatives), links allowed, no file uploads ("a real security concern"), strict bot protection, and affiliate codes added to alternatives that commenters name. Claude's view: real people only needs accounts; comment moderation collides with ADR 0002 (every publication decision automated); reader comments on quality need a legal line beside the verdict; rewriting users' links with affiliate codes changes their words and falls under FTC disclosure, so show the site's own labeled link beside a comment instead.
- **Account model** (developer): reading never needs an account; a free account is needed only to comment; paid features in later builds run on the same accounts.
- **No reader submissions** (Q1): readers don't add documents; the "Send the link" line from "What would change this" is never used.
- **"Report a mistake"** (Q2): every brand page has a private form: a dispute type (source, ownership, other), a text box and up to 3 links; no uploads, no account; an invisible bot check (a hidden field plus rate limits). Reports go to the operator report, never onto the page. A report never edits a verdict: a linked public document reaches the page only through a normal operator batch (decisions.md §15), so facts stay automated (ADR 0002). "What would change this" ends with "Think this is wrong? Tell us." linking to the form.
- **Community notes** (Q3, Q4 option a): after launch, as its own parked map, charted in a separate session; it waits on the launch backend's "Accounts: sign-in, stored data and deletion". Reason for after launch: v1 is already large, moderation against ADR 0002 is unsolved, and empty threads on day one make a site look abandoned.

## Answer

Resolved 2026-11-18 in a grilling session (one round, recorded under Comments).

- **No reader submissions of links or files** in v1.
- **A private "Report a mistake" form** on every brand page (dispute type, text, up to 3 links, no uploads, no account, invisible bot check), feeding the operator report; it never changes a verdict by itself.
- **Account model:** reading never needs an account; free accounts only to comment; paid features later on the same accounts.
- **Community notes** after launch, in a new parked map, charted separately.
- Docs: none changed; no ADR or glossary change. decisions.md's "community submissions are not in the MVP" still holds.

Handed on:
- A new parked "Community notes" map (to chart): threads and tags, identity and bot protection, moderation against ADR 0002, the legal line between evidence and readers' views, labeled affiliate links beside comments.
- launch backend "Accounts: sign-in, stored data and deletion": accounts are free and serve commenting first; paid features later.
- "What would change this" (amended): "Think this is wrong? Tell us." replaces "Send the link".
- "Task: Draft the how-this-works page": section 10 describes the report form.
- engine "API conventions, internal auth and operator surface": reports in the operator report.
- engine "Operational identity, budgets and guardrail values": the form's rate limits.
- "Legal review before launch": what the form stores (free text can contain personal details) and how long it is kept.

### Amended 2026-11-21 (from "Cost cuts before revenue")

- Mechanism only: before revenue the "Report a mistake" form posts to a small free Cloudflare function instead of FastAPI ("Website stack and hosting", amended). Its fields, limits, rate limits, hidden-field bot check and the rule that a report never edits a verdict are unchanged.
