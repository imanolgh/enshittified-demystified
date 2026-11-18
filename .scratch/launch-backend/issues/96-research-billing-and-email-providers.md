# Research: Billing and email providers

Type: research
Status: open
Blocked by: none
Map: [launch-backend](../map.md)

## Question

Which subscription billing services and transactional email services fit a small US consumer subscription run by one developer, and what does each cost, handle (sales tax, refunds, cancellation, deliverability) and require?

## Context

- Charted 2026-11-18. **Not run until the developer unparks this map.**
- Stack (CLAUDE.md): Python 3.12, FastAPI, PostgreSQL, Celery; httpx for outside APIs. Paid APIs log per-call cost from day one.
- The paid product is alerts when a followed brand changes hands plus a recurring digest (ADR 0004; `monetizationideas.md` §3), monthly and yearly plans, a founding-member price, and a beta with no billing that switches on by configuration (`monetizationideas.md` §3A).

## Find out

1. **Billing:** Stripe Billing, and merchants of record that collect and remit sales tax (Paddle, Lemon Squeezy, Polar and similar): fees, who is the seller of record, US state sales tax handling, refunds and chargebacks, cancellation flows, trials and locked prices for early subscribers, a hosted customer portal, Python libraries or plain HTTP APIs, and payout terms.
2. **Email:** Postmark, Amazon SES, Resend and similar: price per thousand, deliverability features (SPF, DKIM, DMARC, suppression lists, bounce and complaint webhooks), separation of transactional and digest mail, and terms on bulk or newsletter-style sending.
3. **Sign-in by email link** if any provider bundles it, and what that costs.
4. Each fact from the provider's own pages or documentation.

## Rules

- Primary sources only (provider pricing pages, documentation, terms). Bot rules as in the map Notes.
- Findings go to `.scratch/launch-backend/research/billing-and-email.md`.

## Hands on

- "Billing: provider, taxes, refunds and downgrades"; "Accounts: sign-in, stored data and deletion".
