#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 17:41:36 2021

@author: bushra

Bushra Ibrahim

Exam 2

Question 2
"""

from digraphClass import *

def sourceRemoval(d):
    
    sortedList = []
    vList = d.vertexList.copy()

    def sr(v):
         d.vertexList.remove(v)
         del d.edges[v]
         sortedList.append(v)
         
    for i in vList:
        if d.inDegree(i) == 0:
            sr(i)
              
    return sortedList

d = Digraph()
d.addVertex(0)
d.addEdge(0,1)
d.addEdge(0,3)
d.addEdge(1,4)
d.addEdge(3,5)
d.addEdge(5,2)
d.addEdge(5,8)
d.addEdge(2,6)
d.addEdge(2,7)

b = Digraph()
b.addVertex(1)
b.addEdge(1,0)
b.addEdge(1,3)
b.addEdge(0,2)
b.addEdge(0,5)
b.addEdge(3,4)
b.addEdge(3,6)

print(sourceRemoval(d))
print(sourceRemoval(b))
