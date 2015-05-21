from graph import *


def isNeighbour(name1, name2): 
	# check if two nodes are neighbours
	
	for ind in range(len(name1)-1):
		if name1[ind] != name2[ind]:
			if name1[ind] == name2[ind+1] and name1[ind+1] == name2[ind]:
				return True

	return False


def make_graph():
	nodes = []
	nodes.append(Node("ABC")) # nodes[0]
	nodes.append(Node("ACB")) # nodes[1]
	nodes.append(Node("BAC")) # nodes[2]
	nodes.append(Node("BCA")) # nodes[3]
	nodes.append(Node("CAB")) # nodes[4]
	nodes.append(Node("CBA")) # nodes[5]
	nodes.append(Node("ABC")) # nodes[5]

	g = Graph()
	for n in nodes:
		print n, "is created"
		g.addNode(n)

	edges = []
	for sourceN_ind in range(len(nodes)):
		for destN_ind in range(sourceN_ind+1, len(nodes)):
			if isNeighbour(nodes[sourceN_ind].getName(), nodes[destN_ind].getName()):
				edges.append(Edge(nodes[sourceN_ind], nodes[destN_ind]))
				#print Edge(nodes[sourceN_ind], nodes[destN_ind])
				

	for edge in edges:
		g.addEdge(edge)

	return g

def DFS(g, start, end, path = []):
	#Depth First Search
	path = path + [start]

	if start == end:
		return path

	for node in g.childrenOf(start):
		print node.getName()
		if node not in path:
			newpath = DFS(g, node, end, path)
			if newpath:
				return newpath



	return None

if __name__ == "__main__":

	g = make_graph()
	
	#print g.childrenOf(Node("ABC"))
	#path = DFS(g, Node("ABC"), Node("BAC"))
	
	#print path
	#print [child.getName() for child in g.childrenOf(Node("ABC"))]
	g.addNode(Node("ABC"))
	g.addNode(Node("ABC"))
	print [[node.getName()] for node in g.nodes]
	print Node("ABC") in [[node] for node in g.nodes]
	print Node("ABC")
	g.addNode(Node("ABDC"))