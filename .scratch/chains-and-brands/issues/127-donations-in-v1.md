# Donations in v1

Type: grilling
Status: open
Blocked by: none
Map: [chains-and-brands](../map.md)

## Question

Does version 1 accept donations, and if so through which service, with what rules about who may give, what donors get (if anything), and where the site mentions it?

## Context

- Opened 2026-11-21 when the developer reviewed the monetization tickets (developer: "yes" to opening it). No doc has considered donations or tips.
- **Why ask:** v1's only revenue is affiliate links ("Alternatives and affiliate links"), and in-store industries (restaurants, gyms, dental, vet, car washes and others) earn nothing. A donation link needs no account, so it fits "v1 launches public and anonymous" (ADR 0004 "Launch backend parked"; developer: no sign-up or login in v1). The Worse on Purpose thread showed an audience that thanks a free tool and asks for more (`painpoints.md`; pivot proposal's Worse on Purpose review).
- **Rules already in force:**
  - Evidence is free (decisions.md §7; `monetizationideas.md` §1): nothing on a brand card, receipt, chain or alternatives block may depend on giving.
  - The how-this-works page's "Who runs it" draft ("The how-this-works page" Q6): self-funded, "It earns money from affiliate links. It has no investors, and it never takes money from private equity firms or from PE-owned brands." Donations would change that text, and the "never takes money from PE" promise has to hold for donations too.
  - No manual review anywhere (ADR 0002): any donor rule has to be one the service or code enforces, or one the site states without checking.
- **Questions to weigh:** whether to accept donations at all in v1; one-off, recurring, or both; which service (its fees, payout, what donor data it shares, whether it needs the developer's name or address shown publicly); whether donors get anything (a thank-you only, since evidence and alternatives stay free); how to handle a gift from a PE firm or PE-owned brand (refuse, refund, or state the limit and trust it); where the link sits (how-this-works page, footer, never on a card's verdict); wording that avoids "tax-deductible" (the site is not a nonprofit); and whether donations count toward engine "When revenue ends the pre-revenue mode".
- Hands on to: "Task: Draft the how-this-works page" (section 11 text), "Legal review before launch" (donation wording, consumer-protection rules for recurring gifts, taxes on gifts to a person), "Website pages and shareable cards" (where the link sits), engine "When revenue ends the pre-revenue mode".
