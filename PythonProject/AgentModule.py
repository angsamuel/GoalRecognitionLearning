import numpy as np
import pylab as plt
import networkx as nx
import random

class Agent:
    def __init__(self, name, isSneaky, gameScenario):
      self.name = name
      self.sneaky = isSneaky
      self.gs = gameScenario
      self.state = self.gs.startState

    def generateQTables(self, tableSize, newGamma, targets):
      self.q_table_dict = dict()
      self.path_dict = dict()
      self.gamma = newGamma
      for target in targets:
        q_table = np.matrix(np.zeros([tableSize,tableSize]))
        self.q_table_dict.update({target: q_table})


    def move(self):
      possible_action = self.get_possible_actions(self.state) #look at possible actions
      action = self.preview_next_action(possible_action) #take a possible action
      self.state = action #update state


    def update(self, current_state, action, target):
      max_index = np.where(self.q_table_dict[target][action,] == np.max(self.q_table_dict[target][action,]))[1]
      if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index, size = 1))
      else:
        max_index = int(max_index)
      max_value = self.q_table_dict[target][action, max_index] #max value of next possible move
      self.q_table_dict[target][current_state, action] = self.R[current_state, action] + self.gamma * max_value
  
      if (np.max(self.q_table_dict[target]) > 0):
        return(np.sum(self.q_table_dict[target]/np.max(self.q_table_dict[target])*100))
      else:
        return (0)

    def get_possible_actions(self, state):
      current_state_row = self.R[state,]
      possible_actions = np.where(current_state_row >= 0)[1]
      return possible_actions

    #pass possible actions
    def preview_next_action(self, available_act):
      next_action = int(np.random.choice(available_act,1))
      return next_action

    def refresh_R_table(self, target, utility):
      self.R = np.matrix(np.ones(shape=(self.gs.nodesNum, self.gs.nodesNum)))
      self.R *= -1
      if utility < 0:
        utility = 0
      for edge in self.gs.edges:
        if edge[1] == target:
          self.R[edge] = utility
        else:
          self.R[edge] = 0

        if edge[0] == target:
          self.R[edge[::-1]] = utility
        else:
          self.R[edge[::-1]] = 0

    def get_best_path(self, target):
      return self.path_dict[target]

    def train_agent(self, episodes):
      self.generateQTables(self.gs.nodesNum, .8, self.gs.targets)

      for target in self.gs.targets:
        self.refresh_R_table(target,self.gs.targetUtility)

        possible_action = self.get_possible_actions(self.gs.startState)
        action = self.preview_next_action(possible_action)

        self.update(self.gs.startState, action, target)
        scores = []
        #place agent in a random location, make a move, record results
        for i in range(episodes):
          current_state = np.random.randint(0, int(self.q_table_dict[target].shape[0]))
          possible_action = self.get_possible_actions(current_state)
          action = self.preview_next_action(possible_action)
          score = self.update(current_state,action, target)
          scores.append(score)
          #print ('Score:', str(score))
        #print("Game Matrix")
        #print(self.R)
        #print("Final Trained Q Table:")
        #print(self.q_table_dict[target]/np.max(self.q_table_dict[target])*100)

        # Testing
        current_state = self.gs.startState
        steps = [current_state]
        q_table = self.q_table_dict[target]
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
        self.path_dict.update({target: steps})
        plt.plot(scores)
        plt.show()
      return self
