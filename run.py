from textwrap import fill
from turtle import width
from cmu_graphics import *
import math

from variables import *
from functions import  *
from enemySpawn import *

for block in blocks:
    
    block.toBack()
    ship.toBack()
    

###game start

def onStep():
    everyFrame()
    enemyBehav()

startMenu(False)

for colour in colours:
    moveKey(player.centerX,player.centerY,colour)
    if (colour == "yellow"):
        moveKey(player.centerX,player.centerY+5000,colour)
    
    itemPickup()


#Makedot is a function that actually creates the monster
makeDot(850,200,"enemy1")

#adds an event that moves the monster to the player

#enemySpawn(270,200,"enemy1")

cmu_graphics.run()
