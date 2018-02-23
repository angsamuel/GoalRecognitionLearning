import numpy as np
import pylab as plt
import networkx as nx


class Observer:
	def __init__(self, gameScenario):
		self.gs = gameScenario

	def generateQTable(self, newGamma):
		self.gamma = newGamma
	    self.q_table = np.matrix(np.zeros([self.gs.nodesNum,len(self.gs.targets)]))
	
    def update(self, current_state, state, game_matrix, target):
    	max_index = np.where(self.q_table[state,] == np.max(self.q_table[state,]))[1]
        if max_index.shape[0] > 1:
        	max_index = int(np.random.choice(max_index, size = 1))
		else:
        	max_index = int(max_index)
		max_value = self.q_table[state, max_index]
		self.q_table[current_state, action] = game_matrix[current_state, action] + self.gamma * max_value
      #print('max_value', game_matrix[current_state, action] + self.gamma * max_value)
  
      #if (np.max(self.q_table) > 0):
        #return(np.sum(self.q_table_dict[target]/np.max(self.q_table_dict[target])*100))
      #else:
      #  return (0)

	def get_possible_actions(self, state):
      current_state_row = self.q_table[state,]
      possible_actions = np.where(current_state_row >= 0)[1]
      return possible_actions

    def preview_next_action(self, available_act):
      next_action = int(np.random.choice(available_act,1))
      return next_action

    def train_observer(self, games, agent):
