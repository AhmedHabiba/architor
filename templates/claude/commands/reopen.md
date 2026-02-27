Read `.arch/state.json` first.

**GATE CHECK:**
- If `reopens.count` >= `reopens.max`, STOP: "Maximum reopens reached ([count] of [max]). This limit prevents infinite rework. If you need further changes, consider working within the current constraints or starting a new architecture session."
- If `current_phase` is `not_started`, STOP: "Nothing to reopen. The project hasn't started yet."

The user wants to reopen an accepted phase or component. Parse $ARGUMENTS to determine:
1. **Target**: What is being reopened (e.g., "phase 2a", "phase 2c", "component api-gateway")
2. **Justification**: Why it needs to be reopened

If justification is missing, ask: "What changed that requires reopening [target]? I need a justification to record in the decision log."

---

## Reopening a Phase

**If target is Phase 1 (evaluation):**
- Set `phases.evaluation.accepted` = false, `phases.evaluation.status` = "in_progress"
- Cascade: un-accept ALL of Phase 2 (reset pattern_accepted, components_overview_accepted, cross_cutting_accepted, accepted all to false)
- Cascade: set all Phase 3 components to status "needs-review"
- Set `phases.components.all_accepted` = false
- Set `current_phase` = "evaluation"

**If target is Phase 2A (pattern):**
- Set `phases.methodology.pattern_accepted` = false
- Cascade: also un-accept components_overview and cross_cutting
- Cascade: set all Phase 3 components to "needs-review", `all_accepted` = false
- Set `phases.methodology.accepted` = false
- Set `current_phase` = "methodology", `sub_phase` = "pattern"

**If target is Phase 2B (components_overview):**
- Set `phases.methodology.components_overview_accepted` = false
- Cascade: also un-accept cross_cutting
- Cascade: set all Phase 3 components to "needs-review", `all_accepted` = false
- Set `phases.methodology.accepted` = false
- Set `current_phase` = "methodology", `sub_phase` = "components_overview"

**If target is Phase 2C (cross_cutting):**
- Set `phases.methodology.cross_cutting_accepted` = false
- Cascade: set all Phase 3 components to "needs-review", `all_accepted` = false
- Set `phases.methodology.accepted` = false
- Set `current_phase` = "methodology", `sub_phase` = "cross_cutting"

## Reopening a Component

**If target is a specific component name:**
- The component must currently be in "accepted" status. If not, STOP: "Component [name] is not accepted. It's currently [status]."
- Set its status to "in_progress"
- Set `current_component` to this component name
- Set `phases.components.all_accepted` = false
- Decrement `accepted_count`
- Find components that list this component in their integration points and mark them as "needs-review"
- If `current_phase` is not "components", set `current_phase` = "components"

## After Reopening (always do this)

- Increment `reopens.count`
- Add to `reopens.history`: `{ "target": "[target]", "justification": "[user's reason]", "timestamp": "[now]", "cascade": ["list of affected items"] }`
- Append to `.arch/decisions.md`:
  ```
  ### [DEC-NNN] Reopen
  - **Decision:** Reopened [target]
  - **Rationale:** [user's justification]
  - **Cascade:** [list of items that were un-accepted or marked needs-review]
  - **Trade-offs:** Progress reset on [count] items
  - **Risk:** Reopens remaining: [max - count]
  - **Date:** [timestamp]
  ```

Say: "[Target] has been reopened. [Count] dependent items marked for re-review. Reopens remaining: [max - new count].

Use `/propose-methodology` or `/design-component` to rework the reopened item."

$ARGUMENTS
