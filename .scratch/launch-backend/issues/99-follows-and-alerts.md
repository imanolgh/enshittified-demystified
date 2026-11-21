# Follows and alerts

Type: grilling
Status: open
Blocked by: engine/29, engine/119  (Events and the public changelog; Refresh schedule and next-check date)
Map: [launch-backend](../map.md)

## Question

What can a user follow (brands, companies, whole industries), which changes trigger an alert, how and when are alerts delivered, and what does an alert say?

## Context

- Charted 2026-11-18. **Not worked until the developer unparks this map.**
- **From the monetization review** (developer, 2026-11-21): an alert is only as fast as the refresh that notices the change, and engine "Cost cuts before revenue" runs no refresh on a timer before revenue. So this ticket waits on "Refresh schedule and next-check date", and shipping alerts ends the pre-revenue mode (engine "When revenue ends the pre-revenue mode").
- ADR 0004: paid alerts tell a user when a followed brand changes hands.
- Candidate triggers, all from the engine's stored changes: a new PE owner (category becomes PE-owned or PE minority stake), a PE exit ("formerly PE-owned"), a pending deal announced, called off or completed (GLOSSARY "Pending deal"), a category change of any kind, sources disagreeing, a hop going "last confirmed". Which events exist and their shapes are engine "Events and the public changelog", which this ticket waits on.
- Delivery: email first (no app in v1, ADR 0004); immediate or batched; quiet periods.
- Wording follows the card rules (no AI-written prose; computed labels and quotes; chains "Card wording").
- Retractions: a claim retracted after an alert went out (engine "Edge lifecycle"); whether a correction alert follows.
