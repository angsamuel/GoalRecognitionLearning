import numpy as np
import pylab as plt
import networkx as nx


class Agent:
    def __init__(self, name, isSneaky):
    	self.name = name
    	self.sneaky = isSneaky

    def generateQTables(self, tableSize, newGamma, targets):
      self.q_table_dict = dict()
      self.gamma = newGamma
      for target in targets:
        q_table = np.matrix(np.zeros([tableSize,tableSize]))
        self.q_table_dict.update({target: q_table})


    def update(self, current_state, action, game_matrix, target):
      max_index = np.where(self.q_table_dict[target][action,] == np.max(self.q_table_dict[target][action,]))[1]
      if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index, size = 1))
      else:
        max_index = int(max_index)
      max_value = self.q_table_dict[target][action, max_index]
      self.q_table_dict[target][current_state, action] = game_matrix[current_state, action] + self.gamma * max_value
      #print('max_value', game_matrix[current_state, action] + self.gamma * max_value)
  
      if (np.max(self.q_table_dict[target]) > 0):
        return(np.sum(self.q_table_dict[target]/np.max(self.q_table_dict[target])*100))
      else:
        return (0)