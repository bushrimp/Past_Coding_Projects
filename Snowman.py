#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 18:22:00 2022

@author: bushra

------------------------------------------------------------------------------
   Name:     BI_IS221_PP_3_10
   Author:   Bushra Ibrahim
   Date:     Apr 20, 2022
   Language: Python
   Purpose:  The purpose of this program is to draw a Snowman based on
             the edits mentioned in PP 3.10.
------------------------------------------------------------------------------
   ChangeLog:
   
   Who:      Bushra Ibrahim           
   Date:     Apr 20, 2022
   Desc.:    This is the original version of the code.
------------------------------------------------------------------------------

"""


from graphics import *

win = GraphWin('Snowman',500,500)
win.setCoords(-100,-100,100,100)
win.setBackground('light blue')

rctGround = Rectangle(Point(-100, -50), Point(100,-100))
rctGround.setFill('dark blue')
rctGround.setOutline('dark blue')
rctGround.draw(win)

crcSun = Circle(Point(75,60), 15)
crcSun.setFill('gold')
crcSun.setOutline('gold')
crcSun.draw(win)

crcSnow1 = Circle(Point(30,-25), 35)
crcSnow1.setFill('white')
crcSnow1.setOutline('white')
crcSnow1.draw(win)

crcSnow2 = Circle(Point(30,15), 25)
crcSnow2.setFill('white')
crcSnow2.setOutline('white')
crcSnow2.draw(win)

crcButton1 = Circle(Point(30,25), 2.5)
crcButton1.setFill('red')
crcButton1.setOutline('red')
crcButton1.draw(win)
crcButton1 = Circle(Point(30,15), 2.5)
crcButton1.setFill('red')
crcButton1.setOutline('red')
crcButton1.draw(win)
crcButton1 = Circle(Point(30,5), 2.5)
crcButton1.setFill('red')
crcButton1.setOutline('red')
crcButton1.draw(win)


crcSnow3 = Circle(Point(30, 50), 15)
crcSnow3.setFill('white')
crcSnow3.setOutline('white')
crcSnow3.draw(win)

crcEye1 = Circle(Point(25,55), 3)
crcEye1.setFill('black')
crcEye1.setOutline('black')
crcEye1.draw(win)
crcEye1 = Circle(Point(35,55), 3)
crcEye1.setFill('black')
crcEye1.setOutline('black')
crcEye1.draw(win)

lnSmile = Line(Point(25,45),Point(35,45))
lnSmile.setFill('black')
lnSmile.draw(win)

lnArm1 = Line(Point(15,15),Point(-10,25))
lnArm1.setFill('black')
lnArm1.draw(win)

lnArm2 = Line(Point(45,15),Point(70,25))
lnArm2.setFill('black')
lnArm2.draw(win)

txtName = Text(Point(-45,70),'Bushra Ibrahim')
txtName.setFill('white')
txtName.draw(win)

rctHat1 = Rectangle(Point(10, 62), Point(50,60))
rctHat1.setFill('black')
rctHat1.setOutline('black')
rctHat1.draw(win)

rctHat2 = Rectangle(Point(20, 80), Point(40,60))
rctHat2.setFill('black')
rctHat2.setOutline('black')
rctHat2.draw(win)


win.getMouse()
win.close()

