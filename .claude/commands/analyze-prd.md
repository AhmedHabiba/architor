Read `.arch/state.json` first.

**GATE CHECK:** If `current_phase` is anything other than `not_started` or `evaluation`, STOP and say:
"Cannot start PRD analysis. Current phase is [phase]. Use /status to check progress."

Read the PRD from `.arch/prd.md`.
Read organizational context from `.arch/org-context.md` (if it exists and is filled in).

Perform a comprehensive PRD evaluation:

## 1. Requirements Extraction
- **Functional Requirements:** List each with an ID (FR-001, FR-002...)
- **Non-Functional Requirements:** Performance, scalability, availability, security, compliance
- **Constraints:** Budget, timeline, technology mandates, team limitations
- **Assumptions:** What the PRD assumes but doesn't state explicitly

## 2. Gap Analysis
For each gap, rate severity: 🔴 Critical | 🟡 Important | 🟢 Minor

Ask specific questions for each gap. Don't be vague — ask questions that have concrete answers.

Bad: "What are the scalability requirements?"
Good: "What's the expected number of concurrent users at peak? What's the target response time at that load?"

## 3. Risk Assessment
- Integration risks (what external systems are involved?)
- Scalability risks (what grows? data? users? transactions?)
- Security surface (where does sensitive data flow?)
- Operational complexity (what's hard to monitor/debug/deploy?)
- Team capability risks (does this require skills the team lacks?)

## 4. PRD Quality Rating
Rate: 🟢 Comprehensive | 🟡 Adequate | 🔴 Needs Significant Clarification

## 5. Recommendations
What should be clarified or added before architecture work begins?

After presenting analysis:
- Write the analysis to `.arch/phase1-evaluation.md`
- Update `.arch/state.json`: set `current_phase` to `evaluation`, `phases.evaluation.status` to `awaiting_acceptance`, `phases.evaluation.analysis_complete` to `true`
- Append a decision entry to `.arch/decisions.md`

Ask the user:
"Review the analysis above. You can:
1. **ACCEPT** — Accept this analysis and proceed to Phase 2 (Methodology)
2. **CLARIFY** — Provide answers to the gaps I identified
3. **RE-ANALYZE** — Ask me to focus on a specific area
4. **CHALLENGE** — Tell me what I missed or got wrong"

$ARGUMENTS
