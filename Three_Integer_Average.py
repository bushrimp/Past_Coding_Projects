#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 00:01:37 2022

@author: bushra

------------------------------------------------------------------------------
   Name:     BI_IS221_PP_2_2
   Author:   Bushra Ibrahim
   Date:     Apr 13, 2022
   Language: Python
   Purpose:  The purpose of this program is to take 3 integer inputs
             and print back their average.
------------------------------------------------------------------------------
   ChangeLog:
   
   Who:      Bushra Ibrahim           
   Date:     Apr 13, 2022
   Desc.:    This is the original version of the code.
------------------------------------------------------------------------------

"""

# 2.2
# Write a program that reads three integers and prints their average.

def BI_IS221_PP_2_2():
    print("\nThis program takes three integers you enter and prints their average.\n")

    blInt1 = False
    blInt2 = False
    blInt3 = False
    
    while blInt1 is False:
        intOne = input("Please enter your first integer: ")
        try:
            i = int(intOne)
            if type(i) == int:
                blInt1 = True
                break
        except ValueError:
            print("That was not an integer, please try again.")
    
    while blInt2 is False:
        intTwo = input("Please enter your second integer: ")
        try:
            i = int(intTwo)
            if type(i) == int:
                blInt2 = True
                break
        except ValueError:
            print("That was not an integer, please try again.")
            
    while blInt3 is False:
        intThree = input("Please enter your third integer: ")
        try:
            i = int(intThree)
            if type(i) == int:
                blInt3 = True
                break
        except ValueError:
            print("That was not an integer, please try again.")
            
    fltAvg = (int(intOne) + int(intTwo) + int(intThree)) / 3
    
    print("\nYour average is: ", fltAvg)

BI_IS221_PP_2_2()

