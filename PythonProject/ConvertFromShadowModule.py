def shadowToVisible(edges, shadowNodes, shadowGroups, nodesNum):
	mem_graph = {}
	shadow_edge_groups = []
	shadow_enterence_groups = []
	memNode = 100
	newEdges = []
	for i in range(0, len(shadowGroups)):
		shadow_edge_groups.append( [] )
		shadow_enter_groups.append( [] )

	for e in edges:
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
			for m in range(0, len(shadowGroups)):
				if shadowNode in shadowNodes[m]:
					shadow_edge_groups[m].append(e)
					shadow_enter_groups.append(entryNode)
		elif (e[0] in shadowNodes and e[1] in shadowNodes): #adding edge to shadow edge_groups
			for m in range(0, len(shadowGroups)):
				if e[0] in shadowNodes[m]:
					shadow_edge_groups[m].append(e)

	for s in range(0, len(shadowGroups)):
		#add all connections for each shadow node
		for n in shadowGroups[s]:
			connections = []
			for e in shadow_edge_groups:
				connection = -1
				if e[0] == n:
					connection = e[1]
				elif e[1] == n:
					connection = e[0]

				if connection != -1:
					connections.append(connection)
			mem_graph.update({n: connections})

		#add all connections for each shadow entrance node
		for n in shadow_enter_groups[s]
			connections = []
			for e in shadow_edge_groups:
				connection = -1
				if e[0] == n:
					connection = e[1]
				elif e[1] == n:
					connection = e[0]

				if connection != -1:
					connections.append(connection)
				mem_graph.update({n: connections})

	#for each mem, find shortest path, add that many mem nodes
	for s in range(0, len(shadow_enter_groups)):
		ranges = []
		prim_node = shadow_enter_groups[s][0]
		for t in range(1, len(shadow_enter_groups[s])):
			ran = find_shortest_path(mem_graph, prim_node, shadow_enter_groups[s][t])
			ranges.append(ran - 2)
		num_mem_nodes = (max(ranges) - 2)
		prev_node = prim_node
		for x in range(0, num_mem_nodes):
			newEdges.append((prev_node, (100 * (s + 1)) + x))
		for r in range(0,len(ranges)):
			newEdges.append( ((100*(s+1)) + ranges[r], shadow_enter_groups[s][r+1]))






def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest



	



	