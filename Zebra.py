#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 23:52:50 2020

@author: bushra
"""

import pylab
infile = open('ZebraBotswana.txt','r')
zebras = []
Z = {}
for line in infile:
    datum = line.split(',')
    if datum[3] not in Z:
        Z[datum[3]] = [datum[:3]]
        zebras.append(datum[3])
    else:
        Z[datum[3]].append(datum[:3])
infile.close()

from math import *
def distance(long1,lat1,long2,lat2):
    
    l1 = radians(float(long1))
    l2 = radians(float(long2))
    p1 = radians(float(lat1))
    p2 = radians(float(lat2))
    dp = p2-p1
    dl = l2-l1
    a=sin(dp/2)**2+cos(p1)*cos(p2)*sin(dl/2)**2
    c=2*atan2(sqrt(a),sqrt(1-a))
    d=6371*c
    return d

def AvgDistancePerDay(zebra):
    long = []
    lat = []
    distances = []
    for record in Z[zebra]:
        LO = record[1]
        LA = record[2]
        long.append(LO)
        lat.append(LA)
    for i in range((len(long) -1)):
        each = distance(long[i],lat[i],long[i+1],lat[i+1])
        distances.append(each)
    avgdistance = (sum(distances))/(NumberOfDays(zebra))
    return avgdistance

def NumberOfDays(zebra):
    timetotal = []
    for record in Z[zebra]:
        timestamp = float(record[0])
        timetotal.append(timestamp)
    first = timetotal[0]
    last = timetotal[-1]
    difference = last - first
    days = difference/86400
    return days

def XCoord(zebra):
    x = []
    for record in Z[zebra]:
        LO = float(record[1])
        x.append(LO)
    return x

def YCoord(zebra):
    y = []
    for record in Z[zebra]:
        LA = float(record[2])
        y.append(LA)
    return y

from random import random
colors={}
for zebra in Z:
    colors[zebra] = (random(),random(),random())
    
pylab.figure(1)
pylab.rcParams['lines.linewidth']=1
pylab.title('Zebra Movement')
pylab.xlabel('Longitude')
pylab.ylabel('Latitude')
for zebra in zebras:
    x = XCoord(zebra)
    y = YCoord(zebra)
    pylab.plot(x,y,color = colors[zebra])
pylab.show()


Zebras = pylab.arange(len(zebras))
counts = []
for zebra in zebras:
    xyz = AvgDistancePerDay(zebra)
    counts.append(xyz)
Colors = []
for zebra in zebras:
    rgb = colors[zebra]
    Colors.append(rgb)
pylab.bar(Zebras,counts,0.5,color = Colors)
pylab.xticks(Zebras,zebras)
pylab.xlabel('Zebra Number')
pylab.ylabel('Average Daily Distance')
pylab.title('Average Distance Traveled Per Day')
pylab.show()



