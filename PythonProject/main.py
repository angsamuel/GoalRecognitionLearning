import numpy as np
import pylab as plt
import networkx as nx
import os

from GameScenarioModule import GameScenario
from AgentModule import Agent
from LPHandlerModule import LPHandler
from ObserverModule import Observer
from CompetitionModule import Competition
from ConvertFromShadowModule import shadowToVisible
from GridMaker import makeGrid

#os.system("glpsol --cpxlp ")
case = 7
if case == 0:
	edges = [(0,1),(0,2),(1,4),(2,6),(3,7),(4,5),(5,6),(6,13),(13,14),(7,15),(5,11),(10,11),(11,12),(12,13),
	(11,16),(12,17),(10,8),(8,9),(16,20),(17,20),(20,23),(15,23),(16,19),(19,9),(9,18),(18,21),(19,21),(19,22),
	(21,24),(22,24),(24,26),(26,27),(27,28),(28,25),(25,23),(14,27),(3,28)]
	targets = [27,10,15,18]
	pDist = [.25,.25,.25,.25]
	shadowNodes = [11,12,16,17,20,21,22,24,26]
	shadowGroups = [[11,12,16,17,20],[21,22,24,26]]
	gs = GameScenario(newEdges = edges, newTargets = targets, probDist = pDist, shadowNodes = shadowNodes, shadowGroups = shadowGroups, newNodesNum = 29,
	startState = 0, guessReward = 1)
	gs.showGraph()

	new_agent = gs.train_agent(2000)
	new_observer = gs.train_observer(20, new_agent)
	new_agent.train_agent_against_observer(3000, new_observer)

	
	lph = LPHandler(gs)
	#lph.WriteLP("withShadow.lp", withShadow = True, withMemory = True)
	lph.WriteLP("noShadow.lp", withShadow = False, withMemory = False)
	strat_dict = lph.get_defender_strat_dict("output.out")
	new_agent.train_agent_LP(2000, strat_dict)
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
	lph.get_defender_strat_dict(fileName="output.out")
if case == 2:
	edges = [(0,1),(0,2),(1,3),(2,4),(3,4),(4,5),(5,6),(6,3),(6,7),(5,8)]
	targets = [7,8]
	pDist = [.5,.5]
	shadowNodes = [3,4,5,6]
	shadowGroups = [[3,4,5,6]]
	gs = GameScenario(newEdges = edges, newTargets = targets, probDist = pDist, shadowNodes = shadowNodes, shadowGroups = shadowGroups, newNodesNum = 29,
	startState = 0, guessReward = 1)
	gs.showGraph()
	shadowToVisible(edges, shadowNodes,shadowGroups, 90)
if case == 3:
	edges = [(0,6),(0,17),(0,16),(6,7),(7,8),(8,2),(2,9),(9,10),(10,11),(11,12),(12,13),(13,4),(17,18),(18,19),
	(19,20),(19,23),(20,21),(21,1),(21,22),(22,23),(23,29),(17,24),(24,25),(25,29),(29,28),(28,27),(27,26),(27,5),
	(16,15),(15,14),(14,4),(28,31),(31,4),(22,30),(30,2),(11,3),(22,32),(32,1),(28,33),(33,5),(10,34),(34,3),(13,35),(35,3)]
	targets = [1,2,3,4,5]
	pDist = [.2,.2,.2,.2]
	shadowNodes = []
	shadowGroups = [shadowNodes]
	gs = GameScenario(newEdges = edges, newTargets = targets, probDist = pDist, shadowNodes = shadowNodes, shadowGroups = shadowGroups, newNodesNum = 36,
	startState = 0, guessReward = 1)
	gs.showGraph()
	new_agent = gs.train_agent(2000)
	

	new_observer = gs.train_observer(50, new_agent)
	new_agent.train_agent_against_observer(3000, new_observer)

	lph = LPHandler(gs)
	#lph.WriteLP("withShadow.lp", withShadow = True, withMemory = True)
	lph.WriteLP("noShadow.lp", withShadow = False, withMemory = False)
	strat_dict = lph.get_defender_strat_dict("output.out")
	new_agent.train_agent_LP(2000, strat_dict)
