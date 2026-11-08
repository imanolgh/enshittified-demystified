# Research: Web search APIs for finding a brand's past coverage

Type: research
Status: open
Map: [engine](../map.md)

## Question

Which web search APIs could the engine use to find pages about a brand's past ownership changes (press releases on issuers' sites, news articles, adviser pages), and what do their terms, prices, coverage and query features allow?

## Context

- Raised 2026-11-08 in "Press and EDGAR full-text connectors": Google News RSS is blocked (robots.txt for `*` and naming Anthropic's crawlers, Google's terms, a personal-use notice), GDELT is deferred, and wire feeds hold only their latest 20 items, so nothing finds a release from 2021 (Dental365's acquisition through The Resolute Fund V). The audit workers found such pages with web search.
- Results would be pointers only: the engine then fetches each page from its own site under the bot rules (own bot name, robots.txt path by path, never getting around a block) and stores it as a document. Search results themselves are never evidence.
- Recalled from memory, to confirm or correct: Microsoft retired the Bing Search APIs in 2025; Google's Programmable Search (Custom Search JSON API) and Brave's Search API exist with terms not checked.
- The decision (which route, if any) goes to "Retrieval fan-out, tracked entities and refresh cadence".

## Find out

For each candidate API (at least: Google Programmable Search / Custom Search JSON API, Brave Search API, the Bing APIs' status and any successor, and any other API that returns web results from its own index, such as Mojeek or Exa; note but don't recommend services that scrape another engine's results, such as SerpAPI, and say why):
- **Availability:** current status, any announced retirement or limits on new customers or on whole-web search.
- **Terms:** whether results may be stored, for how long, and whether automated, commercial or AI use is allowed; whether results may be used to decide which pages to fetch.
- **Price:** cost per 1,000 queries, free tiers, daily caps.
- **Query features:** exact-phrase quoting, site filters, date range filters, result count per query, and whether the index covers old pages (2015–2024).
- **Rough cost for launch:** about 374 brands, a few queries each (brand name plus "acquired", "acquisition", "private equity", "portfolio"), and a quarterly re-run.

## Rules

- Primary sources only: each vendor's own documentation, pricing and terms pages. No third-party comparison blogs as sources.
- Respect robots.txt; any user agent carries no contact detail (CLAUDE.md, memory). Don't sign up for accounts or call paid endpoints.
- Mark anything unconfirmed.

## How to resolve

AFK: a subagent invokes the `research` skill and writes `.scratch/engine/research/web-search-apis.md`, then appends `## Answer` here. No branches, commits or pushes.
