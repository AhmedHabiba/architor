This command launches an adversarial architecture review of a component.

Read `.arch/state.json`. The component to review is specified in $ARGUMENTS. If empty, use the `current_component`.

**GATE CHECK:** The component must have a design file in `.arch/components/[name].md`. If not, STOP: "No design found for component [name]. Design it first with /design-component [name]."

Act as a **different architect** — a skeptical principal architect conducting a formal design review. Forget that you proposed this design. Your job is to find problems.

Read:
- `.arch/components/[component-name].md` — the design under review
- `.arch/phase2-methodology.md` — the overall architecture
- `.arch/phase2-components-overview.md` — how this fits in the system
- `.arch/org-context.md` — organizational constraints
- Any other accepted components in `.arch/components/` — for consistency

## Review Criteria

### 1. Requirements Alignment
- Does this component fully satisfy its stated requirements?
- Are there requirements from the PRD that this component should address but doesn't?

### 2. Technology Fitness
- Is the chosen technology appropriate for the scale?
- Is it appropriate for the team's skill level?
- Are there licensing, cost, or vendor lock-in concerns?

### 3. Integration Integrity
- Do the API contracts match what connected components expect?
- Are data formats consistent across boundaries?
- Is the communication pattern (sync/async) appropriate?

### 4. Failure Analysis
- What's the blast radius if this component fails?
- Is the fallback strategy realistic or wishful thinking?
- What happens to data consistency during failures?

### 5. Security Review
- Are there unprotected endpoints?
- Is sensitive data properly encrypted in transit and at rest?
- Is the authentication/authorization model sufficient?

### 6. Operational Readiness
- Can the team realistically monitor this?
- Are the alerting thresholds meaningful or arbitrary?
- How difficult is debugging when things go wrong?

### 7. Scalability Honesty
- What actually breaks first under 10x load?
- Is the scaling approach tested or theoretical?

## Output

Rate each criterion: ✅ Pass | ⚠️ Concern | ❌ Fail

Write findings to `.arch/reviews/[component-name]-review.md`

Present findings and for each concern or failure, provide a specific recommendation.

End with: "Address these findings by running `/refine [specific feedback]` or accept the risks by running `/accept`."

$ARGUMENTS
