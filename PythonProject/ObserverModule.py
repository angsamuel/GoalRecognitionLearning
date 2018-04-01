import random
import numpy as np
import pylab as plt
import networkx as nx
import random

class Observer:

  def __init__(self, gameScenario):
    self.gs = gameScenario
    self.belief = gameScenario.probDist
    #print(self.belief)

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

  def reset_belief(self):
     self.belief = []
     for p in self.gs.probDist:
      self.belief.append(p)
     #print("prob dist ", self.gs.probDist)

  def update_belief(self, state):
    #print("initial belief",self.belief)

    possible_actions = self.q_table[state]
    action_sum = 0.0
    for g in possible_actions:
      action_sum += g

    #print("observations", possible_actions)
    for b in range(0, len(self.belief)):
      #print("math", self.belief[b], (possible_actions[b] / action_sum), (self.belief[b] * (possible_actions[b] / action_sum)))
      if action_sum > 0:
        self.belief[b] = (self.belief[b] * ((float(possible_actions[b])) / action_sum))
    #print("final belief", self.belief)

  def belief_guess(self):
    #print(self.belief)
    max_belief = 0
    max_belief_index = 0
    for b in range(0, len(self.belief)):
      if self.belief[b] > max_belief: 
        max_belief = self.belief[b]
        max_belief_index = b
    return self.gs.targets[max_belief_index]


  def guess(self, state, target):
    guess = self.maxIndex(self.q_table[state])
    self.q_table[state][target] += self.gs.guessReward
    return self.gs.targets[guess]

  def refresh_R_table(self, target, utility):
    self.R = np.matrix(np.ones(shape=(self.gs.nodesNum, self.gs.nodesNum)))
    self.R *= -1
    for edge in self.gs.edges:
      if edge[1] == target:
        self.R[edge] = utility
      else:
        self.R[edge] = 0

      if edge[0] == target:
        self.R[edge[::-1]] = utility
      else:
        self.R[edge[::-1]] = 0

  def train_observer(self, games, agent):
    self.generateQTable(.8)
    scores = []
    for i in range(0,games):
      target_index = random.randint(0,len(self.gs.targets)-1)
      agent_path = agent.path_dict[self.gs.targets[target_index]]
      gameScore = 0
      for s in agent_path:
        self.q_table[s][target_index] += 1
        #guess = self.maxIndex(self.q_table[s])

  def observe_action(self, location, target):
    target_index = 0
    for t in range(0,len(self.gs.targets)):
      if self.gs.targets[t] == target:
        target_index = t
    self.q_table[location][target_index] += 1



