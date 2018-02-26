import numpy as np
import pylab as plt
import networkx as nx


class Observer:

  def __init__(self, gameScenario):
    self.gs = gameScenario

  def generateQTable(self, newGamma):
    self.gamma = newGamma
    self.q_table = np.matrix(np.zeros([self.gs.nodesNum,len(self.gs.targets)]))
	
  def update(self, current_state, action, game_matrix):
    if action == self.gs.targets[0]:
      game_matrix[current_state, action] += self.gs.guessReward
      return self.gs.guessReward
    else:
      return 0
      #print('max_value', game_matrix[current_state, action] + self.gamma * max_value)
  
      #if (np.max(self.q_table) > 0):
        #return(np.sum(self.q_table_dict[target]/np.max(self.q_table_dict[target])*100))
      #else:
      #  return (0)

  def refreshGameMatrix(self):
      self.matrix = np.matrix(np.zeros(shape=(self.gs.nodesNum, self.gs.nodesNum)))
  
  def get_possible_actions(self, state):
      current_state_row = self.q_table[state,]
      possible_actions = np.where(current_state_row >= 0)[1]
      return possible_actions
  
  def preview_next_action(self, available_act):
      next_action = int(np.random.choice(available_act,1))
      return next_action
  
  def train_observer(self, games, agent):
      self.generateQTable(.8)
      self.refreshGameMatrix()
      possible_action = self.get_possible_actions(self.gs.startState)
      action = self.preview_next_action(possible_action)

      self.update(self.gs.startState, action, self.matrix)
      scores = []
      for i in range(games):
        game_matrix = self.matrix
        agent_path = agent.get_best_path(self.gs.targets[0])
        for p in agent_path:
          if p != self.gs.targets[0]:
            current_state = p
            possible_action = self.get_possible_actions(current_state)
            action = self.preview_next_action(possible_action)
            score = self.update(current_state,action,game_matrix)
            scores.append(score)
        self.matrix = game_matrix

      #take a path from the agent and play it
#Irma as Sociology
#0420584

#Trinity Student Tmail account,
#Belinda Henning
#maple one computer in there

#mars mclean 22
