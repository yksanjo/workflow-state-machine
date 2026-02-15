#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import WorkflowStateMachine, State
def main():
    print("Workflow State Machine Demo")
    m = WorkflowStateMachine()
    m.set_state("wf1", State.RUNNING)
    print(f"State: {m.get_state('wf1')}")
    print("Done!")
if __name__ == "__main__": main()
