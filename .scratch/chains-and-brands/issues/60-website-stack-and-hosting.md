# Website stack and hosting

Type: grilling
Status: open
Map: [chains-and-brands](../map.md)

## Question

What is the website built with, how is it served (server-rendered or static pages over the API), and where is it hosted relative to the engine?

## Context

- ADR 0004: version 1 is a website; a native app comes later.
- CLAUDE.md's stack is backend-only (FastAPI and friends); no frontend stack is recorded. marketgaps.md:214 mentions "FastAPI (Python) + Vue" in passing. Adding a stack is the developer's decision.
- Distribution is the biggest gap (handoff §5): brand pages that can rank in search and shareable deal cards argue for server-rendered or pre-rendered HTML.
- Engine hosting is open in engine "Hosting, storage and deployment".
