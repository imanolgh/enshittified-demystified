# Large shareholders of public owners on the card

Type: grilling
Status: open
Blocked by: engine/120  (The private equity firm test and asset managers)
Map: [chains-and-brands](../map.md)

## Question

When a brand's chain passes through a public company, how does the brand card show that company's large shareholders (the holders of more than 5% from 13D and 13G filings), including the big asset managers?

## Context

- Opened 2026-11-20 from engine "Retrieval fan-out, tracked entities and refresh cadence" (round 2, Q11, Q13, Q14). The developer wants readers to see when BlackRock, Vanguard, State Street and similar managers hold large stakes in a brand's owner.
- **Engine side, settled:**
  - Every tracked public company's 13D and 13G filings are read ("EDGAR full-text search and ownership filings"), and each holder's stake is a claim and an edge.
  - A 13G filed under Rule 13d-1(b), the institutional box, never changes a verdict ("Category precedence and storage"). Such a holder is stored and can be shown, but isn't tracked through that filing (ticket 37 Q11).
  - BlackRock, Vanguard and State Street are tracked through an operator list (Q14).
  - An amendment reporting 5% or less ends the holder's hop.
- **Example:** Hanes → Hanesbrands → Gildan Activewear (public company, NYSE: GIL). Holders on Gildan: CDPQ (13G under 13d-1(c), 6.3%), Janus Henderson, 1832 Asset Management, Cooke & Bieler, FMR, Jarislowsky Fraser, Bank of Nova Scotia and BlackRock (13Gs), and Browning West (13D). Coliseum Capital dropped below 5% in August 2024 (chains "Research: Product-industry audits", apparel).
- **Limits:** 13G and 13D filings exist only for public companies and only above 5%, so most brands in the data (private, PE-owned) have no such line. Holdings below 5% need 13F filings, which are on the parked Asset Managers map.
- **Card rules that apply** (chains "Card wording"): self-explaining labels, a one-line explanation, nothing readers must memorize.
- **Open:**
  - the wording, factual like the rest of the card (Q13 recommended every 5%+ holder, with listed asset managers marked);
  - every holder or only the listed managers;
  - placement on the card;
  - how a holder's label reads before and after "The private equity firm test and asset managers" decides how asset managers are classed;
  - whether the line also covers public companies further up a chain.
