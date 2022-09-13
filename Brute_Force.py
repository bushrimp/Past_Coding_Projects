#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 18:08:42 2021

@author: bushra
"""
#Bushra Ibrahim
#CS337 
#Exam 1
#Question 1

from math import sqrt,inf #importing square root and infinity


#just three sets of points of varying lengths to test the function
P = [(2,3),(0.45,-2),(11,1)]
L = [(1,2),(15,3.5),(7,100.54),(1,3),(0,-47)]
A = [(-45,2),(0,0),(4,3.7),(8.967,12),(1,1000),(-23.45,0)]

def BruteForceClosestPoints(P): #input is P, list of points in (x,y) format
    n = len(P) #getting number of points in list
    dmin = inf #initializing dmin to infinity
    for i in range (n-1): #making sure distance for same pair of points is not 
        for j in range (i+1,n): #calculated twice - complexity is still n^2
            d = sqrt(((P[i][0] - P[j][0])**2 + ((P[i][1] - P[j][1])**2))) #calculating distance
            if d < dmin: #if the distance is less than dmin, replace dmin with d
                dmin = d
                index1 = i 
                index2 = j
    return index1, index2 #returning indices that identify which points are closest

print(BruteForceClosestPoints(P))
print(BruteForceClosestPoints(L))
print(BruteForceClosestPoints(A))