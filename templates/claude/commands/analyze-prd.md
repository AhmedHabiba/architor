Read `.arch/state.json` first.

**GATE CHECK:** If `current_phase` is anything other than `not_started` or `evaluation`, STOP and say:
"Cannot start PRD analysis. Current phase is [phase]. Use /status to check progress."

Read the PRD from `.arch/prd.md`.

## Organization Context Check

Read `.arch/org-context.md`. Check if it is the unmodified template by looking for placeholder text like "[e.g.," or "[Your Organization Name]" or checking if key sections (Team Profile, Current Technology Stack) contain only template instructions.

**If org-context.md appears to be filled in (has real values, not template placeholders):**
- Set `phases.evaluation.org_context_loaded` = true
- Set `phases.evaluation.org_context_source` = "file"
- Proceed to PRD evaluation below

**If org-context.md is empty or still has template placeholders:**
- Say: "I notice `.arch/org-context.md` is not filled in. Organizational context directly affects architecture decisions — team size, tech stack, and constraints determine what patterns are feasible.

  I can either:
  A. **Run a discovery interview** (~5 minutes, 15 questions) — I'll generate org-context.md from your answers
  B. **Skip it** — I'll proceed with explicit assumptions marked throughout

  Which do you prefer?"

**If user chooses A (interview), conduct in 3 blocks:**

### Block 1: Scale & Complexity
1. What's your team size? How many developers, DevOps, QA?
2. What's the seniority distribution? (mostly senior, mixed, mostly junior)
3. What's your current tech stack? (backend language, frontend, database, cloud provider)
4. What's your expected scale? (concurrent users, requests/sec, data volume per day)
5. Is this greenfield or replacing/extending an existing system?

Present all 5 questions. Wait for answers before proceeding to Block 2.

### Block 2: Team Reality
6. What technologies has your team successfully operated in production?
7. What technologies have you tried and abandoned? Why?
8. Do you have dedicated DevOps/Platform/DBA roles, or do developers handle infrastructure?
9. What's your CI/CD maturity? (manual deploys, basic pipelines, full GitOps)
10. What monitoring/observability do you currently use?

Present all 5 questions. Wait for answers before proceeding to Block 3.

### Block 3: Constraints
11. What's your cloud provider and any region requirements?
12. What compliance/regulatory requirements apply? (HIPAA, PCI-DSS, SOC2, GDPR, none)
13. What's your monthly infrastructure budget range?
14. What's your timeline? When must this be in production?
15. Any technologies you MUST use or technologies that are BANNED?

After all answers collected:
- Generate `.arch/org-context.md` from the answers, filling in the structured template sections
- Derive a **complexity tier** and note it at the top of org-context.md:
  - **Startup** (team <5, simple stack, no compliance)
  - **Growth** (team 5-15, moderate stack, basic compliance)
  - **Enterprise** (team 15+, complex stack, strict compliance)
  - **Specialized** (any size, unusual workload constraints like real-time, ML, IoT)
- Set `phases.evaluation.org_context_source` = "interview"
- Set `phases.evaluation.org_context_loaded` = true

**If user chooses B (skip), or refuses to answer:**
- Generate `.arch/org-context.md` with explicit assumptions:
  - Team: Assuming 5-10 engineers with moderate experience
  - Scale: Assuming <10K concurrent users
  - Budget: Assuming $3-5K/month infrastructure
  - Cloud: Assuming AWS (most common)
  - Compliance: Assuming no specific regulatory requirements
- Mark each assumption with `[ASSUMED CONTEXT — verify with team]`
- Set `phases.evaluation.org_context_source` = "assumed"
- Set `phases.evaluation.org_context_loaded` = true
- Say: "Proceeding with assumptions. These will be marked throughout the architecture. You can update `.arch/org-context.md` at any time."

---

## PRD Evaluation

Perform a comprehensive PRD evaluation:

### 1. Requirements Extraction
- **Functional Requirements:** List each with an ID (FR-001, FR-002...)
- **Non-Functional Requirements:** Performance, scalability, availability, security, compliance
- **Constraints:** Budget, timeline, technology mandates, team limitations
- **Assumptions:** What the PRD assumes but doesn't state explicitly

### 2. Gap Analysis
For each gap, rate severity: Critical | Important | Minor

Ask specific questions for each gap. Don't be vague — ask questions that have concrete answers.

Bad: "What are the scalability requirements?"
Good: "What's the expected number of concurrent users at peak? What's the target response time at that load?"

### 3. Risk Assessment
- Integration risks (what external systems are involved?)
- Scalability risks (what grows? data? users? transactions?)
- Security surface (where does sensitive data flow?)
- Operational complexity (what's hard to monitor/debug/deploy?)
- Team capability risks (does this require skills the team lacks?)

### 4. PRD Quality Rating
Rate: Comprehensive | Adequate | Needs Significant Clarification

### 5. Recommendations
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
