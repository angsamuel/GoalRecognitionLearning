import numpy as np
import pylab as plt
import networkx as nx

from GameScenarioModule import GameScenario
from AgentModule import Agent
from LPHandlerModule import LPHandler

edges = [(0,1),(1,2),(2,3),(3,4),(4,5),(0,6),(6,7),(7,8),(8,9),(9,10),(3,7)]
targets = [5, 10]
probDistribution = [.5, .5]
shadowNodes = [2,3,7,8]
shadowGroups = [[2,3,7,8]]

gs = GameScenario(newEdges = edges, newTargets = targets, 
probDist = probDistribution, shadowNodes = shadowNodes, shadowGroups = shadowGroups,
newNodesNum = 11, startState = 0, guessReward = 10)

gs.showGraph()
#gs.train_agent(2000)

#outer_list = ['one', 'two', 'three']

lph = LPHandler(gs)
lph.WriteLP("test.lp")




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
