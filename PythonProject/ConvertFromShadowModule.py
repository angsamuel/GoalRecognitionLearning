def shadowToVisible(edges, shadowNodes, shadowGroups, nodesNum):
	for e in edges:
		newEdges = []
		if e[0] not in shadowNodes and e[1] not in shadowNodes: #edge remains the same
			newEdges.append(e)
		elif (e[0] in shadowNodes and e[1] not in shadowNodes) or (e[0] not in shadowNodes and e[1] in shadowNodes):
			#we have an enterence! make new connections for this part of the graph
			entryNode = -1
			if e[0] not in shadowNodes:
				entryNode = e[0]
			else:
				entryNode = e[1]

			


	