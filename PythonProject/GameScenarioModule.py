import numpy as np
import pylab as plt
import networkx as nx

from AgentModule import Agent

class GameScenario:

    def __init__(self, newEdges, newTargets, probDist, shadowNodes, shadowGroups, newNodesNum, startState, guessReward):
      reversedEdges = []
      for i in range(0, len(newEdges)):
        reversedEdges.append( tuple(reversed(newEdges[i])))
      newEdges.extend(reversedEdges)
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

    def showGraph(self):
      self.pos = nx.shell_layout(self.graph)
      nx.draw_networkx_nodes(self.graph,self.pos, node_color = "Cyan")
      nx.draw_networkx_nodes(self.graph, self.pos, nodelist = self.targets,  node_color = "Purple")
      nx.draw_networkx_nodes(self.graph, self.pos, nodelist = [self.startState],  node_color = "Green")
      nx.draw_networkx_nodes(self.graph, self.pos, nodelist = self.shadowNodes,  node_color = "Grey")
      nx.draw_networkx_edges(self.graph,self.pos)

      nx.draw_networkx_labels(self.graph,self.pos)
      plt.show()

    def refreshGameMatrix(self, target):
      self.matrix = np.matrix(np.ones(shape=(self.nodesNum, self.nodesNum)))
      self.matrix *= -1
      for edge in self.edges:
        if edge[1] == target:
          self.matrix[edge] = 100
        else:
          self.matrix[edge] = 0

        if edge[0] == target:
          self.matrix[edge[::-1]] = 100
        else:
          self.matrix[edge[::-1]] = 0

      #targets connected to each other    
      for edge in self.edges:
        if edge[0] == target and edge[1] == target:
          self.matrix[edge] = 100
          self.matrix[edge[::-1]] = 100
          
      #all goals connect to themselves
      self.matrix[target, target] = 100

     # print (self.matrix)

    #pass current state 
    def get_possible_actions(self, state):
      current_state_row = self.matrix[state,]
      possible_actions = np.where(current_state_row >= 0)[1]
      return possible_actions

    #pass possible actions
    def preview_next_action(self, available_act):
      next_action = int(np.random.choice(available_act,1))
      return next_action

    def train_agent(self, games):
      new_agent = Agent("Bella", False)
      new_agent.generateQTables(self.nodesNum, .8, self.targets)

      for target in self.targets:
        print(target)
        print(self.targets)
        self.refreshGameMatrix(target)

        possible_action = self.get_possible_actions(self.startState)
        action = self.preview_next_action(possible_action)

        new_agent.update(self.startState, action, self.matrix, target)
        scores = []
        for i in range(games):
          current_state = np.random.randint(0, int(new_agent.q_table_dict[target].shape[0]))
          possible_action = self.get_possible_actions(current_state)
          action = self.preview_next_action(possible_action)
          score = new_agent.update(current_state,action,self.matrix, target)
          scores.append(score)
          #print ('Score:', str(score))
        print("Game Matrix")
        print(self.matrix)
        print("Final Trained Q Table:")
        print(new_agent.q_table_dict[target]/np.max(new_agent.q_table_dict[target])*100)

        #test results
        # Testing
        current_state = self.startState
        steps = [current_state]
        q_table = new_agent.q_table_dict[target]
        while current_state != target:
            #print(current_state)
            #print(target)
            next_step_index = np.where(q_table[current_state,] == np.max(q_table[current_state,]))[1]
            if next_step_index.shape[0] > 1:
                next_step_index = int(np.random.choice(next_step_index, size = 1))
            else:
                next_step_index = int(next_step_index)
            steps.append(next_step_index)
            current_state = next_step_index
        print("Most efficient path:")
        print(steps)
        plt.plot(scores)
        plt.show()
      return new_agent