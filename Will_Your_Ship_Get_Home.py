#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 23:00:22 2022

@author: bushra

------------------------------------------------------------------------------
   Name:     BI_IS221_FPP
   Author:   Bushra Ibrahim
   Date:     May 4, 2022
   Language: Python
   Purpose:  The purpose of this program is to model a small spaceship's
             journey in space, and to see whether or not it can get back home!
             (Home being Mission Control in this case, not Earth)
             - Graphics based
             - loops and conditions both used
             - several variables, like circles, rectangles, and polygons
             - signature thing = use of buttons in Python, plus rudimentary
                 animation by drawing, undrawing, and redrawing
------------------------------------------------------------------------------
   ChangeLog:
   
   Who:      Bushra Ibrahim           
   Date:     May 4, 2022
   Desc.:    This is the original version of the code.
------------------------------------------------------------------------------
Notes:
    1. The main change I made from the original plan is that the user
        cannot play the game again. Loop structures are implemented in
        other places in the code, but as it is right now, you can't play again.
        I decided that in order for me to make it replayable the way I want
        it to, it would take more work, another button or two, and more time
        - time which I don't have due to my other finals and projects. So, 
        I decided to stick to a single game.'
        
    2. Loops - loops are involved in the making of the stars in the background, 
        and in redrawing the ship each time it moves.
        
    3. Conditions - conditions are used for when the ship leaves the bounds
        of the window (I make it come back around, like a spherical universe), 
        to check what event is happening (based on the coordinates of the ship),
        and to check if buttons are clicked or not.
"""

#to use for random step choices when the ship moves
import random

#location class to keep track of where things are in the window
class Location(object):
    def __init__(self, x, y):
        """x and y are numbers"""
        self.x, self.y = x, y

    def move(self, deltaX, deltaY):
        """deltaX and deltaY are numbers"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox, oy = other.x, other.y
        xDist, yDist = self.x - ox, self.y - oy
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

#to get and set locations on the window
class Field(object):
    def __init__(self):
        self.Ships = {}
        
    def addShip(self, Ship, loc):
        if Ship in self.Ships:
            raise ValueError('Duplicate Ship')
        else:
            self.Ships[Ship] = loc
            
    def moveShip(self, Ship):
        if Ship not in self.Ships:
            raise ValueError('Ship not in field')
        xDist, yDist = Ship.takeStep()
        currentLocation = self.Ships[Ship]
        #use move method of Location to get new location
        self.Ships[Ship] = currentLocation.move(xDist, yDist)
        
    def getLoc(self, Ship):
        if Ship not in self.Ships:
            raise ValueError('Ship not in field')
        return self.Ships[Ship]
    
    def setLoc(self,Ship,loc):
        self.Ships[Ship]=loc
        
#creating a ship class so that I can make multiple ship objects
class Ship(object):
    def __init__(self, name = None):
        """Assumes name is a str"""
        self.name = name

    def __str__(self):
        if self != None:
            return self.name
        return 'Anonymous'

#making the 4 ships that the user can choose from when playing
class Endurance(Ship): #tends to move towards Gargantua (courtesy of Interstellar)
    def takeStep(self):
        stepChoices = [(0,2), (2,0), (1,0), (0, 1)]
        return random.choice(stepChoices)

class MilleniumFalcon(Ship): #ship that moves over larger distances faster
    def takeStep(self):
        stepChoices = [(0,-3), (0,2), (2, 0), (3, 0), (3.2,0.0), (0,-4)]
        return random.choice(stepChoices)

class Tardis(Ship): #ship that moves erratically, inseveral directions
    def takeStep(self):
        stepChoices = [(-1.0, 0.0), (1.0, 1.0),(2.0,-1.0),(0.0,-2.5)]
        return random.choice(stepChoices)
    
class USSEnterprise(Ship): #ship that tends to move towards the supernova
    def takeStep(self):
        stepChoices = [(0, 1), (-2,0),(-1,0),(0,2)]
        return random.choice(stepChoices)

#-------------------------------------------------------------------------------
#Animations

#importing button stuff so that I can make buttons
from button import *

