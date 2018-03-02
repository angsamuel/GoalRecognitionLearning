import random
import numpy as np
import pylab as plt
import networkx as nx
import random

class Observer:

  def __init__(self, gameScenario):
    self.gs = gameScenario

  def generateQTable(self, newGamma):
    self.gamma = newGamma
    self.q_table = self.make2dList(self.gs.nodesNum,len(self.gs.targets))#np.matrix(np.zeros([self.gs.nodesNum,len(self.gs.targets)]))

  def make2dList(self, rows, cols):
    a=[]
    for row in xrange(rows): a += [[0]*cols]
    return a

  def get_possible_actions(self, state):
      current_state_row = self.q_table[state,]
      possible_actions = np.where(current_state_row >= 0)[1]
      return possible_actions

  def maxIndex(self, row):
    i = 0
    maxR = row[0]
    maxI = 0
    for r in row:
      if r > maxR:
        maxR = r
        maxI = i
      i += 1
    return maxI

  def train_observer(self, games, agent):
    self.generateQTable(.8)
    scores = []
    for i in range(0,games):
      target_index = random.randint(0,len(self.gs.targets)-1)
      agent_path = agent.path_dict[self.gs.targets[target_index]]
      gameScore = 0
      for s in agent_path:
        guess = self.maxIndex(self.q_table[s])
        if guess == target_index:
          self.q_table[s][guess] += self.gs.guessReward
          gameScore += self.gs.guessReward
        else:
          self.q_table[s][guess] -= self.gs.guessReward
      scores.append(gameScore)
    print("plotting scores")
    plt.plot(scores)
    plt.show()


