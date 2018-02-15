import numpy as np
import pylab as plt
import networkx as nx

from AgentModule import Agent

class GameScenario:

    def __init__(self, newEdges, newTargets, newNodesNum):
      self.edges = newEdges
      self.targets = newTargets
      self.nodesNum = newNodesNum
      self.graph = nx.Graph()
      self.graph.add_edges_from(self.edges)
      self.pos = nx.spring_layout(self.graph)
      self.refreshGameMatrix()
      self.count = 1

    def showGraph(self):
      nx.draw_networkx_nodes(self.graph,self.pos)
      nx.draw_networkx_edges(self.graph,self.pos)
      nx.draw_networkx_labels(self.graph,self.pos)
      plt.show()

    def refreshGameMatrix(self):
      self.matrixDict = dict()
      self.matrix = np.matrix(np.ones(shape=(self.nodesNum, self.nodesNum)))
      self.matrix *= -1
      for edge in self.edges:
        if edge[1] in self.targets:
          self.matrix[edge] = 100
        else:
          self.matrix[edge] = 0

        if edge[0] in self.targets:
          self.matrix[edge[::-1]] = 100
        else:
          self.matrix[edge[::-1]] = 0

      #targets connected to each other    
      for edge in self.edges:
        if edge[0] in self.targets and edge[1] in self.targets:
          self.matrix[edge] = 100
          self.matrix[edge[::-1]] = 100
          
      #all goals connect to themselves
      for target in self.targets:
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

    def train_agent(self, start_state, goal_state, games):
      new_agent = Agent("Bella", False)
      new_agent.generateQTable(self.nodesNum, .8)

      initial_state = 1
      possible_action = self.get_possible_actions(initial_state)
      action = self.preview_next_action(possible_action)
      new_agent.update(initial_state, action, self.matrix)


      scores = []
      for i in range(games):
        current_state = np.random.randint(0, int(new_agent.q_table.shape[0]))
        possible_action = self.get_possible_actions(current_state)
        action = self.preview_next_action(possible_action)
        score = new_agent.update(current_state,action,self.matrix)
        scores.append(score)
        #print ('Score:', str(score))
      print("Game Matrix")
      print(self.matrix)
      print("Final Trained Q Table:")
      print(new_agent.q_table/np.max(new_agent.q_table)*100)

      #test results
      # Testing
      current_state = start_state
      steps = [current_state]
      q_table = new_agent.q_table
      while current_state != goal_state:
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