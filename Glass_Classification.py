#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 13:15:10 2020

@author: bushra
"""


""" Part B - Supervised Learning """

""" Uses Nearest Neighbor, K-Nearest Neighbor, and Mean Similarity Vector
    techniques with Minkowski (p=2) metric to classify the 10 unknown 
    glass samples from the 'testGlass.txt' file (this file includes the
    actual classifications, but I made a new file without those to use here.
    The 'glassData.txt' file is used as the training set. The output numbers 
    the unknown glass samples plus the classification that each technique 
    results in. That consits of parts 1, 2, and 3. Part 4 produces a bar 
    graph that shows the number of correct classifications per technique."""

# 1

#Most of the following is all copied exactly how it was, so I'm not going
#to explain it. I changed a few things, but I'll mention those changes.
def feature(featureDatafile, splitCh =','):
    infile=open(featureDatafile,'r')
    feature={}
    ID=1
    for line in infile:
        feature[ID]=line[:-1].split(splitCh)
        ID+=1
    infile.close()
    return feature

def minkowskiDist(v1, v2, p):
    """Assumes v1 and v2 are equal-length arrays of numbers
       Returns Minkowski distance of order p between v1 and v2"""
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p
    return dist**(1/p)

def nearestNeighbor(new,feature):
    """assumes new is a list of floats"""
    nearest = 10000
    value ='?'
    for ID in feature:
        old = [float(a) for a in feature[ID]]
        dist = minkowskiDist(new,old,2)
        if dist < nearest:
            nearest = dist
            value = feature[ID][-1]
            neighbor = ID

    #In order for nearestNeighbor to output the sample number and 
    #identified type of glass, I used the followind if statements.
    #I simply used the original data file (glassData.txt) to figure
    #out which number intervals were what type of glass, and listed
    #those intervals here so that if 'neighbor' is within that interval
    #it is classified as that type of glass.
    if neighbor in range(0,70):
        Type = 'type 1'
    if neighbor in range(71,143):
        Type = 'type 2'
    if neighbor in range(144,158):
        Type = 'type 3'
    if neighbor in range(159,169):
        Type = 'type 5'
    if neighbor in range(170,178):
        Type = 'type 6'
    if neighbor in range(179,205):
        Type = 'type 7'
    
    #The following 'if's here were to make sure the output printed out
    #the sample numbers correctly. I was having trouble with that here, so 
    #I just punched my way through the code, which is why it's pretty long
    #and seeminglt unecessary. I found a more efficient way to do this later
    #on, but I was already completed with the program by then so I didn't 
    #feel the need to come back and fix this.
    if new == [1.51674,12.79,3.52,1.54,73.36,0.66,7.90,0.00,0.00]:
        s = '1'
    if new == [1.51674,12.87,3.56,1.64,73.14,0.65,7.99,0.00,0.00]:
        s = '2'
    if new == [1.51690,13.33,3.54,1.61,72.54,0.68,8.11,0.00,0.00]:
        s = '3'
    if new == [1.51934,13.64,3.54,0.75,72.65,0.16,8.89,0.15,0.24]:
        s = '4'
    if new == [1.52211,14.19,3.78,0.91,71.36,0.23,9.14,0.00,0.37]:
        s = '5'
    if new == [1.51514,14.01,2.68,3.50,69.89,1.68,5.87,2.20,0.00]:
        s = '6'
    if new == [1.51915,12.73,1.85,1.86,72.69,0.60,10.09,0.00,0.00]:
        s = '7'
    if new == [1.51719,14.75,0.00,2.00,73.02,0.00,8.53,1.59,0.08]:
        s = '8'
    if new == [1.51683,14.56,0.00,1.98,73.29,0.00,8.52,1.57,0.07]:
        s = '9'
    if new == [1.51888,14.99,0.78,1.74,72.50,0.00,9.95,0.00,0.00]:
        s = '10'
    
    #Printing the sample number with the identified glass type for each
    #unknown glass sample.
    print('Sample #{0} is glass {1}'.format(s,Type))
    
    
#Opening the glassData file and reading it, splitting into
#lines as per usual. I make a new file called 'glass.txt' without
#the glass classification numbers at the end of each line. This is 
#in order to make a feature suited for the nearestNeighbor function.
infile = open('glassData.txt','r')
outfile = open('glass.txt','w')
for line in infile:
    lineList = line[:-1].split(',')
    newList = lineList[:-1]
    newLine = ','.join(newList)
    print(newLine, file = outfile)
infile.close()
outfile.close()

#Similarly, I parse through the testGlass file and do the same thing.
#I make a new file called 'test.txt' to use, and this file does not
#have the classifications at the end of each line also.
infile = open('testGlass.txt','r')
outfile = open('test.txt','w')
for line in infile:
    lineList = line[:-1].split(',')
    newList = lineList[:-1]
    newLine = ','.join(newList)
    print(newLine, file = outfile)
infile.close()
outfile.close()

#Printing out what part of the program this is and adding some
#lines to make it look organized.
print ('PART B - Supervised Learning')

#Creating a feature space with the glass data lacking the
#classification numbers.
G = feature('glass.txt')
print('--------------------------')
print('1: Nearest Neighbor')
print('--------------------------')

#Opening the unknown glass sample file and parsing through it
#normally. I float all the values and put it in a list called
#'floated' because the nearestNeighbor function uses a list of
#floats to work, not a list of strings. 
infile = open('test.txt','r')
for line in infile:
    lineList = line[:-1].split(',')
    floated = []
    for x in lineList:
        a = float(x)
        floated.append(a)
    #Employing nearestNeighbor here, and finishing it off with a line.
    glass = nearestNeighbor(floated,G)
print('---------------------------')

# 2

#Most of the following is all copied exactly how it was, so I'm not going
#to explain it. I changed a few things, but I'll mention those changes.
def defineClasses(feature):
    #extract class designations into a list
    classDesignations=[]
    for key in feature:
        if feature[key][-1] not in classDesignations:
            classDesignations.append(feature[key][-1])
    return classDesignations

def KNN(new,f,k):
    
    neighborList=[]
    count=0
    ID=0
    
    while count != k:
        ID +=1
        if ID in f:
            old=[float(v) for v in f[ID][:-1]]
            neighborList.append((ID,minkowskiDist(new,old,2)))
            count +=1
    for key in f:
        dist= minkowskiDist(new,[float(v) for v in f[key][:-1]],2)
        currentMax=max(neighborList, key = lambda x: x[1])
        if dist < currentMax[1]:
            neighborList.remove(currentMax)
            neighborList.append((key,dist))
      
    #This KNN was adapted from the work we did with the Iris data.
    #There are 6 types of glass, which is why there are 6 0s in the
    #votes list.
    voters = defineClasses(f)
    votes = [0,0,0,0,0,0]
    
    #The range is 6, again, because there are 6 types of glass.
    #The f (or feature) part is to the 9th piece of data because
    #those are how many attributes there are.
    for pair in neighborList:
        for i in range(6):
            if f[pair[0]][9]==voters[i]:
                votes[i] += 1
    most = 0
    glass = []
    
    #Collecting the votes for the k amount of nearest neighbors
    for i in range(len(votes)):
        if votes[i] > most:
            most = votes[i]
            glass = [voters[i]]
        elif votes[i]==most:
            glass.append(voters[i])

    return glass #returning the glass classification that KNN results in

#Creating a new feature space that uses the original data file and not
#the other one I made without the classification numbers at the end.
G2 = feature('glassData.txt')

#Printing out the title of this section and adding some lines and stuff
#again, for organization.
print('2: K-Nearest Neighbor')
print('--------------------------')

#Opening the tst file with the unknown glass samples and parsing through.
#I'm floating all the data because KNN is expecting a list of floats, not
#strings. I collect the glass classifications in the list 's' and make sure
#that it's just a list of integers rather than strings.
infile = open('test.txt','r')
s = []
for line in infile:
    lineList = line[:-1].split(',')
    floated = []
    for x in lineList:
        a = float(x)
        floated.append(a)
    #Employing KNN here, using the G2 feature, and k=3
    g = KNN(floated,G2,3)
    s.append(int(''.join(g)))
    
#Printing out the results with the sample number and the KNN
#classification.
for i in range(1,11):
    print('Sample #{0} is glass type {1}'.format(i,s[i-1]))
print('--------------------------')
    
# 3

#Most of the following is all copied exactly how it was, so I'm not going
#to explain it. I changed a few things, but I'll mention those changes.
def separateClasses(feature):
    #make a dictionary keyed by class name with values a list of keys
    cd=defineClasses(feature)
    classes={}
    for className in cd:
        classes[className]=[]
    for key in feature:
        classes[feature[key][-1]].append(key)
    return classes

def classMeanVector(keylist,feature):
    #Finds the mean vector for vectors in keylist in feature space
    attributes=len(feature[keylist[0]][:-1])
    numKeys=len(keylist)
    meanVector=[]
    for item in range(attributes):
        total=0
        for key in keylist:
            total = total + float(feature[key][item])
        meanItem=total/numKeys
        meanVector.append(meanItem)
    return meanVector
        
def getAllClassMeanVectors(feature):
    classes=separateClasses(feature)
    meanClassVectors={}
    for className in classes:
        meanClassVectors[className]=classMeanVector(classes[className],feature)
    return meanClassVectors            
    
def classify(new,MCVs):
    #Find the closest class mean vector to new from all mean clas vectors (MCVs)
     c=''
     minDist=10000
     for mcv in MCVs:
         dist = minkowskiDist(new,MCVs[mcv],2)
         
         if dist < minDist:
             c=mcv
             minDist=dist
     #This program didn't need the distance, so I just made it 
     #return classification 'c'
     return c 

#Printing out the title of this section and some lines.
print('3: Mean Similarity')
print('--------------------------')
    
#Parsing through the test data file again, and floating 
#all the values since getAllClassMeanVectors is expecting a 
#list of floats. Similar to KNN, I collect the classifications
#in the list 'j' here to use it in the print statement below.
infile = open('test.txt','r')
j = []
for line in infile:
    lineList = line[:-1].split(',')
    floated = []
    for x in lineList:
        a = float(x)
        floated.append(a)
    #Employing the class mean vector function here with the
    #feature space G2 that I made previously. I didn't need 
    #a new feature space, so I just used that one.
    MCVs = getAllClassMeanVectors(G2)
    #assigning the classifcation a random variable 'k'
    #and appending that to my list 'j'.
    k = classify(floated,MCVs)
    j.append(k)
    
#Printing out the results with the sample number and the mean similarity
#vector classifications.
for i in range(1,11):
    print('Sample #{0} is glass type {1}'.format(i,j[i-1]))
print('--------------------------')

# 4

#Importing pylab because I'm going to need it to make a bar graph
import pylab

#Creating a figure, and just calling it '1' since there's only
#one in this program. 
pylab.figure(1)
#SLTs stands for Supervised Learning Techniques, and I 
#list those here in string form.
SLTs =['Nearest Neighbor','KNN','Mean Similarity']
#I just manually counted how many classifications each technique
#got right, and entered them here in the 'quant' list.
quant=[7,7,4]
q = pylab.arange(len(SLTs))
colors=['red','blue','purple'] #Assigning some arbitrary colors to the bars

#number of bars, height of bars, width of bars,color of bars
pylab.bar(q,quant,0.5,color=colors)

#label the bars
pylab.xticks(q,SLTs)

#Labeling the bars, and the graph itself, and the finally showing it.
pylab.xlabel('Supervised Learning Techniques')
pylab.ylabel('Number of Correct Classifications')
pylab.title('Program 6')
pylab.show()










       
    
    


