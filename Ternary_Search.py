#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 21:57:44 2021

@author: bushra
"""

#Bushra Ibrahim
#CS337 Final Exam
#Part B; 2

L1 = [3,12,21,29,37,43,52,68,87,92,99,102,110,200] #arbitrary sorted list
K1 = 35 #a key that will fail
K2 = 21 #a key that will work

L2 = [3] #a list with only one element to make sure that it can accept 1-element lists
K3 = 3 #the key that is the single element in L2

def Ternary_Search (L, K): #input is a sorted list, L, and a search key int, K
    
    if len(L) == 1 and K in L: #this is for single element lists
        print('1: key was found at L[0], since L only had 1 element')
        return
    
    l = 0 #initializing leftmost
    r = len(L) - 1 #and rightmost 
    
    while l <= r: #as long as l is less than r...
     
      #i1 and i2 are indices that will change as it searches
      i1 = l + (r - l) // 3 #0 to first third
      i2 = l + 2 * (r - l) // 3 #second third to end
      
      #the chunk in between i1 & i2 is the mid third
      
      if K == L[l]: #we found K at L[l] yay
         print("1: key found at index [" + str(l) + "]")
         return
     
      elif K == L[r]: #we found K at L[r] yay
         print("1: key found at index [" + str(r) + "]")
         return
     
      elif K < L[l] or K > L[r]: #if it's not in this list, not within it's range
         print("-1: key not found")
         return
     
      elif K <= L[i1]: #reindexing if K is in first third
         r = i1
         
      elif K > L[i1] and K <= L[i2]: #reindexing if K is mid third
         l = i1 + 1
         r = i2
         
      else: #reindexing if K is in last third
         l = i2 + 1
    return

#testing
Ternary_Search(L1,K1) #should fail
Ternary_Search(L1,K2) #should work
Ternary_Search(L2,K3) #should work