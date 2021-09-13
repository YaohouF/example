from template import Agent
import random
import sys
sys.path.append('agents/agent1/')
import test_agent


class myAgent(Agent):
    def __init__(self,_id):
        super().__init__(_id)
    
    def SelectAction(self,actions,game_state):
        print("testing")
        test_agent.testing1()
        print("after")
        return random.choice(actions)
