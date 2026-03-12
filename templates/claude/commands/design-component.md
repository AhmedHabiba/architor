Read `.arch/state.json` first.

**GATE CHECK:**
- If `current_phase` is not `components`, STOP: "Cannot design components. Current phase is [phase]. Methodology must be accepted first."
- If `phases.methodology.accepted` is not `true`, STOP: "Phase 2 (Methodology) must be accepted first."
- If there is a `current_component` with status `in_progress` or `awaiting_acceptance` that is DIFFERENT from the requested component, STOP: "Component [current_component] is still pending. Accept or refine it before moving to another component. Use /status to check."

Read `.arch/phase2-methodology.md` and `.arch/phase2-components-overview.md` for context.
Read `.arch/org-context.md` for team and technology constraints.
Read any previously accepted components in `.arch/components/` for consistency checking.

If `$ARGUMENTS` is empty, determine the next component in logical dependency order (foundational components first — databases, auth, core services before dependent services).

## Detailed Component Design for: [Component Name]

### 1. Component Specification
- **Name:** [exact name]
- **Role:** [detailed description — what it does, what it owns]
- **Bounded Context:** [what data/logic belongs exclusively to this component]

### 2. Technology Recommendation
- **Primary recommendation:** [Technology vX.Y]
- **Why:** [Specific rationale tied to requirements AND org context]
- **Alternative 1:** [Technology] — [why not chosen]
- **Alternative 2:** [Technology] — [why not chosen]

If org-context lists a preferred technology, acknowledge it:
"Your organization prefers [X]. I'm recommending [Y] instead because [reason]. If you'd prefer to stay with [X], here's what changes: [impact]."

### 3. Integration Specification
- **Inputs:** [what this component receives, from whom, what protocol, what format]
- **Outputs:** [what this component produces, for whom, what protocol, what format]
- **API Contracts:** [key endpoints/interfaces with request/response shapes]
- **Data Formats:** [JSON schemas, message formats, events published]

**CONSISTENCY CHECK:** Compare these integration points with previously accepted components. Flag any mismatches:
"⚠️ This component expects [X format] from [Component Y], but Component Y was accepted with [Z format]. We need to resolve this."

### 4. Scalability
- **Scaling approach:** [horizontal/vertical, what triggers scaling]
- **Bottleneck:** [what breaks first under load]
- **Data growth:** [how data volume grows over time, storage implications]

### 5. Security
- **Authentication:** [how this component authenticates callers]
- **Authorization:** [what permission model it enforces]
- **Data sensitivity:** [what sensitive data it handles, encryption approach]
- **Attack surface:** [what external-facing endpoints exist]

### 6. Monitoring & Observability
- **Key metrics:** [what to measure — latency, error rate, throughput, queue depth]
- **Alerting:** [what thresholds trigger alerts]
- **Logging:** [what to log, structured format, retention]
- **Tracing:** [distributed tracing integration]

### 7. Failure Modes
- **What happens when this component goes down?**
- **What happens when its dependencies are unavailable?**
- **Fallback strategy:** [circuit breaker, graceful degradation, retry policy]
- **Data consistency:** [what happens to in-flight operations during failure?]
- **Recovery:** [how does it recover? manual intervention needed?]

### 8. Complexity Assessment
- **Estimated complexity:** 🟢 Simple | 🟡 Moderate | 🔴 Complex
- **Justification:** [why this rating]
- **Build estimate:** [rough t-shirt size: days/weeks]

### 9. Traceability

Read `.arch/phase1-evaluation.md` for FR-NNN identifiers. Read `.arch/decisions.md` for Phase 2C DEC-NNN entries.

**Requirements Satisfied:**
- [ ] FR-NNN: [requirement description] — [how this component addresses it]
- [ ] FR-NNN: [requirement description] — [how this component addresses it]
(list every FR-NNN from Phase 1 evaluation that this component directly satisfies)

**Cross-Cutting Compliance:**
- [ ] DEC-NNN: [cross-cutting decision] — [how this component complies]
- [ ] DEC-NNN: [cross-cutting decision] — [how this component complies]
(list every Phase 2C DEC-NNN that applies to this component)

**Depends On:** [list other components this design depends on, if any]

After presenting:
- Write component design to `.arch/components/[component-name].md`
- Update `.arch/state.json`: set `current_component`, update component status to `awaiting_acceptance`
- Append decisions to `.arch/decisions.md`

**Before asking for acceptance, CHALLENGE the user:**
"Before you accept, I want to flag these concerns:
1. [specific concern about this component]
2. [integration risk with another component]
3. [operational consideration]
Are you comfortable with these, or should we address them?"

Ask the user:
"You can:
1. **ACCEPT** — Accept this component design (auto-advances to next component)
2. **REFINE** — Tell me what to change
3. **ALTERNATIVE** — Suggest a different technology and I'll redesign around it
4. **CHALLENGE** — Push back on specific decisions"

$ARGUMENTS
