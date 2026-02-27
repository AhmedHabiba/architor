#!/usr/bin/env python3
"""
Hook: PreToolUse — Validates phase transitions in state.json
Exit 0 = allow the write
Exit 1 = block the write (Claude gets error message)
"""

import json
import sys
import os

STATE_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "state.json")

LEGAL_TRANSITIONS = {
    "not_started": ["evaluation"],
    "evaluation": ["methodology"],
    "methodology": ["components"],
    "components": ["finalization"],
    "finalization": []
}

PREREQUISITES = {
    "methodology": {
        "check": lambda old: old["phases"]["evaluation"]["accepted"],
        "message": "BLOCKED: Phase 1 (Evaluation) must be accepted before moving to Methodology."
    },
    "components": {
        "check": lambda old: (
            old["phases"]["methodology"]["accepted"]
            and old["phases"]["methodology"]["pattern_accepted"]
            and old["phases"]["methodology"]["components_overview_accepted"]
        ),
        "message": "BLOCKED: Phase 2 (Methodology) — both pattern AND component overview must be accepted."
    },
    "finalization": {
        "check": lambda old: old["phases"]["components"]["all_accepted"],
        "message": "BLOCKED: All components must be accepted before Finalization."
    }
}

VALID_COMPONENT_TRANSITIONS = {
    "pending": ["in_progress"],
    "in_progress": ["awaiting_acceptance"],
    "awaiting_acceptance": ["accepted", "in_progress"],
    "accepted": []
}


def load_current_state():
    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def validate_phase_transition(old_state, new_state):
    old_phase = old_state["current_phase"]
    new_phase = new_state["current_phase"]

    if old_phase == new_phase:
        return True, ""

    if new_phase not in LEGAL_TRANSITIONS.get(old_phase, []):
        return False, (
            f"BLOCKED: Cannot transition from '{old_phase}' to '{new_phase}'. "
            f"Legal transitions from '{old_phase}': {LEGAL_TRANSITIONS.get(old_phase, [])}"
        )

    if new_phase in PREREQUISITES:
        prereq = PREREQUISITES[new_phase]
        try:
            if not prereq["check"](old_state):
                return False, prereq["message"]
        except (KeyError, TypeError) as e:
            return False, f"BLOCKED: Cannot verify prerequisites — state data incomplete: {e}"

    return True, ""


def validate_component_transitions(old_state, new_state):
    old_components = old_state.get("phases", {}).get("components", {}).get("components", {})
    new_components = new_state.get("phases", {}).get("components", {}).get("components", {})

    for comp_name, new_comp in new_components.items():
        new_status = new_comp.get("status", "pending")
        if comp_name in old_components:
            old_status = old_components[comp_name].get("status", "pending")
            if old_status != new_status:
                valid_next = VALID_COMPONENT_TRANSITIONS.get(old_status, [])
                if new_status not in valid_next:
                    return False, (
                        f"BLOCKED: Component '{comp_name}' cannot transition from "
                        f"'{old_status}' to '{new_status}'. Valid transitions: {valid_next}"
                    )

    active_components = [
        name for name, comp in new_components.items()
        if comp.get("status") in ("in_progress", "awaiting_acceptance")
    ]
    if len(active_components) > 1:
        return False, (
            f"BLOCKED: Only one component can be active at a time. "
            f"Active components: {active_components}"
        )

    for comp_name, old_comp in old_components.items():
        if old_comp.get("status") == "accepted":
            new_comp = new_components.get(comp_name, {})
            if new_comp.get("status") != "accepted":
                return False, (
                    f"BLOCKED: Component '{comp_name}' is already accepted "
                    f"and cannot be reverted to '{new_comp.get('status')}'."
                )

    return True, ""


def validate_no_backward_phase(old_state, new_state):
    phase_order = ["not_started", "evaluation", "methodology", "components", "finalization"]
    old_idx = phase_order.index(old_state["current_phase"]) if old_state["current_phase"] in phase_order else -1
    new_idx = phase_order.index(new_state["current_phase"]) if new_state["current_phase"] in phase_order else -1

    if new_idx < old_idx:
        return False, (
            f"BLOCKED: Cannot go backwards from '{old_state['current_phase']}' "
            f"to '{new_state['current_phase']}'. Phase transitions are forward-only."
        )
    return True, ""


def main():
    try:
        proposed_content = sys.stdin.read().strip()
        if not proposed_content:
            sys.exit(0)
        new_state = json.loads(proposed_content)
    except json.JSONDecodeError as e:
        print(f"BLOCKED: Invalid JSON in proposed state: {e}", file=sys.stderr)
        sys.exit(1)

    current_state = load_current_state()
    if current_state is None:
        sys.exit(0)

    if current_state.get("current_phase") == "not_started" and not current_state.get("project_name"):
        sys.exit(0)

    validations = [
        validate_phase_transition,
        validate_no_backward_phase,
        validate_component_transitions,
    ]

    for validation in validations:
        is_valid, message = validation(current_state, new_state)
        if not is_valid:
            print(message, file=sys.stderr)
            print(message)
            sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
