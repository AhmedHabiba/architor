Read `.arch/state.json` first.

**GATE CHECK:** 
- If `current_phase` is not `evaluation` or `methodology`, STOP: "Cannot propose methodology. Current phase is [phase]."
- If `phases.evaluation.accepted` is not `true`, STOP: "Phase 1 (Evaluation) must be accepted first. Use /status to check progress."

Read `.arch/phase1-evaluation.md` for the accepted analysis.
Read `.arch/org-context.md` for organizational constraints.

## Part A — Architecture Pattern Proposal

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

## Part B — Holistic Component Overview

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
- Write methodology to `.arch/phase2-methodology.md`
- Write component overview to `.arch/phase2-components-overview.md`
- Update `.arch/state.json`: set `current_phase` to `methodology`, `phases.methodology.status` to `awaiting_acceptance`, `pattern_proposed` to `true`, `components_overview_proposed` to `true`
- Append decisions to `.arch/decisions.md`

Ask the user:
"Review the architecture pattern and component overview. You can:
1. **ACCEPT** — Accept BOTH the methodology and component architecture (proceeds to Phase 3)
2. **REFINE** — Tell me what to change (applies to overall approach, NOT individual components)
3. **ALTERNATIVE** — Ask me to propose a completely different pattern
4. **CHALLENGE** — Push back on specific decisions

⚠️ Note: You cannot refine individual components yet. That's Phase 3. Accept or reject the big picture first."

$ARGUMENTS
