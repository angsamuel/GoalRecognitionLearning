class LPHandler:
	def __init__(self, gameScenario):
		self.gs = gameScenario
		self.terms = []
		self.nodes = []
		for e in self.gs.edges:
			self.nodes.append(e[0])
			self.nodes.append(e[1])
		self.nodes = list(set(self.nodes))

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
				#print str(e[0]) + " " 
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
								#row += self.makeTerm("F","S" + str(shadowGroupIndex) + "T" + str(i), gt) 
								row += self.makeTerm("F","S" + str(shadowGroupIndex), gt)
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
							conRow += self.makeTerm("F",str("S" + str(shadowGroupIndex)), self.gs.targets[j])
						else:
							conRow += self.makeTerm("F",i,self.gs.targets[j]) 
						if j != len(self.gs.targets) - 1:
							conRow += " + "
					conRow += " = 1"	
					file.write(conRow + "\n")
			# else:
			# 	for j in range(0, len(self.gs.targets)):
			# 		conRow = ""
			# 		for t in self.terms:
			# 			if "F" in t:
			# 				if  "," + str(self.gs.targets[j]) + ")" in t:
			# 					conRow += t

		for n in self.nodes:
			conRow = ""
			shadowGroupIndex = self.getShadowGroupIndex(n)
			if not withShadow or shadowGroupIndex < 0:
				for t in range(0,len(self.gs.targets)):
					conRow += self.makeTerm("F", n, self.gs.targets[t])
					if t != len(self.gs.targets) - 1:
						conRow += " + "
					else:
						conRow += " = 1 "
				file.write(conRow + "\n")


				# 	if shadowGroupIndex > -1 and withShadow:
				# 		conRow += self.makeTerm("F",str("S" + str(shadowGroupIndex)), self.gs.targets[j])
				# 	else:
				# 		conRow += self.makeTerm("F",i,self.gs.targets[j]) 
				# 	if j != len(self.gs.targets) - 1:
				# 		conRow += " + "
				# conRow += " = 1"
				# file.write(conRow + "\n")
		file.write("bounds\n")
		self.terms = list(set(self.terms))
		for t in self.terms:
			if "F" in t:
				file.write(t + " " + " >= 0"  + "\n")
			elif "V" in t:
				file.write(t + " " + " free " + "\n")


	def makeTerm(self, letter, first, second):
		new_term = letter + "(" + str(first) + "," + str(second) + ")"
		self.terms.append(new_term)
		return new_term

	def getShadowGroupIndex(self, node):
		shadowGroupIndex = -1
		for i in range(0, len(self.gs.shadowGroups)):
			if node in self.gs.shadowGroups[i]:
				shadowGroupIndex = i
		return shadowGroupIndex	