#creating the base window and making it a dark blue color to resemble space
win = GraphWin("Will your ship get home?", 600, 600)
win.setCoords(-50,-50,50,50)
win.setBackground(color_rgb(20,15,45))

#creating random stars in the background
for i in range(250):
    newStar = Circle(Point(random.randint(-50,50),random.randint(-50,50)),0.25)
    newStar.draw(win)
    newStar.setFill("white")

#basic instructions
ChooseShipText = Text(Point(0,45),"Select a ship to run a mission!")
ChooseShipText.draw(win)
ChooseShipText.setTextColor("white")
ChooseShipText.setFace("arial")
ChooseShipText.setSize(25)

#creating 4 buttons, each a ship to simulate
EnduranceButton = Button(win,Point(-2,10),18,5,"Endurance")
EnduranceButton.activate()

MilleniumFalconButton = Button(win,Point(24,10),26,5,"Millenium Falcon")
MilleniumFalconButton.activate()

TardisButton = Button(win,Point(-23,10),16,5,"Tardis")
TardisButton.activate()

USSEnterpriseButton = Button(win,Point(0,3),24,5,"USS Enterprise")
USSEnterpriseButton.activate()

#looping until a button is actually clicked
butClick = False
while (butClick == False):
    
    p = win.getMouse()
    
    if EnduranceButton.clicked(p):
        Ship = Endurance('Rango')
        EnduranceButton.deactivate()
        butClick = True
        
        
    elif MilleniumFalconButton.clicked(p):
        Ship = MilleniumFalcon("Rango")
        MilleniumFalconButton.deactivate()
        butClick = True
        
    elif TardisButton.clicked(p):
        Ship = Tardis("Rango")
        TardisButton.deactivate()
        butClick = True
        
    elif USSEnterpriseButton.clicked(p):
        Ship = USSEnterprise("Rango")
        USSEnterpriseButton.deactivate()
        butClick = True
    
#making space a field object, so i can do location stuff with it
space = Field()

#this is where the ship will start its journey
startLoc = Location(0,-41)

#making a little house icon for Mission Control
MissionControlLoc = Location(12,10)
MissionControlText = Text(Point(15,8),"Mission Control")
MissionControlText.draw(win)
MissionControlText.setTextColor("white")
MissionControl = Rectangle(Point(10,10),Point(14,14))
MissionControl.setFill("lightgrey")
roof = Polygon(Point(10,14),Point(12,17),Point(14,14))
roof.setFill("blue")
door = Rectangle(Point(12,10),Point(13,12))
door.setFill("black")
roof.draw(win)
MissionControl.draw(win)
door.draw(win)

#creating Gargantua, a black hole
BHLoc = Location(30,-10)
BH = Circle(Point(30,-10),10)
BH.setFill("black")
BH.setOutline("white")
BHText = Text(Point(30,-10),"Gargantua")
BHText2 = Text(Point(30,-13),"a black hole")
BHText.setTextColor("white")
BHText2.setTextColor("grey")
BH.draw(win)
BHText.draw(win)
BHText2.draw(win)

#creating a supernova (expressed by a polygon and an explosion radius)
SupernovaLoc = Location(-24,20)
SNRadius = Circle(Point(-24,22),15)
SNRadius.setFill("orange")
Supernova = Polygon(Point(-40,30),Point(-25,25),Point(-20,40),Point(-21,26),
                     Point(-10,32),Point(-13,21),Point(-5,18),Point(-17,17),
                     Point(-16,7),Point(-27,15),Point(-35,10),Point(-30,20),
                     Point(-40,30))
Supernova.setFill("red")
Supernova.setOutline("yellow")
SupernovaText = Text(Point(-24,20),"Supernova")
SupernovaText.setTextColor("white")
SNRadius.draw(win)
Supernova.draw(win)
SupernovaText.draw(win)

#adding a ship object officially at the start location
space.addShip(Ship,startLoc)

