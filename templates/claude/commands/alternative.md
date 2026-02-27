Read `.arch/state.json` first.

**GATE CHECK:** Something must be in `awaiting_acceptance` status. If nothing is pending, say: "Nothing is currently pending. Use /status to check state."

The user wants a fundamentally different approach. Their request is in $ARGUMENTS.

## If Phase 2 (Methodology):
- Propose a COMPLETELY different architecture pattern
- Don't just tweak the existing one — rethink from the requirements
- Compare the new proposal against the previous one explicitly
- Rewrite `.arch/phase2-methodology.md` and `.arch/phase2-components-overview.md`
- Append to `.arch/decisions.md`: "Alternative methodology requested. Previous: [pattern]. New: [pattern]. Reason: [user's reason]"

## If Phase 3 (Component):
- Redesign the current component around the alternative technology the user suggested
- Show how the alternative changes integration points with other components
- Compare: what improves, what gets worse, what stays the same
- Rewrite `.arch/components/[current_component].md`
- Append to `.arch/decisions.md`: "Alternative technology for [component]. Previous: [tech]. New: [tech]. Reason: [reason]"

After presenting the alternative:
- Status remains `awaiting_acceptance`
- Present comparison table: Original vs Alternative
- Ask: "Do you prefer this alternative, want to go back to the original, or refine further?"

$ARGUMENTS
