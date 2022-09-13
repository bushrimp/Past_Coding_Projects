#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 16:58:00 2021

@author: bushra
"""

#Bushra Ibrahim
#CS337 Final Exam
#Part A; 2

import math

# f = sin(2x+4)-cos(5x)-3x^+8

a = 0
b = 2
E = 0.001

def Bisection(a, b, E): # takes the interval from [a,b] and the desired absolute error, E
    
    def f(x): # just evaluating the function, cuz who wants to do that ew
        f = ((math.sin((2*x)+4))-(math.cos(5*x))-(3*((x)**2))+8) #using math for sin & cos
        return f
    
    calc_error = abs(b-a) #start calculating error
    iterations = 0 #initializing iterations
    
    while calc_error > E: #while our calc_error is still greater than our desired error, E...
        
        c = ((a+b)/2) # bisecting the section to hone in on root
        
        iterations += 1 # iteration counter
        
        if f(c) < 0: # I'm keeping it < and >, real simple...
            b = c
            calc_error = abs(b-a) # update current level of error
            
        elif f(c) > 0: # ...since the given interval is positive
            a = c
            calc_error = abs(b-a) # update current level of error
        else:
            print('no man can walk out on his own story')
            #just something to print when I was testing, in case there was a problem
            
    return  c, iterations # returning root and # of iterations

print('Bisection Method:', Bisection(a, b, E),'\n')

def FalsePosition(a, b, E): # takes the interval from [a,b] and the desired absolute error, E
    
    def f(x):
        f = ((math.sin((2*x)+4))-(math.cos(5*x))-(3*((x)**2))+8) # again, just evaluating
        return f
    
    iterations = 0 # initializing iterations
    
    C = (a*f(b)-b*f(a))/(f(b) - f(a)) # finding secant line
    
    calc_error = abs(C-0) #initial error
    
    while calc_error > E: #while our calc_error is still greater than our desired error, E...
        
        c = (a*f(b)-b*f(a))/(f(b) - f(a)) #to keep calculating c as we go
        
        iterations +=1 # keeping count of iterations
        
        if f(c) < 0:
            calc_error = abs(c-b) # update current level of error
            b = c # replace b with what c was, after the error was calculated
                  # because otherwise it would just be 0
            
        if f(c) > 0:
            calc_error = abs(c-a) # update current level of error
            a = c # same deal here
        
        else:
            print('no man can walk out on his own story')
            #just something to print when I was testing, in case there was a problem
            
    return c, iterations # returning root and # of iterations
            
print('False Position Method:', FalsePosition(a, b, E))




            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            