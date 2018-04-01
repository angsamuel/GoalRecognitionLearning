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
		score_dict = dict()
		move_dict = dict()
		for t in self.gs.targets:
			score_dict.update({t: []})
			move_dict.update({t: []})

		for i in range(0, games):
			target_index = random.randint(0,len(self.gs.targets)-1)
			target = self.gs.targets[target_index]
			currentUtility = self.gs.targetUtility
			moves_taken = 0
			self.agent.state = self.gs.startState
			while self.agent.state != target:
				#Observer guess
				observer_guess = self.observer.guess(self.agent.state, target)

				#Update R table
				if observer_guess == target:
					#it's correct
					currentUtility -= self.gs.guessReward

				self.agent.refresh_R_table( target, currentUtility)
				self.agent.move(target)
				#print("agent state: ", self.agent.state)
				moves_taken = moves_taken + 1
			score_dict[target].append(currentUtility)
			move_dict[target].append(moves_taken)

			#score_dict.update({target: score_dict[target].append(currentUtility)})
			#move_dict.update({target: move_dict[target].append(moves_taken)})
		for t in self.gs.targets:
			print("printing agent score on target " + str(t))
			plt.plot(score_dict[t])
			plt.show()
			plt.plot(move_dict[t])
			plt.show()
