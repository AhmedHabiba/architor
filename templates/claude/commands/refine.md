Read `.arch/state.json` first.

**GATE CHECK:** Something must be in `awaiting_acceptance` status. If nothing is pending, say: "Nothing is currently pending refinement. Use /status to check state."

The user wants to refine the current proposal. Their feedback is in $ARGUMENTS.

## Determine what is being refined

**If Phase 1 (Evaluation):** 
- Re-read `.arch/phase1-evaluation.md`
- Apply the user's feedback
- Re-analyze the specific areas mentioned
- Rewrite `.arch/phase1-evaluation.md` with updates
- Append refinement to `.arch/decisions.md`
- Present updated analysis, highlight what changed

**If Phase 2 (Methodology):**
- Re-read `.arch/phase2-methodology.md` and `.arch/phase2-components-overview.md`
- Apply feedback to the OVERALL approach (not individual components)
- If user tries to refine a specific component's details: "Individual component refinement happens in Phase 3. In Phase 2, I can adjust the overall architecture pattern, component boundaries, or integration approach. What would you like to change at the system level?"
- Rewrite both files with updates
- Present updated methodology and component overview, highlight what changed

**If Phase 3 (Component):**
- Read the current component file from `.arch/components/[current_component].md`
- Apply feedback to this specific component only
- Check if changes affect previously accepted components — if yes, FLAG it: "⚠️ This change affects [Component X] which was already accepted. Specifically: [what breaks]. We should address this before proceeding."
- Rewrite the component file
- Present updated design, highlight what changed

After refinement:
- Status remains `awaiting_acceptance`
- Append refinement to `.arch/decisions.md` with what was changed and why
- Ask for acceptance again

$ARGUMENTS
