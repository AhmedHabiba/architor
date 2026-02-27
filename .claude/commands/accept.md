Read `.arch/state.json` first.

This command handles acceptance for any phase or component.

## Determine what is being accepted

Check the current state:

**If `current_phase` is `evaluation` and `phases.evaluation.status` is `awaiting_acceptance`:**
- Confirm with user: "You are accepting the PRD Evaluation analysis. This means we proceed to Phase 2 (Methodology). Confirm? (yes/no)"
- If confirmed: Update `phases.evaluation.accepted` = true, `phases.evaluation.accepted_at` = now, `current_phase` = "methodology", `phases.methodology.status` = "in_progress"
- Append to `.arch/decisions.md`: Phase 1 acceptance with summary of accepted analysis
- Say: "✅ Phase 1 (Evaluation) accepted. Run `/propose-methodology` to begin Phase 2."

**If `current_phase` is `methodology` and `phases.methodology.status` is `awaiting_acceptance`:**
- Confirm: "You are accepting BOTH the architecture methodology ([pattern name]) AND the holistic component overview ([N] components). This means we proceed to Phase 3 where we design each component in detail. Confirm? (yes/no)"
- If confirmed: Update `phases.methodology.accepted` = true, `phases.methodology.pattern_accepted` = true, `phases.methodology.components_overview_accepted` = true, `phases.methodology.accepted_at` = now
- Initialize `phases.components`: set `current_phase` = "components", `status` = "in_progress", populate `components` object from the overview with status `pending` for each, set `total_count`
- Append to `.arch/decisions.md`: Pattern accepted, component list finalized
- Say: "✅ Phase 2 (Methodology) accepted. Architecture pattern: [name]. Components to design: [N]. Run `/design-component` to begin Phase 3 with the first component."

**If `current_phase` is `components` and there's a `current_component` with status `awaiting_acceptance`:**
- Confirm: "You are accepting the detailed design for component: [name]. Confirm? (yes/no)"
- If confirmed: Update that component's status to `accepted`, increment `accepted_count`, clear `current_component`
- Check if ALL components are now accepted: if yes, set `phases.components.all_accepted` = true
- Append to `.arch/decisions.md`: Component acceptance with key technology choice
- If all complete: "✅ All [N] components accepted! Phase 3 complete. Run `/generate-docs` to begin Phase 4 (Finalization)."
- If more components remain: 
    1. Say: "✅ Component [name] accepted. Progress: [X of Y] complete."
    2. Say: "⏭️ Auto-advancing to next component..."
    3. Add a brief separator line: "---"
    4. **IMMEDIATELY proceed to design the next component** — follow the exact same process as the `/design-component` command:
       - Determine the next component in logical dependency order from the components list (pick the next `pending` component, prioritizing foundational/dependency-free components first)
       - Read `.arch/phase2-methodology.md`, `.arch/phase2-components-overview.md`, `.arch/org-context.md`, and all previously accepted components in `.arch/components/`
       - Update `state.json`: set the new component as `current_component` with status `in_progress`
       - Produce the full detailed component design (specification, technology recommendation, integration, scalability, security, monitoring, failure modes, complexity assessment)
       - Update `state.json`: set component status to `awaiting_acceptance`
       - Write the design to `.arch/components/[component-name].md`
       - Challenge the user before asking for acceptance
       - Present the Accept / Refine / Alternative / Challenge options
    5. The user can then `/accept` again to continue the chain, or `/refine` / `/alternative` to adjust before accepting

**If `current_phase` is `finalization` and document is generated:**
- Confirm: "You are approving the final architecture document. This completes the architecture design process. Confirm? (yes/no)"
- If confirmed: Update `phases.finalization.document_approved` = true, `approved_at` = now
- Say: "✅ Architecture document approved. Final document: `output/architecture-document.md`. The architecture design process is complete."

**If nothing is awaiting acceptance:**
- Say: "Nothing is currently awaiting acceptance. Use /status to check the current state."

$ARGUMENTS
