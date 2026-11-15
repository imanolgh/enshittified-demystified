# Task: Draft prompt p9 and run the approval check

Type: task
Status: open
Blocked by: 77  (Extraction prompt rules)
Map: [engine](../map.md)

## Question

Does prompt p9, the v8 test prompt plus the rules settled in "Extraction prompt rules", pass the approval check, so the developer can approve it by committing it?

## Context

- Created 2026-11-15 from [Extraction prompt rules](77-extraction-prompt-rules.md), whose Answer holds the rules (Q1 to Q5), the check and its bars (Q6, Q9) and the approval step. This task does the work. The approval itself is the developer's (CLAUDE.md role contract, item 3).
- **HITL step first:** the developer tops up DeepSeek by $5 (balance $1.18 on 2026-11-15). The check costs about $2 to $2.50 off-peak. No OpenRouter spending (no fallback check, Q10).
- **Claude's steps:**
  1. Draft p9 at `.scratch/engine/research/extraction-prompt-p9.md` from [v8](../research/extraction-test-prompt-v8.md), with the schema minus `document_label`, and the drafting fixes from Q1.
  2. Fetch about 10 new documents under the bot rules (identified user agent, robots.txt, no wire-service pages) that test the new rules: a page saying "used under license", a lender's portfolio page, another team page listing earlier firms' deals, a franchise "independently owned" page, an IP-company trademark notice. Extract them with the block-aware text extractor the 157 used.
  3. Run p9 twice on the 157 clean-text documents plus the new ones, no brand named, DeepSeek's own API, off-peak, 120,000-token output limit. Use the harness at `~/.local/share/extraction-eval/` (scorer `scripts/score_clean.py`). Tell the developer at once if a run is blocked by a balance or key limit.
  4. Score against the bars: at least 138 of 218 known facts per run; at least 98% exact quotes leaving out TSG's page; at most 1 lost answer in 314; no claim breaking a Q2 to Q5 rule in the targeted documents (counted by script: RiverGlade's 12 earlier deals, owners named "private", "privately owned", "local entrepreneurs" or "licensed dentists", licensee claims where the page says licensed, an "affiliate of" claim outside an ownership statement); at least 100 Leonard Green claims.
  5. Blind precision on 40 claims per run, judged by a separate agent that never sees the version: at least 37 fully correct, at most 1 wrong, none of the wrong ones on a new rule.
  6. A missed bar means fix the prompt, rerun the failing documents, then one more full run.
  7. Record the results in research/extraction-model-comparison.md and bring the passing p9 to the developer, who approves it by committing it.
- Document the targeted set (URLs, which rule each tests) so "Testing and acceptance" can make it part of the version check.
