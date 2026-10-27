# No manual review: every classification and publication decision is automated

Status: accepted (2026-10-26). Supersedes the human review queue in CLAUDE.md, `decisions.md` §8, `evidence_layer_plan.md` Stage 5–6, `build_roadmap.md` Steps 8 and 26, and `pre-launch-seeding.md` W5/W8.

The developer will not staff a review queue, so no fact waits on a human. A fact backed by one non-official source publishes as **`reported`** and the card says so. Contradicting sources publish nothing as fact: the card shows **"sources disagree"** with links to each source. We chose this because a one-person project cannot drain a queue that grows with every batch, and an honest "reported" or "sources disagree" label is publishable where a silent backlog is not.

## Rules

- Two independent sources (different `source_type` or domain), or one official filing → `verified`. One non-official source → `reported`. Unchanged from before; only the review item is dropped.
- **Ownership conflict** = two sources each claiming a different *controlling* owner over overlapping dates. Co-investors and minority holders are not conflicts.
- **Ownership loops** (A owned by B owned by A) stop the chain walk; every business that depends on the loop is `sources_disagree`.
- Owner-kind contradictions resolve by source rank (ADR 0001); only same-rank contradictions give "owner type not confirmed".
- Certified Independent (later feature, not in the MVP) will be granted only by automated checks against official records.
- **Ambiguous entity match** (Step 9, research_flows A1): try every deterministic tiebreaker first (address, phone, NPI). Still ambiguous → the ingest item is `ambiguous` with its candidates stored; no claim attaches to any candidate; the search shows "couldn't confirm which business this is". Never create a new entity or take the top candidate. Re-attempted automatically when an identity source (NPPES, SoS, license board) is added or refreshed.
- **Jev claim-support check** (Step 27b, if adopted): low confidence → claim status `unsupported`. The row stays (append-only) but never counts toward an edge. Jev can only remove a claim from publication, never verify, publish or downgrade one. Not a downgrade to `reported`, which keeps meaning exactly "one non-official source".
- **BDC numeric cross-check failure** (Step 21): that row's claim is rejected and logged as a parse failure. Above a per-filing failure-rate threshold (a setting), all of that filing's claims are withheld, the filing is marked unparseable (`no_evidence_found`), and an operational alert fires. The alert asks for a parser fix, never a ruling on a fact.
- **Pre-launch spot-check** (W7) is system QA, not fact review: its findings become fixes to code, fixtures, thresholds or the prompt, followed by a re-run. No one approves, edits or deletes an individual fact by hand.

## Consequences

- Step 26 (review panel) is dropped. The `review_items` table is dropped (ruled 2026-10-26): single-source → edge `reported`, conflict → category `sources_disagree`, low confidence → claim `rejection_reason = unsupported`. Claim status is `pending|accepted|rejected|retracted` plus `rejection_reason`; ingest items gain `result = ambiguous` + `candidates` (evidence_layer_plan.md §4).
- The four places the docs used to route to review (ambiguous resolution, Jev's claim-support check, BDC cross-check failures, the W7 spot-check) each have an automated rule above (added 2026-10-26).
