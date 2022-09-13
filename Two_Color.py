#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 19:07:24 2021

@author: bushra
"""

#Bushra Ibrahim
#CS337 Final Exam
#Part A; 1
            
#three graph inputs to test as an adj.matrix in a list of lists
a1 = [[0,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]] #can be 2-colored, no cycle
a2 = [[0,1,1,1],[1,0,0,0],[1,0,0,1],[1,0,1,0]] #cannot be 2-colored, odd cycle
a3 = [[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]] #can be 2-colored, even cycle

"""This function is what I'm turning in officially, for Part A, 1 of the final"""

def Two_Color(L): #input is adj.matrix in list of lists
    
    n = len(L) #getting length of L (so the # of verticies, basically)
    
    edges = [] #initializing list
    
    for i in range(n):
        for j in range(n):
            if L[i][j] == 1 and [j,i] not in edges: 
                #if there is an edge between i & j, add pair to list, edges
                edges.append([i,j])
    
    cycle = 0 #initializing cycle counter as 0
    
    #this loop basically checks for cycles, and increases cycle count
    for i in range(len(edges)): 
        for j in range(len(edges)):
            if i != j:
                #checking if the vertex in question exists in another edge pair
                if edges[i][1] == edges[j][0] and edges[i][1] != edges[j][1]: 
                    cycle += 1
                #if so, increasing the cycle counter 
                elif edges[i][1] != edges[j][0] and edges[i][1] == edges[j][1]:
                    cycle += 1
    #checking if cycle counter is even or odd
    #odd = odd cycle, so 2 color not possible
    #even = even cycle (or no cycle when cycle = 0), so 2 color possible
    if cycle%2 == 0:
        return '1'
    if cycle%2 == 1:
        return '-1'

#printing results of 3 graphs to test
print()
print('The results for 3 graphs using Two_Color')
print(Two_Color(a1))
print(Two_Color(a2))
print(Two_Color(a3))
                
                
"""This function is one I was previously trying to get it to work
using BFS to traverse the graph and flag ones with edges between them in
different colors, but I didn't figure out how to do that - 
I'm leaving it in here for future use and potentially fixing it"""

def Two_Color_BFS(L):
    
    n = len(L)
    eDict = {} #initializing empty dictionary
    
    #populating eDict with vertices as keys and edges ad values from L
    for i in range(n):
        eDict[str(i)] = []
        for j in range(n):
            if L[i][j] == 1:
                eDict[str(i)].append(str(j))

    visited = [] #Initializing visited verticies list
    q = []       #Initializing a queue
        
    def bfs(visited, eDict, v): #visited list, eDict, first vertex
        visited.append(v)
        q.append(v)
        
        while q:          # Creating loop to visit & print each node
            m = q.pop(0)
            print (m, end = " ") 
            for adj in eDict[m]:
                if adj not in visited:
                    visited.append(adj)
                    q.append(adj)       
        
        
    bfs(visited, eDict, '0')
    
print()
print('The result for 3 graphs using Two_Color_BFS')
#these just happened to be the same BFS traversal becaused I used the same vertices
Two_Color_BFS(a1)
print()
Two_Color_BFS(a2)
print()
Two_Color_BFS(a2)
             
                
                
                
    