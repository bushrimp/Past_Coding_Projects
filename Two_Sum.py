#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 21:19:30 2021

@author: bushra
"""

#Bushra Ibrahim
#CS337 Final Exam
#Part B; 1

L = [3,14,2,33,21,9,17,0,45] #arbitrary list
s = 54 # a sum that works
p = 37 # a sum that doesn't

def Two_Sum(L, s): #input is a list, L, and a sum, s (all real numbers)
    
    n = len(L) #procuring length to determing loop
    
    empty = [] #creating empty list
    
    for i in range(n): #looping through # of elements in L
    
        x = s - L[i] #seeing if the difference between the sum and an element in L exists
        
        if x in empty: #if it does, woohoo, we found a pair
            return (L[i],x) #returning that pair
        empty.append(L[i])
        
    if 'None': #couldn't get it to not say "None"
        print('-1') #but it does return -1 if a pair isn't found

print(Two_Sum(L,s),'\n') #successful
print(Two_Sum(L,p)) #failure


