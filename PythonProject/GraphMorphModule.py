
def convert_graph(edges, shadowNodes, shadowGroups):
	enterences = []
	for e in edges:
		if (e[1] in shadowNodes and e[0] not in shadowNodes) or (e[0] in shadowNodes and e[1] not in shadowNodes):
			enterence.append(e)
			#we have found an enterence node


