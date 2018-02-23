class LPHandler:
	def __init__(self, gameScenario):
		self.gs = gameScenario

	def WriteLP(self, filePath):
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

						row += "F(" + str(e[0]) + "," + str(gt) + ")"
					row += " - V(" + str(e[1]) + "," + str(t) + ") <= 0"
				else:
					row = "V(" + str(t) + "," + str(t) + ") = 0"
 				file.write(row + "\n")
 		#write f constraints
		for i in range(0, self.gs.nodesNum):
			conRow = ""
			for j in range(0, len(self.gs.targets)):
				conRow += "F(" + str(i) + "," + str(self.gs.targets[j]) + ")"
				if j != len(self.gs.targets) - 1:
					conRow += " + "
			conRow += " = 1"
			file.write(conRow + "\n")
		file.write("bounds\n")
		for i in range(0, self.gs.nodesNum):
			for t in self.gs.targets:
				bfRow = "F(" + str(i) + "," + str(t) + ") >= 0" 
			file.write(bfRow + "\n")
		for i in range(0, self.gs.nodesNum):
			for t in self.gs.targets:
				vFree = "F(" + str(i) + "," + str(t) + ") free" 
			file.write(vFree + "\n")
		file.write("end")
		file.close()
