def shadowToVisible(edges, shadowNodes, shadowGroups, nodesNum):
	for e in edges:
		#create new edges to return 
		newEdges = []
		#create index for next memory node
		memNode = 100
		#index of shadow group we're working in
		shadowIndex = -1
		#if the edge has nothing to do with shadow areas then add it to the final group!
		if e[0] not in shadowNodes and e[1] not in shadowNodes: #edge remains the same
			newEdges.append(e)
		#if we found an entrance to the shadow node group, we have work to do
		elif (e[0] in shadowNodes and e[1] not in shadowNodes) or (e[0] not in shadowNodes and e[1] in shadowNodes):
			entryNode = -1
			shadowNode = -1
			if e[0] not in shadowNodes:
				entryNode = e[0]
				shadowNode = e[1]
			else:
				entryNode = e[1]
				shadowNode = e[0]

			newEdges.append((entryNode,memNode))
			#points of exploration
			explorers = []
			#places the exploreres have visited
			visited = []
			#bool added_next_memory = False
			explorers.append(shadowNode)
			#grab the shadow group index we're working with
			for g in range(0, len(self.gs.shadowGroups)):
				if shadowNode in self.gs.shadowGroups[g]:
					shadowIndex = g

			while len(explorers) != 0:
				new_connections = []
				explorer = explorers[0]
				explorers.pop(0)
				steps = []
				for e in self.gs.edges:
					step = -1
					#we have found an edge the explorer connects to
					if e[0] == explorer:
						step = e[1]
					if e[1] == explorer
						step = e[0]
					steps.append(step)

				moved_to_next_mem = False
				
				for s in steps:
					if s in self.gs.shadowGroups[shadowIndex]:
						if !moved_to_next_mem:
							newEdges.append((memNode, memNode + 1))
							moved_to_next_mem = True
							explorers.add(s)
					else:
						newEdges.append((memNode,s))
				















			


	