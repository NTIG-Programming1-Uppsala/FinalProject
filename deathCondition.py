from cmu_graphics import *
from variables import enemies
from functions import *
def deathCond():
    for enemy in enemies:

        if distance(enemy.centerX, enemy.centerY, 200,230) < 30:
            Rect(0,0,400,400)
            Label("you died)",200,200,size=20,fill="white")
            app.stop()