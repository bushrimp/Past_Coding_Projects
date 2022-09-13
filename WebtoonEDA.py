#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Apr  8 00:10:01 2022

@author: bushra

5/5/22

Bushra Ibrahim

Webtoons: Exploratory Data Analysis

https://www.kaggle.com/datasets/iridazzle/webtoon-originals-datasets?select=webtoon_originals_en.csv

*this is where I got the data from
*see note below for changes
"""
#importing pylab and random for graphing use later
import pylab
#ppl seem to use matplotlib more, but this is sufficient for this project
from random import random
#this random is only for the random color generator

"""
Some changes I made to the .csv file before parsing it here...
1. I removed any entries with empty fields (15)
2. I removed f3 fields: authors, weekdays, and synopsis (they had comma, 
   and were unecessary for the analysis I wanted to do)
3. I removed fixed any fields I kept that had commas in them so that
   it didn't affect the parsing
"""
#opening and separating each line from .csv file, and making list of each line
infile = open("Webtoons.csv",'r')
records = []
for line in infile:
    if 'length' not in line:
        L = line[:-1].split(',')
        records.append(L)
    
"""
Column Indices

 'title_id', 0
 'title', 1
 'genre', 2
 'length', 3
 'subscribers', 4
 'rating', 5
 'views', 6
 'likes', 7
 'status', 8
 'daily_pass', 9
 
"""

#initializing lists of the fields I'm analyzing only
title = []
genre = []
subscribers = []
rating = []
views = []
likes = []

#appending the correct data to each list
for record in records:
    title.append(record[1])
    genre.append(record[2])
    subscribers.append(int(record[4]))
    rating.append(float(record[5]))
    views.append(int(record[6]))
    likes.append(int(record[7]))

"""
GENRES
    keep in mind, subscribers can overlap bc if you like a genre, you may 
    subscribe to many in that genre
    
    I noticed the the data labeled some genres differently than Webtoon
"""
#this function returns the 5 key data that i want
def Genre_Analysis(genre):
    count = 0    
    sub = 0
    rat = 0
    views = 0
    likes = 0
    for record in records:
        if record[2] == genre:
            count += 1
            sub += int(record[4])
            rat += float(record[5])
            views += int(record[6])
            likes += int(record[7])
    avg_rat = rat / count
    avg_sub = sub / count
    avg_views = views / count
    avg_likes = likes / count
    return count, avg_sub, avg_rat, avg_views, avg_likes

#i'm primarily analyzing them by genre, so isolating that here
GENRES = []
for gen in genre:
    if gen not in GENRES:
        GENRES.append(gen)
GENRES.sort() #to alphabetize

#initializing 5 lists to append the appropriate outputs to
Genre_Counts = []
Genre_Subs = []
Genre_Ratings = []
Genre_Views = []
Genre_Likes = []

#appending appropriate outputs to respective lists
for gen in GENRES:
    print(gen)
    print("Number of Webtoons: ", Genre_Analysis(gen)[0])
    print("Average Subscribers: ", Genre_Analysis(gen)[1])
    print("Average Rating: ", Genre_Analysis(gen)[2])
    print("Average Views: ", Genre_Analysis(gen)[3])
    print("Average Likes: ", Genre_Analysis(gen)[4])
    print("----------------------------------------")
    Genre_Counts.append(Genre_Analysis(gen)[0])
    Genre_Subs.append(Genre_Analysis(gen)[1])
    Genre_Ratings.append(Genre_Analysis(gen)[2])
    Genre_Views.append(Genre_Analysis(gen)[3])
    Genre_Likes.append(Genre_Analysis(gen)[4])

#printing out data for easy reading
#note - highest rating has least # webtoons
print("\nGENRE STATS")
print("----------------------------------------")
print("Total Webtoons: 699")
print("----------------------------------------")
print("Greatest Number of Webtoons: Fantasy = ",  max(Genre_Counts))
print("Least Number of Webtoons: Heartwarming = ",  min(Genre_Counts))
print("----------------------------------------")
print("Highest Average Subs: Romance ",  max(Genre_Subs))
print("Lowest Average Subs: Tiptoon",  min(Genre_Subs))
print("----------------------------------------")
print("Highest Average Rating: Heartwarming ",  max(Genre_Ratings))
print("Lowest Average Rating: Superhero",  min(Genre_Ratings))
print("----------------------------------------")
print("Highest Average Views: Romance ",  max(Genre_Views))
print("Lowest Average Views: Historical",  min(Genre_Views))
print("----------------------------------------")
print("Highest Average Likes: Romance ",  max(Genre_Likes))
print("Lowest Average Likes: Tiptoon",  min(Genre_Likes))
print("----------------------------------------")

"""
MAX & MIN

