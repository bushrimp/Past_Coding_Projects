#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 00:20:32 2022

@author: bushra

------------------------------------------------------------------------------
   Name:     BI_IS221_PP_2_4
   Author:   Bushra Ibrahim
   Date:     Apr 15, 2022
   Language: Python
   Purpose:  The purpose of this program is take a user's name, age, college
             and pet's name, then print out some sentences with that info.'
------------------------------------------------------------------------------
   ChangeLog:
   
   Who:      Bushra Ibrahim           
   Date:     Apr 15, 2022
   Desc.:    This is the original version of the code.
------------------------------------------------------------------------------

"""

# 2.4
# Write a program that prompts for and reads a person’s name, age, college, and pet’s name. Then print the following paragraph, inserting the appropriate data:
    # Hello, my name is name and I am age years old. 
    # I’m enjoying my time at college, though
    # I miss my pet petname very much!

def BI_IS221_PP_2_4():
    print("Hello, this program prompts you for your name, age, college, and pet’s name. Then, it will print back a few sentences that you might say!")
        
    strName = input("Please enter your name: ")  
    intAge = input("Please enter your age: ")
    strCollege = input("Please enter your college name: ")
    strPet = input("Please enter your pet's name: ")
    
    print("\nGreat! Here are the sentences: \n")
    
    print("Hello, my name is ", strName, " and I am ", intAge," years old.")
    print("I’m enjoying my time at ", strCollege," though I miss my pet ", strPet," very much!")
    
BI_IS221_PP_2_4()


