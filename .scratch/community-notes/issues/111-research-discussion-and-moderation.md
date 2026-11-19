# Research: How comparable sites run discussion and moderation

Type: research
Status: open
Blocked by: none
Map: [community-notes](../map.md)

## Question

How do comparable sites structure threaded, tagged discussion and moderate it, and which automated moderation tools could a one-person site use?

## Context

- Charted 2026-11-18. **Not run until the developer unparks this map.**
- The developer's idea: Reddit-style threads on each brand page, tagged (ownership dispute, source dispute, quality, older versions, alternatives), real people only, links but no uploads.
- ADR 0002 (no manual review; every publication decision automated) is the constraint "Moderation and ADR 0002" weighs.

## Find out

1. **Structures:** Reddit, Hacker News, Discourse, Stack Exchange and X's Community Notes: threads and nesting, tags or flair, voting and sorting, editing and deleting, pseudonyms; how X's notes rate helpfulness across raters who usually disagree.
2. **Moderation:** each site's published rules and tools: reporting, automatic filters, rate limits, new-account limits, removal, appeals, bans; what is automated and what humans do.
3. **Automated tools:** spam and abuse classifiers and services usable by a small site (cost, privacy, accuracy claims from their own docs). No OpenAI models (developer rule).
4. Each fact from the sites' own documentation or published policies.

## Rules

- Primary sources only; bot rules as in the map Notes; never fetch Reddit pages themselves (project rule), using Reddit's own published help and policy pages only where robots.txt allows.
- Findings go to `.scratch/community-notes/research/discussion-and-moderation.md`.
