def makeGrid(width, height):
	edges = []
	for i in range(0, width*height):
		if (i+1) % width != 0:
			edges.append((i,i+1))
			print (i + 1, width, i+1 % width)
		if i >= width:
			edges.append((i, i-width))
	return edges
