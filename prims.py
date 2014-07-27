# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 13:00:15 2014

@author: Corinna
"""
from random import randint

def readfile():
    data = []
    firstline = True
    with open("jobs.txt") as f:
        for line in f:
            if not firstline:
                data.append( [int(i) for i in line.split(" ")] )
            else:
                firstline = False
                print line
    return data
    
def swap(array, i1, i2):
    temp = array[i1]
    array[i1] = array[i2]
    array[i2] = temp
    
def schedule_tasks(score_array, d, start, end):
    #print score_array[start:end]
    if end - start  > 1:
        counter = start
        pivot = score_array[start]
        for i in range(start+1, end):
            if score_array[i] < pivot or (score_array[i] == pivot and d[i][0] < d[start][0] ):
                counter += 1
                swap(score_array, counter, i)
                swap(d, counter, i)
        
        swap(score_array, start, counter)
        swap(d, start, counter)
        
        schedule_tasks(score_array, d, start, counter)
        schedule_tasks(score_array, d, counter+1, end)
        
                
def gen_finish_time_sum(tasks):
    time = 0
    ws = 0
    for t in tasks:
        time = time + t[1]
        ws += time * t[0]
        
        
    return ws
                
def test():
    
    t = []
    for i in range(1000): 
        t.append( randint(0,1000000) )
        
    schedule_tasks(t, [[a,a] for a in t], 0, len(t))
                
    
def main():
    d = readfile()
    score_array = [(v[0]*1.0) - (v[1]*1.0) for v in d]
    
    schedule_tasks(score_array, d, 0, len(score_array) )
    score_array = score_array[::-1]
    d = d[::-1]    
    
    print d
    ws = gen_finish_time_sum(d)
    print ws    
    

def add_min_edge(visited, edges):
    m = None
    for e in edges:
        f = e[0] in visited and e[1] not in visited
        s = e[1] in visited and e[0] not in visited
        
        if (f or s) and (m==None or e[2] < m[2]):
            m = e
    
    if m != None:        
        if m[0] in visited:
            visited[m[1]] = True
        else:
            visited[m[0]] = True
            
        return m[2]
    else:
        return None


def MST():
    visited = {}
    edges = [] #v1,v2,w
    r = 0
    with open("edges.txt") as f:
        firstline = True
        for line in f:
            if firstline == False:
                vals = [int(a) for a in line.split(" ")]
                edges.append( (vals[0], vals[1], vals[2]) ) 
            else:
                firstline = False
    print "done reading" 
    
    visited[ edges[0][0] ] = True    
    
    while True:
        new_e = add_min_edge(visited , edges)
        if new_e != None:
            r += new_e
        else:
            break
        
    print r
    
MST()
        
    
    
    