from textwrap import fill
from turtle import width
from cmu_graphics import *
from playsound import playsound
import math

from variables import *
from functions import  *

for block in blocks:
    
    block.toBack()
    ship.toBack()
    

###game start

def onStep():
    everyFrame()

startMenu(False)

for colour in colours:
    moveKey(77,500,colour)

cmu_graphics.run()
