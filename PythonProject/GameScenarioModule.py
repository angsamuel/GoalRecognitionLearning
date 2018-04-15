import numpy as np
import pylab as plt
import networkx as nx

from AgentModule import Agent
from ObserverModule import Observer

#Sonia Riales, assign ticket, Eduction-Red
#ask what she was trying to print
#Sonia Mireles, Storch, 223, Transcript

class GameScenario:

    def __init__(self, newEdges, newTargets, probDist, shadowNodes, shadowGroups, newNodesNum, startState, guessReward):
      reversedEdges = []
      for i in range(0, len(newEdges)):
        reversedEdges.append( tuple(reversed(newEdges[i])))
      newEdges.extend(reversedEdges)
      newEdges = list(set(newEdges))
      self.edges = newEdges
      self.shadowNodes = shadowNodes
      self.shadowGroups = shadowGroups
      self.targets = newTargets
      self.nodesNum = newNodesNum
      self.graph = nx.Graph()
      self.graph.add_edges_from(self.edges)
      self.startState = startState
      self.probDist = probDist
      self.guessReward = guessReward
      self.targetUtility = 10

    def showGraph(self):
      self.pos = nx.spring_layout(self.graph)
      nx.draw_networkx_nodes(self.graph,self.pos, node_color = "Cyan")
      nx.draw_networkx_nodes(self.graph, self.pos, nodelist = self.targets,  node_color = "Purple")
      nx.draw_networkx_nodes(self.graph, self.pos, nodelist = [self.startState],  node_color = "Green")
      nx.draw_networkx_nodes(self.graph, self.pos, nodelist = self.shadowNodes,  node_color = "Grey")
      nx.draw_networkx_edges(self.graph,self.pos)

      nx.draw_networkx_labels(self.graph,self.pos)
      plt.show()

     # print (self.matrix)
    def train_agent(self, games):
      new_agent = Agent("Bella", False, self)
      new_agent.train_agent(games)
      return new_agent

    def train_observer(self, games, agent):
      new_observer = Observer(self)
      new_observer.train_observer(games, agent)
      return new_observer

#pomdp
#policy gradient algorithm
#playing two agents against each other to see if they converge, 
#useful for defender to play mixed strategy, value of policy is
#a function given mixed strategy
#mapping from belief/history into action