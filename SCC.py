import sys
import fileinput

class Vertex:
    def __init__(self, val):
        self.val = val
        self.edges = []
        self.leader = None
        self._mark = 0
        self.markedB = False
    
    def get_value(self):
        return self.val
        
    def add_edge(self, edge):
        self.edges.append( edge )

    def set_leader(self, leader):
        self.leader = leader

    def get_leader(self):
        return self.leader

    def mark(self):
        self._mark += 1

    def get_mark(self):
        return self._mark

    def markV(self):
        self.markedB = True

    def is_marked(self):
        return self.markedB

def depth_first_search_loop_1(vertices, adj_list ): #adj list is a graph from v to outgoing edges

    ordering = []
    random_nums = 0
    
    for v in vertices.values():
        #if v.get_mark() == 0:
        if v.is_marked() == False:
            depth_first_search_1(adj_list, v, ordering)

    return ordering

def depth_first_search_loop_2( adj_list, ordering ): #adj list is a graph from v to outgoing edges
    for v in ordering:
        if v.get_leader() == None:
            depth_first_search_2(adj_list, v, v)


def depth_first_search_1( adj_list, seed, ordering):

    CALLSTACK = [seed]

    while len(CALLSTACK) > 0:
        v = CALLSTACK[-1]
        if v.get_mark() == 0:
            v.mark()
            for ov in adj_list[v]:
                if ov.get_mark() == 0:
                    CALLSTACK.append(ov)

        elif v.get_mark() == 1: #CHANGE TO ELSE?
            ordering.append( CALLSTACK.pop() )
            v.mark()

        else:
            CALLSTACK.pop()

    '''
    seed.markV()
    
    for v in adj_list[seed]:#run DFS
        if v.is_marked() == False:
            depth_first_search_1(adj_list, v, ordering)

    ordering.append( seed )
    '''
    

def depth_first_search_2( adj_list, seed, leader):

    
    CALLSTACK = [seed]

    while len(CALLSTACK) > 0:
        v = CALLSTACK.pop()
        
        v.set_leader(leader)
        
        for ov in adj_list[v]:#run DFS
            if ov.get_leader() == None:
                CALLSTACK.append(ov)
    '''
    seed.set_leader(leader)
    
    for v in adj_list[seed]:#run DFS
        if v.get_leader() == None:
            depth_first_search_2(adj_list, v, leader)
    '''


def make_vertices(edges):
    vertices = []
    for e in edges:
        m = max(e[0], e[1])
        if len(vertices) - 1 < m:
            for i in range(len(vertices), m+1):
                vertices.append( Vertex( i ) )
            
    return vertices

def make_vertices_new(edges):
    vertices = {}
    for e in edges:
        if e[0] not in vertices:
            vertices[ e[0] ] = Vertex( e[0] )

        if e[1] not in vertices:
            vertices[ e[1] ] = Vertex( e[1] )

    return vertices

def make_adj_list(edges, vertices):
    adj_list = {}

    for e in edges:
        v0 = vertices[ e[0] ]
        v1 = vertices[ e[1] ]
         
        if v0 in adj_list:
            adj_list[ v0 ].append( v1 )
        else:
            adj_list[ v0 ] = [ v1 ]

        if v1 not in adj_list:
            adj_list[ v1 ] = []

    return adj_list

def make_adj_list_reverse(edges, vertices):
    adj_list = {}

    for e in edges:
        v0 = vertices[ e[0] ]
        v1 = vertices[ e[1] ]
        
        if v1 in adj_list:
            adj_list[ v1 ].append( v0 )
        else:
            adj_list[ v1 ] = [ v0 ]

        if v0 not in adj_list:
            adj_list[ v0 ] = []

    return adj_list


def find_SCCs():
    sys.setrecursionlimit(2**20)

    edges = []
    with open("SCC.txt", "r") as f:
        counter = 10e10
        for line in f:
            if counter > 0 :
                e = [int(v) for v in line.strip("\n").split(" ") if v!= ""]
                edges.append(e)
                counter -= 1
            else:
                break

            
    print "Done with edges"    
    vertices = make_vertices_new(edges)
    print "Done vertices"
    adj_list = make_adj_list( edges, vertices )
    print "Done reg adj_list"
    adj_list_reverse = make_adj_list_reverse( edges, vertices )
    print "Done adj_list"

    ordering = depth_first_search_loop_1(vertices, adj_list_reverse )[::-1]
    print "Done ordering"

    depth_first_search_loop_2(adj_list, ordering)
    print "Done dfs 2"
    

    scc_member_count = {}
    for v in adj_list:
        l = v.get_leader()
        if l in scc_member_count:
            scc_member_count[l] += 1

        else:
            scc_member_count[l] = 1

    return scc_member_count

print sorted(find_SCCs().values(), reverse=True)[:5]
