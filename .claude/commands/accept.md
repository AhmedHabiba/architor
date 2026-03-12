Read `.arch/state.json` first.

This command handles acceptance for any phase or component.

## Determine what is being accepted

Check the current state:

**If `current_phase` is `evaluation` and `phases.evaluation.status` is `awaiting_acceptance`:**
- Confirm with user: "You are accepting the PRD Evaluation analysis. This means we proceed to Phase 2 (Methodology). Do you ACCEPT? (yes/no)"
- If confirmed: Update `phases.evaluation.accepted` = true, `phases.evaluation.accepted_at` = now, `current_phase` = "methodology", `phases.methodology.status` = "in_progress"
- Append to `.arch/decisions.md`: Phase 1 acceptance with summary of accepted analysis
- Say: "Phase 1 (Evaluation) accepted. Run `/propose-methodology` to begin Phase 2A (Architecture Pattern)."

**If `current_phase` is `methodology`:**

Check `phases.methodology.sub_phase`:

- **If `sub_phase` is `pattern` and status is `awaiting_acceptance`:**
  - Confirm: "You are accepting the architecture pattern: [pattern name]. This proceeds to Phase 2B (Component Map). Do you ACCEPT? (yes/no)"
  - If confirmed: Update `pattern_accepted` = true, `pattern_accepted_at` = now, `sub_phase` = null, status = `in_progress`
  - Append to `.arch/decisions.md`: Pattern accepted with pattern name. Include `**References:** [FR-NNN requirements that drove the pattern selection]` from Phase 1 evaluation.
  - Say: "Phase 2A (Pattern) accepted: [pattern name]. Run `/propose-methodology` to continue with Phase 2B (Component Map)."

- **If `sub_phase` is `components_overview` and status is `awaiting_acceptance`:**
  - Confirm: "You are accepting the component map ([N] components). This proceeds to Phase 2C (Cross-Cutting Decisions). Do you ACCEPT? (yes/no)"
  - If confirmed: Update `components_overview_accepted` = true, `components_overview_accepted_at` = now, `sub_phase` = null, status = `in_progress`
  - Append to `.arch/decisions.md`: Component map accepted with count
  - Say: "Phase 2B (Component Map) accepted: [N] components. Run `/propose-methodology` to continue with Phase 2C (Cross-Cutting Decisions)."

- **If `sub_phase` is `cross_cutting` and status is `awaiting_acceptance`:**
  - Confirm: "You are accepting the cross-cutting decisions. This completes Phase 2 and proceeds to Phase 3 (Component Design). Do you ACCEPT? (yes/no)"
  - If confirmed: Update `cross_cutting_accepted` = true, `cross_cutting_accepted_at` = now, `accepted` = true, `accepted_at` = now
  - Initialize `phases.components`: set `current_phase` = "components", `status` = "in_progress", populate `components` object from the overview with status `pending` for each, set `total_count`
  - Append to `.arch/decisions.md`: Phase 2 complete, all three sub-phases accepted. Include `**References:** [FR-NNN requirements addressed by cross-cutting decisions]`.
  - Say: "Phase 2 complete. Pattern: [name]. Components: [N]. Cross-cutting decisions locked. Run `/design-component` to begin Phase 3."

**If `current_phase` is `components` and there is a `current_component` with status `awaiting_acceptance`:**
- Confirm: "You are accepting the detailed design for component: [name]. Do you ACCEPT? (yes/no)"
- If confirmed: Update that component's status to `accepted`, increment `accepted_count`, clear `current_component`
- Check if ALL components are now accepted: if yes, set `phases.components.all_accepted` = true
- Append to `.arch/decisions.md`: Component acceptance with key technology choice. Include `**References:** [FR-NNN requirements this component satisfies], [DEC-NNN cross-cutting decisions from Phase 2C it complies with]` from the component's Traceability section.
- If all complete: "All [N] components accepted! Phase 3 complete. Run `/generate-docs` to begin Phase 4 (Finalization)."
- If more components remain:
    1. Say: "Component [name] accepted. Progress: [X of Y] complete."
    2. Say: "Auto-advancing to next component..."
    3. Add a brief separator line: "---"
    4. **Proceed to design the next component** using the same process defined in the `/design-component` command. Refer to that command's instructions for the full detailed design process including all 9 sections, cross-cutting compliance check, consistency check against accepted components, and adversarial challenge before acceptance.

**If `current_phase` is `finalization` and document is generated:**
- Confirm: "You are approving the final architecture document. This completes the architecture design process. Do you ACCEPT? (yes/no)"
- If confirmed: Update `phases.finalization.document_approved` = true, `approved_at` = now
- Say: "Architecture document approved. Final document: `output/architecture-document.md`. The architecture design process is complete."

**If nothing is awaiting acceptance:**
- Say: "Nothing is currently awaiting acceptance. Use /status to check the current state."

$ARGUMENTS
