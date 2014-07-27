def load_data():
    edges = []
    leaders = {}
    with open("clusteringData.txt", "r") as f:
        firstline = True
        for line in f:
            if firstline:
                firstline = False
            else:
                new_edge = [int(n) for n in line.strip().split(" ")]
                edges.append( new_edge )
                
                e0 = new_edge[0]
                e1 = new_edge[1]
                if leaders.has_key(e0) == False:
                    leaders[ e0 ] = e0
                if leaders.has_key(e1) == False: 
                    leaders[ e1 ] = e1
            
    edges = sorted(edges, key=lambda x:x[2]) #need to sort by the third p
    
    return edges, leaders

e,l = load_data()

def cluster(edges, leaders, clusters):
    c = 0
    l_keys = leaders.keys()
    clusters = len (leaders.values() )
    

    while clusters > 4:
        leader0 = edges[c][0]
        leader1 = edges[c][1]

        if leaders[ leader0 ] != leaders[ leader1 ]:
            first_group = []
            second_group = []
            for k in l_keys:
                if leaders[ k ] == leaders[edges[c][0]]:
                    first_group.append(k)
                elif leaders[ k ] == leaders[edges[c][1]]:
                    second_group.append(k)

            if len(first_group) < len(second_group):
                for v in first_group:
                    leaders[v] = leaders[ leader1 ]
                    
            else:
                for v in second_group:
                    leaders[v] = leaders[ leader0 ]

            #print first_group, second_group
                    
            clusters = clusters - 1
                    
            
        c = c + 1


    l0, l1 = leaders[edges[c][0]], leaders[edges[c][1]]
    while l0 == l1:
        c = c + 1
        l0, l1 = leaders[edges[c][0]], leaders[edges[c][1]]
   
    print edges[c][2]

#edges, leaders = load_data()
#cluster(edges, leaders, 4)
    
    
    
def load_data2():
	leaders = {}
	groups = {}

	with open("clustering_big.txt",'r') as f:
		firstline = True
		for line in f:
			if firstline:
				firstline = False
			else:
				d = line.strip().replace(' ', '')
				leaders[ d ] = d
				groups[d] = [d] 

	return leaders, groups

def solve_problem(leaders, groups): # Min number of clusters, s.t all vertices of distance <=2 are in the same cluster
	keys = leaders.keys()
	for v in keys: # leaders maps each vertex to its leader
		for h in generate_Ham2(v):
			if leaders.has_key(h) and leaders[h] != leaders[v]:
			
				lh = leaders[h]
				lv = leaders[v]	
				gv = groups[lv]
				gh = groups[lh]
				if len(gh) > len(gv):
					for vertex in gv:
						leaders[vertex] = lh
					groups[lh].extend(gv)
					del groups[lv]

				else:
					for vertex in gh:
						leaders[vertex] = lv
					groups[lv].extend(gh)
					del groups[lh]

	print len(groups.keys())

def invert_indices(lis, s): # to make this faster use int representations
	t = ''
	for i in range(len(s)):
		if i in lis:
			if s[i] == '0':
				t = t + "1"
			else:
				t = t + "0"

		else:
			t = t + s[i]

	return t

def generate_Ham2(v):
	l = len(v)

	for i in range(l):
		t = invert_indices([i], v)
		yield t

	for i in range(l-1): # specific case 2 of n choose 2
		for j in range(i+1,l):
			t = invert_indices([i,j], v)
			yield t

leaders, groups = load_data2()
solve_problem( leaders, groups )