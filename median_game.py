def problem2():
     running_total = 0
     maxheap = []
     minheap = []

     with open("a6P2Data.txt","r") as f:
          for line in f:
               n_m = getNewMedian(maxheap, minheap, int(line) )
               running_total += n_m

     print running_total % 10000
               

def getNewMedian(h1, h2, n): #h1 is max heap, h2 is min heap
     if len(h1) == len(h2):
          if len(h1)==0 or h1[0] >= n:
               heap_add_max(h1, n)

          else:
               heap_add_min(h2, n)
               swap(h2, 0, -1)
               heap_add_max(h1, h2.pop())
               downheap_min(h2)

     else: # by construction len(h2) < len (h1)
          assert(len(h2) < len(h1) )
          if len(h1) == 0 or h1[0] <= n:
               heap_add_min(h2, n)
          else:
               heap_add_max(h1, n)
               swap(h1, 0, -1)
               heap_add_min(h2, h1.pop() )
               downheap_max(h1)
               
     return h1[0]

def swap(a, i1, i2):
     tmp = a[i1]
     a[i1] = a[i2]
     a[i2] = tmp

def heap_add_min(heap, e):
     heap.append(e)
     ind = len(heap) - 1
     p_ind = (ind - 2 + (ind%2) )/2
     #print ind, p_ind

     v = heap[ind]
     p = heap[p_ind]
     while (v < p) and (ind != 0):
          swap(heap, ind, p_ind)
          ind = p_ind
          p_ind = (ind - 2 +(ind % 2) )/2
          p = heap[p_ind]

def heap_add_max(heap, e):
     heap.append(e)
     ind = len(heap) - 1
     p_ind = (ind - 2 + (ind%2) )/2
     #print ind, p_ind

     v = heap[ind]
     p = heap[p_ind]
     while (v > p) and (ind != 0):
          swap(heap, ind, p_ind)
          ind = p_ind
          p_ind = (ind - 2 +(ind % 2) )/2
          p = heap[p_ind]


def downheap_min(heap): #left child is 2n+1 right child is 2n+2
     i = 0
     l = len(heap)
     while 2*i + 2 < l :
         lc = heap[2*i + 1]
         rc = heap[2*i + 2]
         p = heap[i]
         
         if (rc < lc) and (rc < p):
             swap(heap, 2*i + 2, i )
             i = 2*i + 2
             
         elif (lc <= rc) and (lc < p):
             swap(heap, 2*i + 1, i)
             i = 2*i + 1
             
         else:
             break

     if (l == 2*i + 2):
          if (heap[i] > heap[2*i + 1] ):
              swap(heap, 2*i + 1, i)


def downheap_max(heap): #left child is 2n+1 right child is 2n+2
     i = 0
     l = len(heap)
     while 2*i + 2 < l :
         lc = heap[2*i + 1]
         rc = heap[2*i + 2]
         p = heap[i]
         
         if (rc > lc) and (rc > p):
             swap(heap, 2*i + 2, i )
             i = 2*i + 2
             
         elif (lc >= rc) and (lc > p):
             swap(heap, 2*i + 1, i)
             i = 2*i + 1
             
         else:
             break

     if (l == 2*i + 2):
          if (heap[i] < heap[2*i + 1] ):
              swap(heap, 2*i + 1, i)

problem2()
