#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 11:29:39 2020

@author: bushra
"""
#Bushra Ibrahim
#Program 4 - Mushrooms
#October 27, 2020

#This program uses the naive Bayes Classifier to learn the qualities of
#edible mushrooms versus poisonous mushrooms from a large training set
#of mushroom data. It then uses the learned information to predict
#whether each shroom in an unknown set of mushroom data is edible or not.

#importing all functionalities of naiveBayesGeneral here, to use
#getTrainingSet and Bayes.
from naiveBayesGeneral import *

#Opening the original mushroom data file, mr.txt. It needs to be edited 
#to use getTrainingSet.
infile = open('mr.txt','r')
#Opening a new file called 'shrooms.txt' to which the edited data from
#mr.txt will write out to.
outfile = open('shrooms.txt','w')
#For each line until 'EOF' is reached, I'm cutting of the line feed, and 
#splitting it at the commas. The newList becomes the old list without the
#first term (which is the poisonous or edible classification) and adds
#that first term to the end of the list. newLine turns it into a line and
#writes it out in the outfile called 'shrooms.txt.'
for line in infile:
    if line != 'EOF':
        lineList = line[:-1].split(',')
        newList = lineList[1:]+[lineList[0]]
        newLine = ','.join(newList)
        print(newLine, file = outfile)
#Closing both files
infile.close()
outfile.close()

#Using getTrainingSet to find the max mushroom value, and the probability
#of a mushroom being that value (in this case 'p' or 'e').
vm,tm = getTrainingSet('shrooms.txt')

#Opening the unknown.txt file which has the unknown mushroom data.
#Going through each line and cutting off the line feed, splitting
#at the commas. 'novel' is the list of attributes of a mushroom
#from the unknown data file, and 'prediction' uses the Bayes function
#with the shrooms traingin data and values ('p' and 'e') to predict
#what novel's value is.
infile = open('unknown.txt','r')
for line in infile:
    lineList = line[:-1].split(',')
    novel = lineList
    prediction = Bayes(novel,tm,vm)
    print(prediction)
infile.close()
#Just printing an English explanation of the result.
print('The program classified the first three mushrooms as edible, and the fourth as poisonous.')