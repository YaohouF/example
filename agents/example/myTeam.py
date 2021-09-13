from template import Agent
import random
import sys
import agents.example.test_agent


class myAgent(Agent):
    def __init__(self,_id):
        super().__init__(_id)
    
    def SelectAction(self,actions,game_state):
        print("start calling")
        agents.example.test_agent.testing1()
        print("after calling")
        return random.choice(actions)
