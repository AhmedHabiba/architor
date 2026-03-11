Read `.arch/state.json` first.

**GATE CHECK:** Something must be in `awaiting_acceptance` status. If nothing is pending, say: "Nothing is currently pending. Use /status to check state."

The user wants a fundamentally different approach. Their request is in $ARGUMENTS.

## If Phase 2 (Methodology):
- Propose a COMPLETELY different architecture pattern
- Don't just tweak the existing one — rethink from the requirements
- Compare the new proposal against the previous one explicitly
- Rewrite `.arch/phase2-methodology.md` and `.arch/phase2-components-overview.md`
- Append to `.arch/decisions.md`:
  ```
  ### [DEC-NNN] Phase 2 | Alternative
  - **Decision:** Alternative methodology. New: [pattern]
  - **Rationale:** [user's reason for requesting alternative]
  - **Alternatives:** Previous approach: [previous pattern]
  - **Trade-offs:** [what changed — improvements and regressions]
  - **Risk:** [residual risk of the new approach]
  - **Supersedes:** [DEC-NNN of the previous proposal decision for this target]
  - **Date:** [timestamp]
  ```

## If Phase 3 (Component):
- Redesign the current component around the alternative technology the user suggested
- Show how the alternative changes integration points with other components
- Compare: what improves, what gets worse, what stays the same
- Rewrite `.arch/components/[current_component].md`
- Append to `.arch/decisions.md`:
  ```
  ### [DEC-NNN] Phase 3 | Alternative
  - **Decision:** Alternative technology for [component]. New: [tech]
  - **Rationale:** [user's reason]
  - **Alternatives:** Previous: [previous tech]
  - **Trade-offs:** [what improves, what gets worse]
  - **Risk:** [residual risk]
  - **Supersedes:** [DEC-NNN of the previous proposal decision for this component]
  - **Date:** [timestamp]
  ```

After presenting the alternative:
- Status remains `awaiting_acceptance`
- Present comparison table: Original vs Alternative
- Ask: "Do you prefer this alternative, want to go back to the original, or refine further?"

$ARGUMENTS
