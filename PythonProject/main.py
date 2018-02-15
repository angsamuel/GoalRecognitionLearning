import numpy as np
import pylab as plt
import networkx as nx

from GameScenarioModule import GameScenario
from AgentModule import Agent

#edges = [(0,1), (1,5), (5,6), (5,4), (1,2), (2,3), (2,7)]
edges = [(0,1), (0,13), (1,13), (1,2), (2,3), (2,4), (2,14), (3,4), 
(3,16), (4,5), (5,6), (5,8), (5,16), (6,7), (7,8), (7,9), (8,9), (8,11), (9,10),
(10,11),(11,12), (11,15),(12, 13), (15,14)]

targets = [6,10,16]

gs = GameScenario(edges, targets, 17)

gs.showGraph()
gs.train_agent(0, 7, 5000)

outer_list = ['one', 'two', 'three']


