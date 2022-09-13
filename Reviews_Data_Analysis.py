#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 23:54:46 2020

@author: bushra
"""

#Midterm Exam
#Bushra Ibrahim
#October 1, 2020

#Part 1
import pylab

reviewers = []
R = {}
C =['Sports','Religion','Nature','Theatre','Shopping','Picnic']
infile = open('reviews.txt','r')
total1 = 0
total2 = 0
total3 = 0
total4 = 0
total5 = 0
total6 = 0

for line in infile:
    lineList = line[:-1].split(',')
    total1 = total1 + int(lineList[1])
    total2 = total2 + int(lineList[2])
    total3 = total3 + int(lineList[3])
    total4 = total4 + int(lineList[4])
    total5 = total5 + int(lineList[5])
    total6 = total6 + int(lineList[6])
    if lineList[0] not in R:
        R[lineList[0]] = lineList[1:]
        reviewers.append(lineList[0])
    else:
        R[lineList[0]].append(lineList[1:])
infile.close()

Category = pylab.arange(len(C))
counts = []
for category in C:
    counts = [total1,total2,total3,total4,total5,total6]
    
from random import random
colors = {}
for category in C:
    colors[category] = (random(),random(),random())
    
Colors = []
for category in C:
    rgb = colors[category]
    Colors.append(rgb)
pylab.bar(Category,counts,0.5,color = Colors)
pylab.xticks(Category,C)
pylab.xlabel('Category')
pylab.ylabel('Number of Reviews')
pylab.title('Review by Category')
pylab.show()

#Question 2
infrequent = []
for key in R:
    record = R[key]
    if int(record[0]) < 100:
        if int(record[1]) < 100:
            if int(record[2]) < 100:
                if int(record[3]) < 100:
                    if int(record[4]) < 100:
                        if int(record[5]) < 100:
                            infrequent.append(key)
print(infrequent)

#Question 3
favorite = {}
for key in R:
    record = R[key]
    r = []
    for x in record:
        y = int(x)
        r.append(y)
    favorite[key] = max(r)
print(favorite)

#Question 4
from graphClass import *
R2 = Graph()
V1 = []
for key in R:
    record = R[key]
    r = []
    for x in record:
        y = int(x)
        r.append(y)
    Max = max(r)
    if Max == int(record[3]):
        v = key
        V1.append(v)

for i in range(len(V1)):
    rec1 = R[V1[i]]
    r1 = int(rec1[0])
    for x in range(len(V1)):
        rec2 = R[V1[x]]
        r2 = int(rec2[0])
        if i < x:
            if r1 == r2:
                R2.addEdge(V1[i],V1[x])
print(R2)

        
        


    

    



        
        
    