if case == 4:
	edges = [(0,1),(1,2),(1,3),(2,5),(5,6),(5,4),(4,10),(10,15),(15,18),(18,16),(18,17),(6,11),(11,12),
	(1,3),(3,8),(8,7),(7,13),(13,12),(8,9),(9,14),(14,17)]
	targets = [15,17]
	pDist = [.5,.5]
	shadowNodes = [4,5,6,7,8,9,11,13]
	shadowGroups = [[4,5,6,11],[7,8,9,13]]
	gs = GameScenario(newEdges = edges, newTargets = targets, probDist = pDist, shadowNodes = shadowNodes, shadowGroups = shadowGroups, newNodesNum = 19,
	startState = 0, guessReward = 1)
	gs.showGraph()

	lph = LPHandler(gs)
	lph.WriteLP("withShadow.lp", withShadow = True, withMemory = False)



	edges = [(0,1),(1,2),(1,3),(2,4),(4,7),(7,6),(7,10),(6,13),(13,14),(14,16),(14,15),(15,9),(9,8),(3,5),(5,8),
	(8,12),(12,11),(10,11),(11,16)]
	targets = [15,13]
	pDist = [.5,.5]
	shadowNodes = []
	shadowGroups = [[]]
	gs = GameScenario(newEdges = edges, newTargets = targets, probDist = pDist, shadowNodes = shadowNodes, shadowGroups = shadowGroups, newNodesNum = 17,
	startState = 0, guessReward = 1)
	gs.showGraph()


	new_agent = gs.train_agent(2000)
	new_observer = gs.train_observer(500, new_agent)
	new_agent.train_agent_against_observer(3000, new_observer)

	
	lph = LPHandler(gs)
	
	lph.WriteLP("noShadow.lp", withShadow = False, withMemory = False)
	strat_dict = lph.get_defender_strat_dict("output.out")
	new_agent.train_agent_LP(2000, strat_dict)
	#new_observer = gs.train_observer(50, new_agent)
	#new_agent.train_agent_against_observer(3000, new_observer)
if case == 5:
	print("start")
	edges = [(0,1),(1,2),(2,3),(3,5),(5,4),(2,4),(5,6),(4,7),(0,8),(8,10),(10,9),(9,12),(12,13),(10,13),(12,11),(13,14)]
	shadowNodes = [9,10,12,13,2,3,4,5]
	shadowGroups = [(9,10,13,12),(2,3,4,5)]
	print(shadowToVisible(edges,shadowNodes, shadowGroups, 15))
if case == 6:
	print "case 6"
	edges = [(0,6),(6,11),(11,10),(10,9),(9,8),(8,7),(7,30),(30,15),(15,16),(9,16),(16,17),(30,29),(15,22),(22,1)
	,(1,57),(29,31),(31,32),(32,23),(23,16),(23,24),(17,24),(24,33),(24,25),(31,38),(38,37),(37,57),(37,2),(11,18)
	,(18,19),(19,25),(25,34),(34,40),(34,35),(25,26),(40,3),(3,53),(53,33),(33,39),(39,45),(45,2),(45,46),(46,47)
	,(47,48),(39,40),(40,41),(41,51),(51,58),(58,48),(48,49),(49,50),(50,52),(52,44),(44,43),(43,4),(43,42),(42,35)
	,(42,36),(36,27),(27,21),(21,13),(13,12),(21,20),(20,12),(12,18),(13,14),(14,28),(28,5),(28,27),(5,54),(54,55),(55,56)
	,(56,44),(52,4),(20,26),(42,51),(0,8)]
	targets = [1,2,3,4,5]
	pDist = [.2,.2,.25,.35]
	shadowNodes = [7,30,29,31,32,23,38,12,13,20,21,27,36,42,51,58,48,49,50,41,35,26]
	shadowGroups = [[7,30,29,31,32,23,24,38],[12,13,20,21,27,36,42,51,58,48,49,50,41,35,26]]
	gs = GameScenario(newEdges = edges, newTargets = targets, probDist = pDist, shadowNodes = shadowNodes, shadowGroups = shadowGroups, newNodesNum = 59,
	startState = 0, guessReward = 1)
	gs.showGraph()
	#new_agent = gs.train_agent(2000)
	#new_observer = gs.train_observer(50, new_agent)
	#new_agent.train_agent_against_observer(3000, new_observer)
	lph = LPHandler(gs)
	lph.WriteLP("withShadow.lp", withShadow = True, withMemory = True)
	lph.WriteLP("noShadow.lp", withShadow = False, withMemory = False)
