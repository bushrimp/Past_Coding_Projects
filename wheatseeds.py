#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 12:36:55 2020

@author: bushra
"""

#Bushra Ibrahim
#November 17, 2020
#Program 5

#This program uses the K-means clustering technique to classify wheat kernels
#into three groups. Also, this program reports the cohesion, integrity, 
#and seperation of the cluster. 

#Most of this code is from projectileKmeans, and it is relatively unchanged.
#I might have tweaked a few things, but I will comment wherever I've changed
#something.

import random, pylab

def minkowskiDist(v1, v2, p):
    """Assumes v1 and v2 are equal-length arrays of numbers
       Returns Minkowski distance of order p between v1 and v2"""
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p
    return dist**(1/p)
    
class Example(object):
    
    def __init__(self, name, features, label = None):
        #Assumes features is an array of floats
        self.name = name
        self.features = features
        self.label = label
        
    def dimensionality(self):
        return len(self.features)
    
    def getFeatures(self):
        return self.features[:]
    
    def getLabel(self):
        return self.label
    
    def getName(self):
        return self.name
    
    def distance(self, other):
        return minkowskiDist(self.features, other.getFeatures(), 2)
    
    def __str__(self):
        return self.name +':'+ str(self.features) + ':'\
               + str(self.label)

#To make a list of examples from the wheat seed data, I open the file, read it
#split it into lines as per usual. Then, I skip every empty line since this data
#had data in only every other line. For the first through the 6th data values,
#I append them to the features list, and the 7th value, which is the type classification,
#I append that as the name or kind of "key" for the example. I also label each
#example by the classificatin, which is 1,2, or 3. Then, I append all those examples 
#to the examples list, close the file, and return the list.
def makeWheatExamples():
    infile = open('seedsData.txt','r')
    examples = []
    for line in infile:
        lineList = line[:-1].split('\t')
        features = []
        if lineList != ['']:
            for k in range(0,6):
                features.append(float(lineList[k]))
            examples.append(Example(lineList[7],features,lineList[7]))
    infile.close()
    return examples

class Cluster(object):
    
    def __init__(self, examples):
        """Assumes examples a non-empty list of Examples"""
        self.examples = examples
        self.centroid = self.computeCentroid()
        
    def update(self, examples):
        """Assume examples is a non-empty list of Examples
           Replace examples; return amount centroid has changed"""
        oldCentroid = self.centroid
        self.examples = examples
        self.centroid = self.computeCentroid()
        return oldCentroid.distance(self.centroid)
    
    def computeCentroid(self):
        vals = pylab.array([0.0]*self.examples[0].dimensionality())
        for e in self.examples: #compute mean
            vals += e.getFeatures()
        centroid = Example('centroid', vals/len(self.examples))
        return centroid

    def getCentroid(self):
        return self.centroid

    def variability(self):
        totDist = 0.0
        for e in self.examples:
            totDist += (e.distance(self.centroid))**2
        return totDist
    
    def cohesion(self):
        totDist=0.0
        for e in self.examples:
            totDist += e.distance(self.centroid)
        return 1/totDist

    def separation(self,cluster):
        return minkowskiDist(self.centroid.getFeatures(),cluster.centroid.getFeatures(),2)                

    def integrity(self):
        labels={}
        for e in self.examples:
            if e.getLabel() not in labels:
                labels[e.getLabel()]=1
            else:
               labels[e.getLabel()] +=1
        
        maj = max([labels[i] for i in labels])
        total=sum([labels[i] for i in labels])
        return maj/total    

    def __str__(self):
        names = []
        for e in self.examples:
            names.append(e.getName())
        names.sort()
        result = 'Cluster with centroid '\
               + str(self.centroid.getFeatures()) + ' contains: '
        #I cut out this portion, because I didn't want every single seed to be
        #listed when I print out the clusters.
        return result 

def dissimilarity(clusters):
    totDist = 0.0
    for c in clusters:
        totDist += c.variability()
    return totDist
    
def trykmeans(examples, numClusters, numTrials, verbose = False):
    """Calls kmeans numTrials times and returns the result with the
          lowest dissimilarity"""
    best = kmeans(examples, numClusters, verbose)
    minDissimilarity = dissimilarity(best)
    trial = 1
    while trial < numTrials:
        try:
            clusters = kmeans(examples, numClusters, verbose)
        except ValueError:
            continue #If failed, try again
        currDissimilarity = dissimilarity(clusters)
        if currDissimilarity < minDissimilarity:
            best = clusters
            minDissimilarity = currDissimilarity
        trial += 1
    return best

def kmeans(examples, k, verbose = False):
    #Get k randomly chosen initial centroids, create cluster for each
    initialCentroids = random.sample(examples, k)
    clusters = []
    for e in initialCentroids:
        clusters.append(Cluster([e]))
        
    #Iterate until centroids do not change
    converged = False
    numIterations = 0
    while not converged:
        numIterations += 1
        #Create a list containing k distinct empty lists
        newClusters = []
        for i in range(k):
            newClusters.append([])
            
        #Associate each example with closest centroid
        for e in examples:
            #Find the centroid closest to e
            smallestDistance = e.distance(clusters[0].getCentroid())
            index = 0
            for i in range(1, k):
                distance = e.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            #Add e to the list of examples for appropriate cluster
            newClusters[index].append(e)
            
        for c in newClusters: #Avoid having empty clusters
            if len(c) == 0:
                raise ValueError('Empty Cluster')
        
        #Update each cluster; check if a centroid has changed
        converged = True
        for i in range(k):
            if clusters[i].update(newClusters[i]) > 0.0:  
                #update returns distance between old and new centroids
                converged = False
                
        if verbose:
            print('Iteration #' + str(numIterations))
            for c in clusters:
                print(c)
            print('') #add blank line
    return clusters

#This code is from Dr. Rauff's email when I asked about how to count
#the number of seeds instead of just listing them all.
#To give counts of examples in cluster
def clusterDist(cluster):
    #Find the labels on the examples in the cluster
    labels=[]
    for ex in cluster.examples:
        if ex.label not in labels:
            labels=labels+[ex.label]
    labelDict = {}
    for label in labels:
        labelDict[label] = 0
    for ex in cluster.examples:
        labelDict[ex.label]+=1
    
    print(labels)
    
    for key in labelDict:
        if key == '1':
            print(str(labelDict[key])+ ' ' + 'Kama ')
        elif key == '2':
            print(str(labelDict[key])+ ' ' + 'Rosa ')
        elif key == '3':
            print(str(labelDict[key])+ ' ' + 'Canadian ')




WE = makeWheatExamples() #WE stands for Wheat Examples
WC = Cluster(WE) #WC stands for Wheat Clusters
TKM = trykmeans(WE,3,2) #This is the trykmeans output for WE
x,y,z = TKM #I assign x,y,and z to each of the clusters to use them below

#Assigning variables to the cohesion value of each cluster
X1 = x.cohesion()
Y1 = y.cohesion()
Z1 = z.cohesion()

#Assigning variables to the integrity values of each cluster
X2 = x.integrity()
Y2 = y.integrity()
Z2 = z.integrity()

#Calculating the global integrity
I = (X2 + Y2 + Z2) / 3

#Assigning variables to the separation values of each cluster
X3 = WC.separation(x)
Y3 = WC.separation(y)
Z3 = WC.separation(z)

#Making a list of separation values, so I can sort it and identify the two 
#greatest ones
S = [X3,Y3,Z3]
S1 = sorted(S)

#Everything below here is just printing out the final results
print('Final result:\n')

#Looping through the three best clusters and printing the amount of each seed
#in each cluster, plus each cluster's integrity, separation, and cohesion.
for i in range(3):
    print(TKM[i])
    print(str(clusterDist(TKM[i]))[:-4])
    print('This cluster has: ')
    print('cohesion - ',TKM[i].cohesion())
    print('integrity - ',TKM[i].integrity())
    print('separation - ',WC.separation(TKM[i]))
    print('-----------------------------------------')
    
print()

#Finding which cohesion value is the greatest and printing it out
if X1 > Y1 and X1 > Z1:
    print('The first cluster has the greatest cohesion of',X1)
    print()

if Y1 > X1 and Y1 > Z1:
    print('The second cluster has the greatest cohesion of',Y1)
    print()
    
if Z1 > Y1 and Z1 > X1:
    print('The third cluster has the greatest cohesion of',Z1)
    print()
    
#Printing out the two clusters with the greates separation, and also reporting
#the global integrity.
print("The two clusters with a separation of",S1[1],'and',S1[2],'are the most definitive\n')
print('The global integrity is',I,)








