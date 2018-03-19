import numpy as np
import pylab as plt
import networkx as nx
import random

class Competition:
	def __init__(self, gameScenario, agent, observer):
		self.agent = agent
		self.observer = observer
		self.gs = gameScenario

	def compete(self, games):
		scores = []
		moves = []
		for i in range(0, games):
			target_index = random.randint(0,len(self.gs.targets)-1)
			target = self.gs.targets[target_index]
			currentUtility = self.gs.targetUtility
			moves_taken = 0
			while self.agent.state != target:
				#Observer guess
				observer_guess = self.observer.guess(self.agent.state, target)

				#Update R table
				if observer_guess == target:
					#it's correct
					currentUtility -= self.gs.guessReward

				self.agent.refresh_R_table( target, currentUtility)
				self.agent.move()
				print("agent state: ", self.agent.state)
				moves_taken+=1
			scores.append(currentUtility)
			moves.append(moves_taken)
		plt.plot(scores)
		plt.show()
		plt.plot(moves)
		plt.show()