if case == 7: #simple example
	print "case 7"
	edges = [(0,5),(5,6),(4,5),(3,4),(1,3),(6,7),(7,8),(8,2)]
	targets = [1,2]
	pDist = [.75, .25]
	shadowNodes = [4,5,6,7]
	shadowGroups = [ shadowNodes ]

	gs = GameScenario(newEdges = edges, newTargets = targets, probDist = pDist, shadowNodes = shadowNodes, shadowGroups = shadowGroups, newNodesNum = 9,
	startState = 0, guessReward = 1)
	gs.showGraph()

	lph = LPHandler(gs)
	lph.WriteLP("zwithShadow.lp", withShadow = True, withMemory = True)
	lph.WriteLP("znoShadow.lp", withShadow = False, withMemory = False)

	edges = shadowToVisible(edges,shadowNodes,shadowGroups,9)
	shadowNodes = []
	shadowGroups = []
	gs = GameScenario(newEdges = edges, newTargets = targets, probDist = pDist, shadowNodes = shadowNodes, shadowGroups = shadowGroups, newNodesNum = 9,
	startState = 0, guessReward = 1)
	gs.showGraph()
	lph = LPHandler(gs)
	lph.WriteLP("zmem.lp", withShadow = False, withMemory = False)
	os.system("python solvelp.py")
if case == 8:
	edges = [(0,1),(0,2),(1,4),(2,6),(3,7),(4,5),(5,6),(6,13),(13,14),(7,15),(5,11),(10,11),(11,12),(12,13),
	(11,16),(12,17),(10,8),(8,9),(16,20),(17,20),(20,23),(15,23),(16,19),(19,9),(9,18),(18,21),(19,21),(19,22),
	(21,24),(22,24),(24,26),(26,27),(27,28),(28,25),(25,23),(14,27),(3,28)]
	targets = [27,10,15,18]
	pDist = [.25,.25,.25,.25]
	shadowNodes = [11,12,16,17,20,21,22,24,26]
	shadowGroups = [[11,12,16,17,20],[21,22,24,26]]
	gs = GameScenario(newEdges = edges, newTargets = targets, probDist = pDist, shadowNodes = shadowNodes, shadowGroups = shadowGroups, newNodesNum = 29,
	startState = 0, guessReward = 1)
	gs.showGraph()

	
	lph = LPHandler(gs)
	#lph.WriteLP("withShadow.lp", withShadow = True, withMemory = True)
	lph.WriteLP("znoShadow.lp", withShadow = False, withMemory = False)
	lph.WriteLP("zwithShadow.lp", withShadow = True, withMemory = True)


	edges = shadowToVisible(edges, shadowNodes, shadowGroups, 29)
	gs = GameScenario(newEdges = edges, newTargets = targets, probDist = pDist, shadowNodes = [], shadowGroups = [], newNodesNum = 29,
	startState = 0, guessReward = 1)
	gs.showGraph()

	lph = LPHandler(gs)

	lph.WriteLP("zmem.lp", withShadow = False, withMemory = False)
	os.system("python solvelp.py")
if case == 9:
	edges = makeGrid(9,9)
	targets = [0,1,2]
	pDist = [.25,.25,.5]
	available_nodes = [0,1,2,3,4,5,6,7,8,9,13,17,18,22,26,27,31,35,36,37,38,39,40,41,42,43,44,45,49,53,54,58,62,63,67,71,72,73,74,75,76,77,78,79,80]
	#shadowNodes = [10,11,12,  14,15,16,  19,20,21,  23,24,25,  28,29,30, 32,33,34,  46, 47,48,  50,51,52, 55,56,57,  59,60,61,  64, 65,66,  68,69,70]
	#shadowGroups = [[10,11,12,19,20,21,28,29,30], [14,15,16,23,24,25,32,33,34], [46,47,48,55,56,57,64,65,66], [50,51,52,59,60,61,68,69,70]]
	shadowNodes = [20,21,22,23,24,29,30,31,32,33,38,39,40,41,42,47,48,49,50,51,56,57,58,59,60]
	shadowGroups = [[20,21,22,23,24,29,30,31,32,33,38,39,40,41,42,47,48,49,50,51,56,57,58,59,60]]
	edges = shadowToVisible(edges, shadowNodes, shadowGroups, 81)
	
	gs = GameScenario(newEdges = edges, newTargets = targets, probDist = pDist, shadowNodes = [], shadowGroups = [], newNodesNum = 9,
	startState = 4, guessReward = 1)
	print ("showing graph")
	gs.showGraph()
	#optimal no shadow - 2.8
if case == 10:
	edges = makeGrid(5,5)
	targets = [0,1]
	pDist = [.5,.5]
	shadowNodes = [6,7,8,11,12,13,16,17,18]
	shadowGroups = [[6,7,8,11,12,13,16,17,18]]
	edges = shadowToVisible(edges, shadowNodes, shadowGroups, 25)

	gs = GameScenario(newEdges = edges, newTargets = targets, probDist = pDist, shadowNodes = [], shadowGroups = [], newNodesNum = 25,
	startState = 4, guessReward = 1)
	print ("showing graph")
	print edges
	gs.showGraph()


	#3.75 no shadow
	#3.25 fat method
	#





