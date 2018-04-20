def shadowToVisible(edges, shadowNodes, shadowGroups, nodesNum):

	reversedEdges = []

	for i in range(0, len(edges)):
		reversedEdges.append( tuple(reversed(edges[i])))
	edges.extend(reversedEdges)
	edges = list(set(edges))

	print('Call')
	mem_graph = {}
	shadow_edge_groups = []
	shadow_enter_groups = []
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
			#newEdges.append((entryNode,memNode))
			for m in range(0, len(shadowGroups)):
				if shadowNode in shadowGroups[m]:
					shadow_edge_groups[m].append(e)
					shadow_enter_groups[m].append(entryNode)
					shadow_enter_groups[m] = list(set(shadow_enter_groups[m]))
		elif (e[0] in shadowNodes and e[1] in shadowNodes): #adding edge to shadow edge_groups
			for m in range(0, len(shadowGroups)):
				if e[0] in shadowGroups[m]:
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
		#print(shadow_enter_groups)

		for n in shadow_enter_groups[s]:
			#print("node" + str(n))
			connections = []
			for eg in shadow_edge_groups:
				for e in eg:
					#print("edge: " + str(e))
					connection = -1
					if e[0] == n:
						connection = e[1]
					elif e[1] == n:
						connection = e[0]

					if connection != -1:
						#print("adding connection")
						connections.append(connection)
			mem_graph.update({n: connections})

	for n in shadowNodes:
		#print("node" + str(n))
		connections = []
		for eg in shadow_edge_groups:
			for e in eg:
				#print("edge: " + str(e))
				connection = -1
				if e[0] == n:
					connection = e[1]
				elif e[1] == n:
					connection = e[0]

				if connection != -1:
					#print("adding connection")
					connections.append(connection)
		mem_graph.update({n: connections})

	#for each mem, find shortest path, add that many mem nodes
	print(mem_graph)


	for s in range(0, len(shadow_enter_groups)):
		for p in range(0, len(shadow_enter_groups[s])):
			ranges = []
			prim_node = shadow_enter_groups[s][0]
			print("foo")
			newEdges.append( ((  (1000 * (s+1)) +  (100 * (p+1)) + 1), prim_node) )
			print((prim_node,(  (1000 * (s+1)) +  (100 * (p+1)) + 1)) )
			for t in range(1, len(shadow_enter_groups[s])):
				ran = len(find_shortest_path(mem_graph, prim_node, shadow_enter_groups[s][t]))
				ranges.append(ran - 2)
			num_mem_nodes = (max(ranges) - 2)
			prev_node = prim_node
			print("break")
			for x in range(1, num_mem_nodes + 1):
				print((prev_node, (1000 * (s+1)) + (100 * (p + 1)) + x))
				#newEdges.append((prev_node, (1000 * (s+1)) + (100 * (p + 1)) + x))
			for r in range(0,len(ranges)):
				print("change")
				newEdges.append( (  (1000 * (s+1)) + (100*(p+1)) + ranges[r], shadow_enter_groups[s][r+1]))
				print( (  (1000 * (s+1)) + (100*(p+1)) + ranges[r], shadow_enter_groups[s][r+1]) )
			#connect mem_nodes
			for m in range(1,num_mem_nodes + 2):
				print("golf")
				newEdges.append( (  ( (1000*(s+1)) + (100*(p+1)) + m),( (1000 * (s+1)) + (100*(p+1)) + m + 1)) )
				print((  ( (1000*(s+1)) + (100*(p+1)) + m),( (1000 * (s+1)) + (100*(p+1)) + m + 1)) )
			shadow_enter_groups[s].remove(prim_node)
			shadow_enter_groups[s].append(prim_node)
		print(newEdges)
	return list(set(newEdges))




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



	



	