#undrawing all the texts so the game can begin on a clear screen
#with the obstacles in place
ChooseShipText.undraw()
EnduranceButton.rect.undraw()
EnduranceButton.label.undraw()
MilleniumFalconButton.rect.undraw()
MilleniumFalconButton.label.undraw()
TardisButton.rect.undraw()
TardisButton.label.undraw()
USSEnterpriseButton.rect.undraw()
USSEnterpriseButton.label.undraw()

#creating the ship - it's a small circle
ShipFig = Circle(Point(0,-41), 1)
ShipFig.setFill('grey')
ShipFig.draw(win)

#creating a planet where the ship crashed
PlanetX = Circle(Point(0,-45), 3)
PlanetX.setFill("green")
PlanetX.draw(win)
PlanetXText = Text(Point(0,-45),"X")
PlanetXText.setTextColor("white")
PlanetXText.draw(win)

StartText = Text(Point(0,45),"Click anywhere to begin your mission!")
StartText.setTextColor("white")
StartText.setSize(20)
StartText.draw(win)

win.getMouse()
StartText.undraw()

#the default event is normal - it will change based on the conditions I mention
#a couple lines below
event = "normal"

#drawing and redrawing the ship to create the illusion of movement
for i in range(200): 
    x1 = space.getLoc(Ship).getX()
    y1 = space.getLoc(Ship).getY()
    space.moveShip(Ship)
    x = space.getLoc(Ship).getX()
    y = space.getLoc(Ship).getY()
    path = Line(Point(x1,y1),Point(x,y))
    path.setFill("yellow")
    time.sleep(0.1)
    ShipFig.undraw()
    ShipFig = Circle(Point(x,y),1)
    ShipFig.setFill('grey')
    ShipFig.draw(win)
    path.draw(win)
    
    #so the ship comes back around if it leaves the bounds of the window
    if space.getLoc(Ship).getX()< -50:
        space.setLoc(Ship, Location(50,space.getLoc(Ship).getY()))
    if space.getLoc(Ship).getY()< -50:
        space.setLoc(Ship, Location(space.getLoc(Ship).getX(),50))    
    if space.getLoc(Ship).getX()> 50:
        space.setLoc(Ship, Location(-50,space.getLoc(Ship).getY()))
    if space.getLoc(Ship).getY()> 50:
        space.setLoc(Ship, Location(space.getLoc(Ship).getX(),-50))
    
    #Supernova area is breached, so ship dies
    if (-39 <= x <= -9) and (7 <= y <= 37):
        event = "incinerated"
        break
    
    #Mission Control area is breached, so ship made it home  
    if (10 <= x <= 14) and (10 <= y <= 14):
        event = "made it home"
        break
    
    #Gargantua area is breached, so ship is spaghettified
    if BHLoc.distFrom(space.getLoc(Ship)) < 10:
        event = "spaghettification"
        break
    
#printing a statement based on where the ship ended up
if event == 'incinerated':
    supernovaText=Text(Point(0,-25),"The Ship got incinerated by the Supernova!\n" + "Hot damn!")
    supernovaText.setTextColor("lightblue")
    supernovaText.setSize(20)
    supernovaText.draw(win)
    
elif event == "made it home":
    madeItText=Text(Point(0,-25),"The Ship made it back Mission Control!\n" + "Welcome home!")
    madeItText.setTextColor("lightblue")
    madeItText.setSize(20)
    madeItText.draw(win)
    
elif event == "spaghettification":
    suckedText = Text(Point(0,-25),"Gargantua's gravity has sucked in the Ship!\n" + "You're officially spaghettified!")
    suckedText.setTextColor("lightblue")
    suckedText.setSize(20)
    suckedText.draw(win)

else: #in case the ship didn't run into any obstacles, and didn't make it home either
    distance = round(MissionControlLoc.distFrom(space.getLoc(Ship)),2)
    distText=Text(Point(0,-25),"The Ship crashed out " + str(distance/10) + " lightyears from Mission Control!\n" + "Too bad!")
    distText.setTextColor("lightblue")
    distText.setSize(20)
    distText.draw(win)

CloseText = Text(Point(0,45),"Click anywhere to end the mission!")
CloseText.setTextColor("white")
CloseText.setSize(20)
CloseText.draw(win)

#closing the window with a click
win.getMouse()
win.close()







