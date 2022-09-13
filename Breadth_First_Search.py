#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 17:41:36 2021

@author: bushra

Bushra Ibrahim

Exam 2

Question 1
"""
from matrixClass import *

A = Matrix(5,5)
A.mat[0][1] = 1
A.mat[0][2] = 1
A.mat[0][4] = 1
A.mat[1][0] = 1
A.mat[2][0] = 1
A.mat[3][4] = 1
A.mat[4][0] = 1
A.mat[4][3] = 1

def BFS(B):
    vDict = {}
    vList = []
    VO = [0]
    for i in range(B.rows):
        vDict[i] = 0
        vList.append(i)
    for i in range(B.rows):
        for j in range(B. columns):
            if B.mat[i][j] == 1:
                if vDict[j] == 0:
                    vDict[j] = 1
                if j not in VO:
                    VO.append(j)
    return VO

Run = BFS(A)
print(Run)