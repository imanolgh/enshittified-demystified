# Billing: provider, taxes, refunds and downgrades

Type: grilling
Status: open
Blocked by: 96, 102  (Research: Billing and email providers; Prices and the founding-member offer)
Map: [launch-backend](../map.md)

## Question

Which billing provider runs subscriptions, who handles sales tax, what are the refund and cancellation rules, and what happens to a user's follows when they downgrade?

## Context

- Charted 2026-11-18. **Not worked until the developer unparks this map.**
- `monetizationideas.md` §3A: billing must be built and tested before the beta starts, so turning it on is a configuration change; on downgrade, extra follows are saved and paused, not deleted, and the user picks which stay active.
- Paid APIs log per-call cost from day one (CLAUDE.md).
- Facts: "Research: Billing and email providers". Legal questions (auto-renewal and cancellation rules) sit in the map's fog ("Legal before billing").
