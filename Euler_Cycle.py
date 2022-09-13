#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 18:08:42 2021

@author: bushra
"""
#Bushra Ibrahim
#CS337 
#Exam 1
#Question 2

#some matrices to test function

M1 = [[1,0,0],[0,0,1],[1,1,0]] #no Euler Cycle
M2 = [[1,0,1,1],[0,1,0,1],[1,1,0,0],[1,0,1,0]] #no Euler Cycle
M3 = [[1,1,1,1],[1,1,1,1],[1,1,0,0],[1,0,1,0]] #has an Euler Cycle
M4 = [[1,1,0],[0,0,0],[1,0,1]] #has an Euler Cycle

        
def DoesMatrixHaveEulerCircuit(M): #input is a matrix (nxn since it represents a graph)
    n = len(M) #taking the number of rows in matrix
    ED = 0 #initializing even degree counter
    for i in range (n): 
        a = M[i]
        aSum = 0
        for i in a: #summing up the numbers in each row
            aSum += i
        if aSum % 2 == 0: #if sum is even, ED counter increments
            ED += 1
    if ED == n: #if all rows have even degree, then the graph has a Eulerian Circuit
        return 'This graph has an Eulerian Circuit'
    else: #if not, it doesn't
        return 'This graph does not have an Eulerian Circuit'
            

print(DoesMatrixHaveEulerCircuit(M1))
print(DoesMatrixHaveEulerCircuit(M2))
print(DoesMatrixHaveEulerCircuit(M3))
print(DoesMatrixHaveEulerCircuit(M4))
