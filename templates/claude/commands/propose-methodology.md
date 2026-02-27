Read `.arch/state.json` first.

**GATE CHECK:**
- If `current_phase` is `evaluation` and `phases.evaluation.accepted` is false, STOP: "Phase 1 (Evaluation) must be accepted first. Run /accept or use /status to check progress."
- If `current_phase` is not `evaluation` and `current_phase` is not `methodology`, STOP: "Cannot propose methodology. Current phase is [phase]."

Read `.arch/phase1-evaluation.md` for the accepted analysis.
Read `.arch/org-context.md` for organizational constraints.

## Determine which sub-phase to execute

Check `phases.methodology`:
- If `pattern_accepted` is false: Execute **Phase 2A** below
- If `pattern_accepted` is true AND `components_overview_accepted` is false: Execute **Phase 2B** below
- If `components_overview_accepted` is true AND `cross_cutting_accepted` is false: Execute **Phase 2C** below
- If all three are accepted: STOP: "Phase 2 is complete. All sub-phases accepted. Run /design-component to begin Phase 3."

---

## Phase 2A — Architecture Pattern Proposal

Propose an architecture pattern. Your proposal MUST include:

### 1. Recommended Pattern
Name the pattern (e.g., Event-Driven Microservices, Modular Monolith, Serverless-First, CQRS, Layered Monolith, Hybrid).

### 2. Why This Pattern — Specific to THIS Project
Don't give generic benefits. Map each benefit to a specific requirement from the PRD.
- "I recommend [pattern] because requirement FR-007 needs [X], and this pattern provides [Y]"
- Reference the team profile: "Given your team of [N] with [skills], this pattern's operational complexity is manageable because..."

### 3. What You Sacrifice
Every pattern has costs. Be explicit:
- What becomes harder?
- What technical debt does this introduce?
- What future flexibility do you lose?

### 4. Alternatives Considered
Present at least 2 alternative patterns with brief comparison.

| Criterion | Recommended | Alternative 1 | Alternative 2 |
|-----------|------------|----------------|----------------|
| Fits requirements | ... | ... | ... |
| Team capability | ... | ... | ... |
| Operational cost | ... | ... | ... |
| Time to deliver | ... | ... | ... |
| Future flexibility | ... | ... | ... |

### 5. Key Architectural Decisions
List the top 5-7 architectural decisions this pattern implies (e.g., synchronous vs async communication, shared vs separate databases, deployment strategy).

After presenting:
- Write methodology to `.arch/phase2-methodology.md`
- Update `.arch/state.json`: set `current_phase` to `methodology`, `phases.methodology.status` to `awaiting_acceptance`, `sub_phase` to `pattern`, `pattern_proposed` to `true`
- Append decisions to `.arch/decisions.md`

Ask the user:
"Review the architecture pattern. You can:
1. **ACCEPT** — Accept this architecture pattern (proceeds to Phase 2B: Component Map)
2. **REFINE** — Tell me what to change
3. **ALTERNATIVE** — Ask me to propose a completely different pattern
4. **CHALLENGE** — Push back on specific decisions

Note: This accepts the pattern only. Component map and cross-cutting decisions are separate steps."

---

## Phase 2B — Holistic Component Overview

Read `.arch/phase2-methodology.md` for the accepted pattern.

Present the COMPLETE system as components. This is the big picture — NOT detailed design.

For EACH component:
| # | Component | Role (one sentence) | Why It Exists | Connects To | Technology Direction |
|---|-----------|-------------------|---------------|-------------|---------------------|
| 1 | ... | ... | ... | ... | ... |

Then describe the end-to-end flow: how a typical user request travels through these components.

**CHALLENGE YOURSELF before presenting:**
- Is this too many components for the team size?
- Is any component doing too much (god service)?
- Are there missing cross-cutting concerns (auth, logging, monitoring)?
- Could any two components be merged without loss?

After presenting:
- Write component overview to `.arch/phase2-components-overview.md`
- Update `.arch/state.json`: set `sub_phase` to `components_overview`, `components_overview_proposed` to `true`, `component_count` to the number of components, status to `awaiting_acceptance`
- Append decisions to `.arch/decisions.md`

Ask the user:
"Review the component overview. You can:
1. **ACCEPT** — Accept this component map (proceeds to Phase 2C: Cross-Cutting Decisions)
2. **REFINE** — Tell me what to change about the component boundaries
3. **CHALLENGE** — Push back on specific components

Note: Individual component details come in Phase 3. Accept or reject the big picture first."

---

## Phase 2C — Cross-Cutting Decisions

Read `.arch/phase2-methodology.md` and `.arch/phase2-components-overview.md`.

Present cross-cutting architectural decisions that constrain ALL component designs in Phase 3. These MUST include:

### 1. Authentication & Authorization Strategy
- Pattern (JWT, session, OAuth2, API keys, service mesh mTLS)
- Token propagation across components
- Service-to-service authentication
- Authorization model (RBAC, ABAC, etc.)
- Every component MUST comply with this decision

### 2. Observability Strategy
- Logging standard (structured JSON, correlation IDs)
- Metrics collection (Prometheus, CloudWatch, Datadog)
- Distributed tracing (OpenTelemetry, Jaeger)
- Alerting approach and thresholds

### 3. Deployment Strategy
- CI/CD pipeline approach
- Environment strategy (dev, staging, prod)
- Container/orchestration strategy
- Release strategy (blue-green, canary, rolling)
- Rollback procedure

### 4. Error Handling & Resilience
- Circuit breaker pattern and library
- Retry policy (exponential backoff, max retries)
- Timeout strategy (per-service defaults)
- Graceful degradation rules

### 5. Data Management Cross-Cuts
- Database migration strategy
- Backup and restore approach
- Data encryption standards
- Cache invalidation strategy

For each decision, compare at least 2 options with trade-offs.

After presenting:
- Write cross-cutting decisions to `.arch/phase2-cross-cutting.md`
- Update `.arch/state.json`: set `sub_phase` to `cross_cutting`, `cross_cutting_proposed` to `true`, status to `awaiting_acceptance`, populate `cross_cutting_decisions` object with the key decisions
- Append decisions to `.arch/decisions.md`

Ask the user:
"Review the cross-cutting decisions. These become CONSTRAINTS for every component in Phase 3. You can:
1. **ACCEPT** — Accept these cross-cutting decisions (completes Phase 2, proceeds to Phase 3)
2. **REFINE** — Tell me what to change
3. **CHALLENGE** — Push back on specific decisions

Once accepted, these decisions cannot be changed without a /reopen."

$ARGUMENTS
