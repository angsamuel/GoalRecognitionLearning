class LPHandler:
	def __init__(self, gameScenario):
		self.gs = gameScenario

	def get_defender_strat_dict(self, fileName):
		lines = []
		strat_dict = dict()
		with open(fileName) as f:
			for line in f:
				if "F(" in line:
					strat = line[25 : 42].translate(None, ' ')
					f_guts = line.split("F(")[1].split(")")[0] .split(",")
					location = int(f_guts[0])
					guess = int(f_guts[1])
					strat_dict.update({(location,guess): strat})
		return strat_dict

	def WriteLP(self, filePath, withShadow, withMemory):
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
		#write rows
		for e in self.gs.edges:
			for t in self.gs.targets:
				shadowGroupIndex = self.getShadowGroupIndex(e[0])
				if withMemory and shadowGroupIndex > -1:
					for i in range(0, len(self.gs.shadowGroups[shadowGroupIndex])):
						row = ""
						if t != e[0]:
							row = self.makeTerm("V", e[0], t)
							#add guesses
							for gt in self.gs.targets:
								row +=  " - "
								if gt == t:
									row += str(self.gs.guessReward)
								else:
									row += "0"
								row += self.makeTerm("F","S" + str(shadowGroupIndex) + "T" + str(i), gt) 
							row += " - " + self.makeTerm("V", e[1], t) + " <= 0" 
						else:
							row = self.makeTerm("V", t, t) + " = 0"
		 				file.write(row + "\n")
				else:
					row = ""
					if t != e[0]:
						row = self.makeTerm("V", e[0], t) 
						#add guesses
						for gt in self.gs.targets:
							row +=  " - "
							if gt == t:
								row += str(self.gs.guessReward)
							else:
								row += "0"
							if shadowGroupIndex > -1 and withShadow:
								row += self.makeTerm("F","S" + str(shadowGroupIndex), gt) 
							else:
								row += self.makeTerm("F", e[0], gt) 
						row += " - " + self.makeTerm("V", e[1], t) + " <= 0" 
					else:
						row = self.makeTerm("V", t, t) + " = 0" 
	 				file.write(row + "\n")
 		#write f constraints
		for i in range(0, self.gs.nodesNum):
			conRow = ""
			shadowGroupIndex = self.getShadowGroupIndex(i)
			if shadowGroupIndex > -1 and withMemory:
				for m in range(0, len(self.gs.shadowGroups[shadowGroupIndex])):
					conRow = ""
					for j in range(0, len(self.gs.targets)):
						if shadowGroupIndex > -1 and withShadow:
							conRow += self.makeTerm("F",str("S" + str(shadowGroupIndex)) + "T" + str(m), self.gs.targets[j])
						else:
							conRow += self.makeTerm("F",i,self.gs.targets[j]) 
						if j != len(self.gs.targets) - 1:
							conRow += " + "
					conRow += " = 1"	
					file.write(conRow + "\n")
			else:
				for j in range(0, len(self.gs.targets)):
					if shadowGroupIndex > -1 and withShadow:
						conRow += self.makeTerm("F",str("S" + str(shadowGroupIndex)), self.gs.targets[j])
					else:
						conRow += self.makeTerm("F",i,self.gs.targets[j]) 
					if j != len(self.gs.targets) - 1:
						conRow += " + "
				conRow += " = 1"
				file.write(conRow + "\n")
		file.write("bounds\n")
		for i in range(0, self.gs.nodesNum):
			for t in self.gs.targets:
				shadowGroupIndex = self.getShadowGroupIndex(i)
				bfRow = ""
				if withMemory and shadowGroupIndex > -1:
					for m in range(0, len(self.gs.shadowGroups[shadowGroupIndex])):
						bfRow = self.makeTerm("F",str("S" + str(shadowGroupIndex) + "T" + str(m)),t) + " >= 0"
						file.write(bfRow + "\n")
				elif shadowGroupIndex > -1 and withShadow:
					bfRow = self.makeTerm("F",str("S" + str(shadowGroupIndex)),t) + " >= 0" #"#"F(" + str("S" + str(shadowGroupIndex)) + "," + str(t) + ") >= 0" 	
				else:
					bfRow = self.makeTerm("F", i,t) + " >= 0" 
				if not withMemory:	
					file.write(bfRow + "\n")
		for i in range(0, self.gs.nodesNum):
			for t in self.gs.targets:
				vFree = self.makeTerm("V", i, t) + " free" 
			file.write(vFree + "\n")
		file.write("end")
		file.close()

	def makeTerm(self, letter, first, second):
		return letter + "(" + str(first) + "," + str(second) + ")"

	def getShadowGroupIndex(self, node):
		shadowGroupIndex = -1
		for i in range(0, len(self.gs.shadowGroups)):
			if node in self.gs.shadowGroups[i]:
				shadowGroupIndex = i
		return shadowGroupIndex	

