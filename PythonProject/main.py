import numpy as np
import pylab as plt
import networkx as nx

from GameScenarioModule import GameScenario
from AgentModule import Agent

#edges = [(0,1), (1,5), (5,6), (5,4), (1,2), (2,3), (2,7)]
edges = [(0,1), (0,13), (1,13), (1,2), (2,3), (2,4), (2,14), (3,4), 
(3,16), (4,5), (5,6), (5,8), (5,16), (6,7), (7,8), (7,9), (8,9), (8,11), (9,10),
(10,11),(11,12), (11,15),(12, 13), (15,14)]

targets = [6, 10, 16, 15]

gs = GameScenario(edges, targets, 17, 0)

gs.showGraph()
gs.train_agent(2000)

outer_list = ['one', 'two', 'three']

#partially observable mdp
#fi(s) now uses the same s for all states belonging to non observable portion of the graph
#keep track of how many steps since we saw attacker
#multi agent reinforcement learning

#modify linear program
#finish observer q-learning
#look into different types of agents
#discrete non-observable graph
#multi agent reinforcement learning stochastic games 
#multi agent reinforcement learning check google scholar8;;pklljkl;wawsedr
