#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 21:28:16 2020

@author: bushra
"""
#Part 1
infile = open('winequality-white.txt','r')
avgAtt = [0,0,0,0,0,0,0,0,0,0,0]
wineCount = 0

for line in infile:
    wineLine = line[:-1].split(';')
    wineCount += 1
    for i in range(11):
        avgAtt[i] += float(wineLine[i])
avgAtt = [i/wineCount for i in avgAtt]
    
infile.close()

#Part 2
infile = open('winequality-white.txt','r')
outfile = open('winequality-whiteAB.txt','w')
for line in infile:
    wineLine = line[:-1].split(';')
    newLine = ''
    for i in range(11):
        if float(wineLine[i]) >= avgAtt[i]:
            newLine = newLine + 'a,'
        else:
            newLine = newLine + 'b,'
    newLine = newLine + wineLine[11]
    print(newLine,file = outfile)
outfile.close()
infile.close()

#Part 3
"""To do: Count all wines with value 'val'.
          Count within that group those that have attNum attVal.
          Divide the second count by the first."""
            
def Prob(attNum,attVal,val,filename):
    """attNum is int, attVal is str, val is int"""
    attNum = attNum - 1
    countVal = 0
    countAttVal = 0
    infile = open(filename,'r')
    for line in infile:
        wineLine = line[:-1].split(',') #Assumes comma separated values (CSV)
        if wineLine[-1] == str(val):
            countVal += 1
            if wineLine[attNum] == attVal:
                countAttVal += 1
    return countAttVal/countVal
    
#Example runs
P1 = Prob(4,'a',6,'winequality-whiteAB.txt')
P2 = Prob(8,'b',6,'winequality-whiteAB.txt')

#Calculate the probability that a white wine has quality > 7 given that it has above average residual sugar. 
infile = open('winequality-whiteAB.txt','r')
count1 = 0
count2 = 0
for line in infile:
    lines = line[:-1].split(',')
    if lines[11] in ['7','8'] and lines[3] == 'a':
        count1 += 1
    if lines[3] == 'a':
        count2 += 1
        
prob = count1/count2
print(prob)
    














