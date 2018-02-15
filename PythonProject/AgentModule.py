import numpy as np
import pylab as plt
import networkx as nx


class Agent:
    def __init__(self, name, isSneaky):
    	self.name = name
    	self.sneaky = isSneaky

    def generateQTable(self, tableSize, newGamma):
    	self.q_table = np.matrix(np.zeros([tableSize,tableSize]))
    	self.gamma = newGamma

    def update(self, current_state, action, game_matrix):
      max_index = np.where(self.q_table[action,] == np.max(self.q_table[action,]))[1]
      if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index, size = 1))
      else:
        max_index = int(max_index)
      max_value = self.q_table[action, max_index]
      self.q_table[current_state, action] = game_matrix[current_state, action] + self.gamma * max_value
      #print('max_value', game_matrix[current_state, action] + self.gamma * max_value)
  
      if (np.max(self.q_table) > 0):
        return(np.sum(self.q_table/np.max(self.q_table)*100))
      else:
        return (0)