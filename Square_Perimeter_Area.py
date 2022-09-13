#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 00:35:39 2022

@author: bushra

------------------------------------------------------------------------------
   Name:     BI_IS221_PP_2_12
   Author:   Bushra Ibrahim
   Date:     Apr 15, 2022
   Language: Python
   Purpose:  The purpose of this program is to take the side length of a square
             from the user, and print back the square's perimeter and area.'
------------------------------------------------------------------------------
   ChangeLog:
   
   Who:      Bushra Ibrahim           
   Date:     Apr 15, 2022
   Desc.:    This is the original version of the code.
------------------------------------------------------------------------------

"""
# 2.12
# Write a program that prompts for and reads an integer representing the length of a square’s side, then prints the square’s perimeter and area.

print("This program will take an integer from you that is the length of a side of a square.")
print("Then, it will give you that square's perimeter and area.")

blSide = False
    
while blSide is False:
    intSide = input("Please enter the length of a side of your square: ")
    try:
        i = int(intSide)
        if type(i) == int:
            blSide = True
            break
    except ValueError:
        print("That was not an integer, please try again.")
        
intPeri = (int(intSide)) * 4
intArea = (int(intSide)) ** 2

print("\nThe perimeter of your square is: ", intPeri)
print("The area of your square is: ", intArea)
