from cmu_graphics import *
from finalProject.py import *

def onStep():
    everyFrame()

startMenu(False)

for colour in colours:
    moveKey(77,500,colour)




cmu_graphics.run()