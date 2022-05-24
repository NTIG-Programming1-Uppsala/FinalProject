from textwrap import fill
from turtle import width
from cmu_graphics import *
from playsound import playsound
import math

from variables import *
from functions import  *
from enemySpawn import enemyBehav

for block in blocks:
    
    block.toBack()
    ship.toBack()
    

###game start

def onStep():
    everyFrame()
    enemyBehav()

startMenu(False)

for colour in colours:
    moveKey(77,500,colour)

makeDot(250,200,"enemy1")
#makeDot(150,200,"enemy")

cmu_graphics.run()
