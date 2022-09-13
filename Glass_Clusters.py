#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 17:44:13 2020

@author: bushra
"""

#Program 6 
#Final Assessment
#Bushra Ibrahim
#December 7, 2020

""" Part A - Unsupervised Learning"""

""" Uses kmeans clustering with the z-scaled glass data to identify
    6 clusters for these data, using 200 trials. There are 6 types of glass
    present, which is why we're finding 6 clusters. These clusters and the
    number of each type of glass in each cluster are displayed in the output.
    It could take a few minutes for this output to show up, since it has to
    do 200 trials."""

# 1

#Z-scaling code from class
def zScaleFeatures(vals):
    """Assumes vals is a sequence of floats""" 
    
    mean = sum(vals)/len(vals)
    result = [(x - mean)/stdDev(vals) for x in vals]
    return result

def variance(X):
    """Assumes that X is a list of numbers.
       Returns the standard deviation of X"""
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return tot/len(X)
    
def stdDev(X):
    """Assumes that X is a list of numbers.
       Returns the standard deviation of X"""
    return variance(X)**0.5

#Opening the glassData file and reading it, splitting into
#lines as per usual. I'm flaoting all the values in each
#line and appending them to the data list to then scale
#it with zScaleFeatures. I also collect the categories of 
#glass from the end of each line and store it seperately.
infile = open('glassData.txt','r')
data = []
category = []
for line in infile:
    lineList = line[:-1].split(',')
    lineNum = [float(x) for x in lineList[:-1]]
    data.append(lineNum[:])
    category.append(lineList[-1])
infile.close()

#Make a list of all the attribute values by attribute
allVal = []
for i in range(len(data[0])):
    val = []
    for rec in data:
        val.append(rec[i])
    allVal.append(val)

#Z - Scaling
scaledAllVal = []
for vals in allVal:
    scaledAllVal.append(zScaleFeatures(vals))
   
#Creating template for scaled data
scaledData = []
for i in range(len(data)):
    scaledData.append([])

#Rebuilding the data with scaled attributes
for j in range(len(scaledAllVal)):
    item = scaledAllVal[j]
    for i in range(len(data)):
        scaledData[i].append(item[i])
    
#Create a scaled data file

for i in range(len(scaledData)):
    scaledData[i].append(category[i])
   
outfile = open('glass-zscaled.txt','w')

for rec in scaledData:
    strRec = [str(a) for a in rec]
    string = ','.join(strRec)
    print(string,file = outfile)
    
outfile.close() 
#Successfully made a z-scaled txt file of the data.
#This was all code from class, so I'm not going to
#explain it in detail. The only think I changed was
#instead of i-scaling, its being z-scaled.


#importing these two things because random is used in kmeans
#and pylab is used in computing the centroid.
import random, pylab

#The following is all copied exactly how it was, so I'm not going
#to explain it. I changed a few things, but I'll mention those changes.
def minkowskiDist(v1, v2, p):
    """Assumes v1 and v2 are equal-length arrays of numbers
       Returns Minkowski distance of order p between v1 and v2"""
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p
    return dist**(1/p)
    

#Figure 23.2
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

#Figure 23.3
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
#added method        
    def cohesion(self):
        totDist=0.0
        for e in self.examples:
            totDist += e.distance(self.centroid)
        return 1/totDist
#added method
    def separation(self,cluster):
        return minkowskiDist(self.centroid.getFeatures(),cluster.centroid.getFeatures(),2)                

#added method
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
        result = 'Cluster #' 
        #For this program, Dr. Rauff did not want the centroids displayed,
        #so I just removed that whole part from here.
        return result 

#Figure 23.4
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

#figure 23.5
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

#This is adapted from the wheatseeds clusterDist that Dr. Rauff emailed me
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
    
    #The keys are 1-7 (ommitting 4) in this case, whereas in the wheatseeds
    #it was 1,2,and 3. I simply edited this to fit the glass data, otherwise
    #it's pretty much the same.
    for key in labelDict:
        if key == '1':
            print(str(labelDict[key])+ ' ' + 'items of type 1 ')
        elif key == '2':
            print(str(labelDict[key])+ ' ' + 'items of type 2 ')
        elif key == '3':
            print(str(labelDict[key])+ ' ' + 'items of type 3 ')
        elif key == '5':
            print(str(labelDict[key])+ ' ' + 'items of type 5 ')
        elif key == '6':
            print(str(labelDict[key])+ ' ' + 'items of type 6')
        elif key == '7':
            print(str(labelDict[key])+ ' ' + 'items of type 7')
            
# 2

#To make a list of examples from the glass data, I open the file, read it
#split it into lines as per usual. For the first through the 8th data values,
#I append them to the features list, and the 9th value, which is the glass type,
#I append that as the name or kind of "key" for the example. I also label each
#example by the classificatio, which is 1,2,3,5,6,or 7. Then, I append all those
#examples to the examples list, close the file, and return the list.
def makeGlassExamples():
    infile = open('glass-zscaled.txt','r')
    examples = []
    for line in infile:
        lineList = line[:-1].split(',')
        features = []
        for k in range(0,8):
            examples.append(Example(lineList[9],features,lineList[9]))
    
    features.append(float(lineList[k]))
    infile.close()
    return examples

GE = makeGlassExamples() #GE stands for Glass Examples
GC = Cluster(GE) #GC stands for Glass Cluster
TKM = trykmeans(GE,6,200) #This is the trykmeans output for GE

#Printing out the results with the title and lines to organize it.
print('------------------------------')
print('PART A - Unsupervised Learning')
print('------------------------------')
for i in range(6):
    print(TKM[i],str(i+1),'contains:')
    print(str(clusterDist(TKM[i]))[:-4])
    print('------------------------------')


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    