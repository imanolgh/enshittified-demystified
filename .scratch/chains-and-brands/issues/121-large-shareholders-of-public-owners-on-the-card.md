# Large shareholders of public owners on the card

Type: grilling
Status: resolved
Blocked by: engine/120  (The private equity firm test and asset managers)
Map: [chains-and-brands](../map.md)

## Question

When a brand's chain passes through a public company, how does the brand card show that company's large shareholders (the holders of more than 5% from 13D and 13G filings), including the big asset managers? And how does a brand that an asset manager controls read (the label and one-line explanation for `asset_manager_owned`)?

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
- **From engine "The private equity firm test and asset managers"** (2026-11-20; ADR 0001 amended): new owner kind `asset_manager` (a firm with $50bn or more in registered funds, such as BlackRock, Vanguard, State Street, Fidelity, J.P. Morgan, Goldman Sachs, T. Rowe Price) and new category `asset_manager_owned` (a brand an asset manager controls). This ticket also takes that category's **card label and one-line explanation**. Asset managers are no longer labeled private equity firms, so the large-shareholders line can name them as asset managers.

## Grilling

### Round 1 (2026-11-20)

- **Which holders show** (Q1, option a): every holder above 5% named in a current 13D or 13G, of any kind (asset managers, pensions, activist funds, families, PE firms). This reverses engine "Brand card, receipt and edge shapes" round 2 Q6, which kept 13d-1(b) holdings off the card. Verdict rules are unchanged: a 13d-1(b) holding is listed but never changes a category.
- **Which public companies** (Q2, option a): every public company on the brand's current ownership chains, each with its own list under its name. This also applies to the existing "Private equity shareholders" section.
- **`asset_manager_owned` on the card** (Q3): label "Owned by an asset manager"; explanation "An investment firm that mainly runs mutual funds and ETFs sold to the public controls this brand." No firm is named in the fixed line.

### Round 2 (2026-11-20)

- **Section layout** (Q4, option a): "Private equity shareholders" stays as settled in "Card wording" (the PE holders that count toward the verdict). A new section directly after it, "Other large shareholders of {company}", lists every other holder, with the fixed line "Holders of more than 5% of {company}'s shares, from their SEC filings. Smaller holdings aren't listed. These holders don't change this brand's verdict." Both section titles carry the company's name. A PE firm whose 13G is filed under 13d-1(b) doesn't count, so it sits in "Other large shareholders" with its "Private equity firm" label.
- **Holder row** (Q5): "{holder} · {owner kind} · {percent}% of {class as the filing names it} · as of {event date}", linking to the filing as its receipt ("Verified by an official filing (13G)"). The owner kind is in plain words (Asset manager, Private equity firm, Investment fund, Family, Public company and so on); a holder of unknown kind shows its name only. The percent and date come from the same filing. Rows are sorted by stake, largest first, with no cap.
- **Passive tag** (Q6): rows from a 13G filed under 13d-1(b) or (c) carry "Passive: the filer certifies it isn't trying to influence control", computed from the stored rule box. 13D rows and 13d-1(d) rows carry no tag.

### Round 3 (2026-11-20)

- **Quiet and ended holdings** (Q7): a holder whose hop is unconfirmed (no filing or proxy table in 18 months) drops out of "Other large shareholders" with no line in its place; its data is kept and it returns when a later filing or proxy confirms it. An ended holding (an amendment reporting 5% or less, or 0%) drops out the same way, with no history line. "Formerly PE-owned" history stays PE-only.
- **No duplicates** (Q8): a holder already shown as an owner or under "Private equity shareholders" is left out of "Other large shareholders" for that company.

## Answer

Resolved 2026-11-20 in a grilling session (three rounds, recorded under Grilling).

- **Who shows:** every holder above 5% named in a current 13D or 13G, of any kind, including the asset managers' passive 13d-1(b) filings. This reverses engine "Brand card, receipt and edge shapes" round 2 Q6. Verdict rules are unchanged: a 13d-1(b) holding never changes a category.
- **Which companies:** every public company on the brand's current ownership chains, each with its own list under its name (this also applies to "Private equity shareholders").
- **Layout:** "Private equity shareholders of {company}" stays as settled. Directly after it, "Other large shareholders of {company}", with the fixed line "Holders of more than 5% of {company}'s shares, from their SEC filings. Smaller holdings aren't listed. These holders don't change this brand's verdict."
- **Row:** "{holder} · {owner kind} · {percent}% of {class as the filing names it} · as of {event date}", linking to the filing as its receipt. Plain-word owner kind; a holder of unknown kind shows its name only. Sorted by stake, largest first, no cap.
- **Passive tag:** rows from a 13G filed under 13d-1(b) or (c) carry "Passive: the filer certifies it isn't trying to influence control"; 13D and 13d-1(d) rows carry none.
- **Quiet and ended holdings:** an unconfirmed holder (18 months with no filing or proxy table) or an ended holding (5% or less, or 0%) drops off the list with no line in its place; the data is kept, and an unconfirmed holder returns when confirmed. History stays PE-only.
- **No duplicates:** a holder shown as an owner or under "Private equity shareholders" isn't listed again.
- **`asset_manager_owned`:** label "Owned by an asset manager"; explanation "An investment firm that mainly runs mutual funds and ETFs sold to the public controls this brand."
- Docs: `GLOSSARY.md` gains "Large shareholder". No ADR change.

Handed on:
- "Card wording" (amended): the new section in the section order, the new label in the label table.
- engine "Brand card, receipt and edge shapes" (amended): round 2 Q6 reversed; the card shape gains the other-large-shareholders lists.
- "The how-this-works page" (amended) and "Task: Draft the how-this-works page": section 6 explains the list and the passive tag.
- "Website pages and shareable cards": the new section and its fixed line.
- asset managers map (parked): what v1 now shows; holdings of 5% or less (13F) stay there.
