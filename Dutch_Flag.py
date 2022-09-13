#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 18:08:42 2021

@author: bushra
"""
#Bushra Ibrahim
#CS337 
#Exam 1
#Question 3

#two strings to test the function
S1 = 'BBRWWBRWBRWW'
S2 = 'BRWRWBRRBBRWRBWWRWBRRRBBBRWRWRB'

def DutchFlagProblem(S): #input is a string of 'R's 'B's and 'W's
    L = list(S) #turn the string to a list
    #initialize Red, White, and Blue lists as empty lists
    R = []
    W = []
    B = []
    for x in L:
        #for each character in the string, it gets appended to its respective list
        if x == 'R':
            R.append(x)
        if x == 'W':
            W.append(x)
        if x == 'B':
            B.append(x)
    RWB = R + W + B #the three seperate lists are put back together as one list
    Dutch = ''.join(RWB) #turning RWB to a string
    return Dutch #since the input was a string, I'm making the output also a string

print(DutchFlagProblem (S1))
print(DutchFlagProblem (S2))