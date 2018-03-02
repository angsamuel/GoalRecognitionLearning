class LPHandler:
	def __init__(self, gameScenario):
		self.gs = gameScenario

	def WriteLP(self, filePath, withShadow):
		file = open(filePath, "w")
		file.write("maximize\n")
		maximizeLine = ""
		for i in range(0,len(self.gs.probDist)):
			maximizeLine += str(self.gs.probDist[i]) + "V(" + str(self.gs.startState) + ","  
			maximizeLine += str(self.gs.targets[i]) + ")"
			if i != len(self.gs.probDist) - 1:
				maximizeLine += " + "
		file.write(maximizeLine)
		file.write("\nsubject to\n")
		for e in self.gs.edges:
			for t in self.gs.targets:
				row = ""
				if t != e[0]:
					row = "V(" + str(e[0]) + "," + str(t) + ")"
					#add guesses
					for gt in self.gs.targets:
						row +=  " - "
						if gt == t:
							row += str(self.gs.guessReward)
						else:
							row += "0"
						shadowGroupIndex = self.getShadowGroupIndex(e[0])
						if shadowGroupIndex > -1 and withShadow:
							row += "F(" + str("S" + str(shadowGroupIndex)) + "," + str(gt) + ")"
						else:
							row += "F(" + str(e[0]) + "," + str(gt) + ")"
					row += " - V(" + str(e[1]) + "," + str(t) + ") <= 0"
				else:
					row = "V(" + str(t) + "," + str(t) + ") = 0"
 				file.write(row + "\n")
 		#write f constraints
		for i in range(0, self.gs.nodesNum):
			conRow = ""
			shadowGroupIndex = self.getShadowGroupIndex(i)
			for j in range(0, len(self.gs.targets)):
				if shadowGroupIndex > -1 and withShadow:
					conRow += "F(" + str("S" + str(shadowGroupIndex)) + "," + str(self.gs.targets[j]) + ")"
				else:
					conRow += "F(" + str(i) + "," + str(self.gs.targets[j]) + ")"
				if j != len(self.gs.targets) - 1:
					conRow += " + "
			conRow += " = 1"
			file.write(conRow + "\n")
		file.write("bounds\n")
		for i in range(0, self.gs.nodesNum):
			for t in self.gs.targets:
				shadowGroupIndex = self.getShadowGroupIndex(i)
				if shadowGroupIndex > -1 and withShadow:
					bfRow = "F(" + str("S" + str(shadowGroupIndex)) + "," + str(t) + ") >= 0" 
				else:
					bfRow = "F(" + str(i) + "," + str(t) + ") >= 0" 
			file.write(bfRow + "\n")
		for i in range(0, self.gs.nodesNum):
			for t in self.gs.targets:
				vFree = "F(" + str(i) + "," + str(t) + ") free" 
			file.write(vFree + "\n")
		file.write("end")
		file.close()

	def getShadowGroupIndex(self, node):
		shadowGroupIndex = -1
		for i in range(0, len(self.gs.shadowGroups)):
			if node in self.gs.shadowGroups[i]:
				shadowGroupIndex = i
		return shadowGroupIndex	

