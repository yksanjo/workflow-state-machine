"""Workflow State Machine - State machine for workflows."""
from enum import Enum
from typing import Dict, Set

class State(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

class WorkflowStateMachine:
    def __init__(self):
        self.states: Dict[str, State] = {}
        self.transitions: Dict[State, Set[State]] = {
            State.PENDING: {State.RUNNING},
            State.RUNNING: {State.COMPLETED, State.FAILED},
            State.COMPLETED: set(),
            State.FAILED: {State.PENDING}
        }
    
    def set_state(self, workflow_id: str, state: State) -> bool:
        current = self.states.get(workflow_id, State.PENDING)
        if state in self.transitions.get(current, set()):
            self.states[workflow_id] = state
            return True
        return False
    
    def get_state(self, workflow_id: str) -> State:
        return self.states.get(workflow_id, State.PENDING)

__all__ = ["WorkflowStateMachine", "State"]
