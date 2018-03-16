import numpy as np
import pylab as plt
import networkx as nx

from GameScenarioModule import GameScenario
from AgentModule import Agent
from LPHandlerModule import LPHandler
from ObserverModule import Observer




case = 0
if case == 0:
	edges = [(0,1),(0,2),(1,4),(2,6),(3,7),(4,5),(5,6),(6,13),(13,14),(7,15),(5,11),(10,11),(11,12),(12,13),
	(11,16),(12,17),(10,8),(8,9),(16,20),(17,20),(20,23),(15,23),(16,19),(19,9),(9,18),(18,21),(19,21),(19,22),
	(21,24),(22,24),(24,26),(26,27),(27,28),(28,25),(25,23)]
	targets = [27,10,15,18]
	pDist = [.25,.25,.25,.25]
	shadowNodes = [11,12,16,17,20,21,22,24,26]
	shadowGroups = [[11,12,16,17,20],[21,22,24,26]]
	gs = GameScenario(newEdges = edges, newTargets = targets, probDist = pDist, shadowNodes = shadowNodes, shadowGroups = shadowGroups, newNodesNum = 29,
	startState = 0, guessReward = 1)
	#gs.showGraph()
	#new_agent = gs.train_agent(2000)
	#new_observer = gs.train_observer(2000, new_agent)
	lph = LPHandler(gs)
	lph.WriteLP("withShadow.lp", withShadow = True, withMemory = True)
	lph.WriteLP("noShadow.lp", withShadow = False, withMemory = False)
if case == 1:
	edges = [(0,1),(1,2),(2,3), (3,4), (4,5), (5,6), (6,7), (7,8),(8,13),(13,14),(14,15),(15,16),(16,17),(17,18),(0,9),(9,10),(10,11),(11,12), (3,10)]
	targets = [12, 18]
	pDist = [.5, .5]
	shadowNodes = [2,3,4,5,10]
	shadowGroups = [shadowNodes]
	gs = GameScenario(newEdges = edges, newTargets = targets, probDist = pDist, shadowNodes = shadowNodes, shadowGroups = shadowGroups, newNodesNum = 29,
	startState = 0, guessReward = 1)
	gs.showGraph()
	lph = LPHandler(gs)
	lph.WriteLP("withShadow.lp", withShadow = True, withMemory = False)
	lph.WriteLP("noShadow.lp", withShadow = False, withMemory = False)


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
