from cmu_graphics import *
from functions import *
from variables import *



def enemySpawn(x,y,enemyName):
    for enemy in enemies:
        if enemy.name == enemyName:
            enemy.centerX = x
            enemy.centerX = y
            enemy.active = True

# BEHAVIOUR

def enemyBehav():
    for enemy in enemies:
        #print(enemy.name,enemy.timer)
        if enemy.active == True:
            if enemy.name == "enemy1":
                if enemy.timer <= 1:
                    if player.dy > 1 or player.dx > 1:
                        enemy.behav = "aggressive"
                        print("ATTACK")
                    enemy.timer = 100
                #if dist > radar > inactive

                
            
        enemy.timer -= 1
        print(enemy.name,enemy.timer)

    pass

