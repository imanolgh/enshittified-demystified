# Launch-state run budget and the NYC-area counties

Type: grilling
Status: open
Blocked by: engine/42  (Operational identity, budgets and guardrail values)
Map: [local-businesses](../map.md)

## Question

What is the spend cap for one launch-state deep batch, and which New York counties make up the NYC area that runs first?

## Context

Split out of engine "Operational identity, budgets and guardrail values" on 2026-11-04 (ADR 0004). The engine ticket keeps the cap mechanism; this ticket sets the local values.

- A per-batch spend cap for launch-state deep batches was ruled necessary in "Launch states and metros": a full NY run could be ~$1k of extraction, a rough estimate.
- The NY counties that make up the NYC area, which run first (ruled 2026-10-31 in "Launch states and metros", point 7; pre-launch-seeding.md "New York run order"). No NJ, CT or PA coverage.
