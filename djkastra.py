def dijkstra(graph , s):
     heap = [(s,0)]
     paths = {}
     while len(heap) > 0:

         c = True
         v = pop_heap(heap)
         
         while v[0] in paths:
             try:
                  v = pop_heap(heap)
                  
             except:
                  c = False
                  break

         if c == False:
              break
          
         paths[ v[0] ] = v[1]

         if v[0] in graph:
              edges = graph[ v[0] ]
         else:
              edges = []

         for e in edges:
             if e[0] not in paths:
                 heap_add(heap, (e[0], e[1] + v[1]) )
     
     return paths

def heap_add(heap, e):
     heap.append(e)
     ind = len(heap) - 1
     p_ind = (ind - 2 + (ind%2) )/2
     #print ind, p_ind

     v = heap[ind][1]
     p = heap[p_ind][1]
     while (v < p) and (ind != 0):
          swap(heap, ind, p_ind)
          ind = p_ind
          p_ind = (ind - 2 +(ind % 2) )/2
          p = heap[p_ind][1]


def pop_heap(heap):
     swap(heap, 0, -1)

     t = heap.pop()

     downheap(heap)
     return t

def downheap(heap): #left child is 2n+1 right child is 2n+2
     i = 0
     l = len(heap)
     while 2*i + 2 < l :
         lc = heap[2*i + 1][1]
         rc = heap[2*i + 2][1]
         p = heap[i][1]
         
         if (rc < lc) and (rc < p):
             swap(heap, 2*i + 2, i )
             i = 2*i + 2
             
         elif (lc <= rc) and (lc < p):
             swap(heap, 2*i + 1, i)
             i = 2*i + 1
             
         else:
             break

     if (l == 2*i + 2):
          if (heap[i][1] > heap[2*i + 1][1] ):
              swap(heap, 2*i + 1, i)

def swap(arr, i1, i2):
     temp = arr[i1]
     arr[i1] = arr[i2]
     arr[i2] = temp

def loadGraph():
    adj_list = {}
    v = None
    with open("dijkstraData.txt", "r") as f:
        for line in f:
            i = line.split()
            for t in i:
                y = [int(x) for x in t.split(',')]
                if len(y) > 1:
                    if v in adj_list:
                        adj_list[v].append( (y[0], y[1]) )
                    else:    
                        adj_list[v] = [ (y[0], y[1]) ]
                else:
                    v = y[0]
                    
    return adj_list

g = loadGraph()
d = dijkstra(g,1)

a = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
#a = [2,3,4,5]
s = ''
for n in a:
     if n in d:
          print d[n]
          s+= str(d[n]) + ','
     else:
          s+= '1000000,'

print s