"""
#max and min - which webtoons had greatest & least subscribers & ratings
W_max_subscribers = ""
W_min_subscribers = ""
for record in records:
    if int(record[4]) == max(subscribers):
        W_max_subscribers = record[1]
for record in records:
    if int(record[4]) == min(subscribers):
        W_min_subscribers = record[1]
         
W_max_rating = ""
W_min_rating = ""
for record in records:
    if float(record[5]) == max(rating):
        W_max_rating = record[1]
for record in records:
    if float(record[5]) == min(rating):
        W_min_rating = record[1]

W_max_views = ""
W_min_views = ""
for record in records:
    if int(record[6]) == max(views):
        W_max_views = record[1]
for record in records:
    if int(record[6]) == min(views):
        W_min_views = record[1]
        
W_max_likes = ""
W_min_likes = ""
for record in records:
    if int(record[7]) == max(likes):
        W_max_likes = record[1]
for record in records:
    if int(record[7]) == min(likes):
        W_min_likes = record[1]
 
#printing out max and min stats for easy reading
print("\nWEBTOON MAX MIN STATS")
print("---------------------------")
print("Max Subs: ", W_max_subscribers)
print("Min Subs: ", W_min_subscribers)
print("---------------------------")
print("Max Rating: ", W_max_rating)
print("Min Rating: ", W_min_rating)
print("---------------------------")
print("Max Views: ", W_max_views)
print("Min Views: ", W_min_views)
print("---------------------------")
print("Max Likes: ", W_max_likes)
print("Min Likes: ", W_min_likes)
print("---------------------------")
 
"""
GRAPHING

"""
#random colors dictionary to color the graph
G = ["ACT","COM","DRA","FAN","HEA","HIS","HOR","MYS",
    "ROM","SF","SLI","SPO","SUP","SPN","THR","TIP"]
c = {}
for g in G:
    c[g] = (random(),random(),random())
colors = []
for g in G:
    rgb = c[g]
    colors.append(rgb)

#the number of bars basically
Webtoons = pylab.arange(len(Genre_Counts))

#graphing the number of webtoons in each genre
pylab.bar(Webtoons,Genre_Counts, 0.5, color = colors)
pylab.xticks(Webtoons, G, fontsize=8.5)
pylab.xlabel('Genre')
pylab.ylabel('Number of Webtoons')
pylab.title('Number of Webtoons in each Genre')
pylab.show()

#graphing average subs
pylab.bar(Webtoons,Genre_Subs, 0.5, color = colors)
pylab.xticks(Webtoons, G, fontsize=8.5)
pylab.xlabel('Genre')
pylab.ylabel('Average Subs')
pylab.title('Average Subscribers of Each Genre')
pylab.show()

#graphing average ratings
pylab.bar(Webtoons,Genre_Ratings, 0.5, color = colors)
pylab.xticks(Webtoons, G, fontsize=8.5)
pylab.xlabel('Genre')
pylab.ylabel('Average Rating')
pylab.title('Average Rating of Each Genre')
pylab.show()
 
#graphing average views
pylab.bar(Webtoons,Genre_Views, 0.5, color = colors)
pylab.xticks(Webtoons, G, fontsize=8.5)
pylab.xlabel('Genre')
pylab.ylabel('Average Views')
pylab.title('Average Views of Each Genre')
pylab.show()

#graphing average likes
pylab.bar(Webtoons,Genre_Likes, 0.5, color = colors)
pylab.xticks(Webtoons, G, fontsize=8.5)
pylab.xlabel('Genre')
pylab.ylabel('Average Likes')
pylab.title('Average Likes of Each Genre')
pylab.show()
 
 
 
 
 
 
