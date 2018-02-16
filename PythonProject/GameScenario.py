import numpy as np
import pylab as plt
import networkx as nx

class GameScenario:

    def __init__(self, newEdges, newGoals, newNodesNum):
    	self.edges = newEdges
    	self.goals = newGoals
    	self.nodesNum = newNodesNum

    	self.graph = nx.Graph()
    	self.graph.add_edges_from(self.edges)
    	self.pos = nx.spring_layout(self.graph)

   	def showGraph(self):
   		nx.draw_networkx_nodes(self.graph,self.pos)
		  nx.draw_networkx_edges(self.graph,self.pos)
		  nx.draw_networkx_labels(self.graph,self.pos)
		  plt.show()