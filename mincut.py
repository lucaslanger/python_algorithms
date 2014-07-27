from random import randint,choice

class UnionFind(object):
    def __init__(self):
        self.leader = {}
        self.group = {}

    def makeSet(self, elements):

        assert type(elements) is list

        group = set(elements)
        self.group[elements[0]] = group
        for i in group:
            self.leader[i] = elements[0]

    def find(self, element):
        return self.leader[element]

    def union(self, element1, element2):
        
        leader1 = self.leader[element1]
        leader2 = self.leader[element2]
        
        if leader1 != leader2:
            group1 = self.group[leader1]
            group2 = self.group[leader2]
        else:
            return
        
        if len(group1) < len(group2):
            element1,leader1,group1,element2,leader2,group2 = element2,leader2,group2,element1,leader1,group1
        
        group1 |= group2
        del self.group[leader2]
        for i in group2:
            self.leader[i] = leader1

    def getGroups(self):
        return group

    def getNumGroups(self):
        return len(self.group)

    def printLeaders(self):
        print self.leader

def minCut(graph):
    UF = UnionFind()
    edges = constructData(graph,UF)
    #UF.printLeaders()

    while UF.getNumGroups() > 2:
        lastindex = len(edges) - 1
        r_ind = randint(0, lastindex )
        swap(edges, r_ind, lastindex )

        edge_to_contract = edges[lastindex]
        #print edge_to_contract
        UF.union(edge_to_contract[0], edge_to_contract[1] )

        edges.pop()

    ce = kill_self_loops(UF,edges)
    return len(ce)
        
def kill_self_loops(uf,edges):
    crossing_edges = []
    for e in edges:
        if uf.find(e[0]) != uf.find(e[1]):
            crossing_edges.append(e)
    return crossing_edges

def swap(li, i1, i2):
    temp = li[i1]
    li[i1] = li[i2]
    li[i2] = temp
   
def constructData(graph, uf):
    dupl = {}
    edges = []

    for k in graph:
            for t in graph[k]:
                    if dupl.has_key(t) == False:
                        dupl[k] = t
                        edges.append([k,t] )
            uf.makeSet([k])
            
    return edges

def fileToGraph(s):
	g = {}
	with open(s,"r") as f:
		for l in f.readlines():
			ls = l.strip("\n")
			entries = [int(e) for e in ls.split("\t") if e != ""]
			g[ int(entries[0]) ] = entries[1:]
	return g

def test():
	testgraph = fileToGraph("kargerMinCut.txt")
	best = None
	for i in range(1000):
		mc = minCut(testgraph)
		if best == None or mc < best:
			best = mc

	print best

test()
