from template import Agent
import random
import sys

class myAgent(Agent):
    def __init__(self,_id):
        super().__init__(_id)
    
    def SelectAction(self,actions,game_state):
        print("before open file")
        with open("agents/example2/test.txt","r") as f:
            print(f.readline())
        print("after open file")
        return random.choice(actions)
