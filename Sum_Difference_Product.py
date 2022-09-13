#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 00:09:33 2022

@author: bushra

------------------------------------------------------------------------------
   Name:     BI_IS221_PP_2_3
   Author:   Bushra Ibrahim
   Date:     Apr 15, 2022
   Language: Python
   Purpose:  The purpose of this program is to take two floating point numbers 
             you enter and print their sum, difference, and product.
------------------------------------------------------------------------------
   ChangeLog:
   
   Who:      Bushra Ibrahim           
   Date:     Apr 15, 2022
   Desc.:    This is the original version of the code.
------------------------------------------------------------------------------

"""

# 2.3
# Write a program that reads two floating point numbers and prints their sum, difference, and product.

def BI_IS221_PP_2_3():
    
    print("\nThis program takes two floating point numbers you enter and prints their sum, difference, and product.\n")
    
    blFlt1 = False
    blFlt2 = False
    
    while blFlt1 is False:
        fltOne = input("Please enter your first float: ")
        try:
            i = float(fltOne)
            if type(i) == float:
                blFlt1 = True
                break
        except ValueError:
            print("That was not a float, please try again.")
    
    while blFlt2 is False:
        fltTwo = input("Please enter your second float: ")
        try:
            i = float(fltTwo)
            if type(i) == float:
                blFlt2 = True
                break
        except ValueError:
            print("That was not a float, please try again.")
            
    fltSum = float(fltOne) + float(fltTwo)
    fltDiff = float(fltOne) - float(fltTwo)
    fltProd = float(fltOne) * float(fltTwo)
    
    print("\nThe sum of your two floats is: ", fltSum)
    print("The difference of your two floats is: ", fltDiff)
    print("The product of your two floats is: ", fltProd)
    
BI_IS221_PP_2_3()
