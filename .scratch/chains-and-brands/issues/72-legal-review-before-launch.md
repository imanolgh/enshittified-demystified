# Legal review before launch

Type: task
Status: open
Map: [chains-and-brands](../map.md)

## Question

Before the chains-and-brands site launches, what does a lawyer say about the legal questions below, and what changes do their answers require?

## Context

- Created 2026-11-08 from engine "Press and EDGAR full-text connectors" (Q6, developer ruling). HITL: the developer takes these questions to a lawyer; Claude records the answers and turns any required changes into tickets. It blocks launch, not the current tickets (gate recorded in engine "Testing and acceptance bars").
- Claude's notes in that ticket are not legal advice; case references there are from memory.

## Questions for the lawyer

1. **Stored copies.** The engine keeps full private copies of fetched pages, news articles and press releases included, so quotes can be checked word for word; the public site shows only short quotes, the source's name and a link ("Document storage, fetch log and last-confirmed"; "Brand card, receipt and edge shapes"). Is that defensible (fair use), and does it need limits for news articles?
2. **Wire services' terms.** PR Newswire's terms bar robots, data mining and "database storage and retrieval"; Business Wire's appear to as well. The plan reads their public RSS feeds only to learn that a release exists, then stores the release from the issuer's own site. Is reading the feeds a problem? Would a licensed feed be needed?
3. **Crawling.** The bot uses its own name, follows robots.txt for its name and `*`, does not follow rules that name only AI crawlers, never gets around blocks, and stops when asked. Is ignoring AI-crawler-only rules a meaningful risk, given that page text goes to an AI model for extraction?
4. **Takedowns.** Documents are never deleted (the evidence archive). What process is needed for a removal or correction request, and must stored copies ever be deleted?
5. **Defamation.** The site publishes ownership facts ("PE-owned", "sources disagree", "formerly PE-owned") with sourced quotes and confidence labels. What wording, disclaimers or correction process lowers exposure?
6. **Search results.** If a web search API is used to find a brand's past coverage ("Research: Web search APIs for finding a brand's past coverage"), most terms allow only transient storage of results. The engine would fetch each result's page itself and keep the page's URL as part of the stored document. Does keeping that URL count as storing search results under those terms?
7. **Structure.** Should the product sit in a company (an LLC or similar) rather than with the developer personally?
8. **The honest browser retry.** When a site answers with a bot challenge, the bot retries once in its own unmodified browser, still named as our bot, with no clicks, and uses the page only if the site's own check lets it through (added 2026-11-12 by engine "Rosters, portfolio pages and the registry"). Warburg Pincus challenges a plain request but serves the browser this way. Is that a meaningful risk under computer-access law or a site's terms?

## How to resolve

The developer records the lawyer's answers under `## Answer`; Claude opens tickets for any required changes.
