from cmu_graphics import *
from functions import *
from variables import *
from animation import *


def enemySpawn(x,y,enemyName):
    for enemy in enemies:
        if enemy.name == enemyName:
            enemy.timer = 60
            enemy.centerX = x
            enemy.centerY = y
            enemy.active = True
            nearDeathAnimationStart(False)

def enemySelect(enemyName):
    for enemy in enemies:
        if enemy.name == enemyName:
            return enemy
    return None

# BEHAVIOUR

#Randomspawn

def enemyRandom():
    if app.counter%400 == 0: #400
        enemySpawn(randrange(130,250),150,"enemy1")
        nearDeathAnimationStart(False)
        
        c = enemySelect("enemy1")
        print(distance(c.centerX, c.centerY, 200,230))
        #print("spawned")

def enemyBehav():

    for enemy in enemies:
        if enemy.behav == "agressive":
                enemySpeed = 80

                if enemy.centerX > 200:
                    enemy.centerX += enemySpeed
                if enemy.centerX < 200:
                    enemy.centerX -= enemySpeed

                if enemy.centerY > 230:
                    enemy.centerY -= enemySpeed
                if enemy.centerY < 230:
                    enemy.centerY += enemySpeed
                print(enemy.centerX, enemy.centerY)

    for enemy in enemies:

        #print(enemy.name,enemy.timer)
        if enemy.active == True:


            if enemy.name == "enemy1":
                if enemy.timer <= 0:
                    if app.sonar:
                        enemy.behav = "aggressive"
                        print("ATTACK")
                        enemySpeed = 5

                        if enemy.centerX > 200:
                            enemy.centerX -= enemySpeed
                        if enemy.centerX < 200:
                            enemy.centerX += enemySpeed

                        if enemy.centerY > 230:
                            enemy.centerY -= enemySpeed
                        if enemy.centerY < 230:
                            enemy.centerY += enemySpeed
                        #print(enemy.centerX, enemy.centerY)
                    
                enemy.timer -= 1

                if distance(enemy.centerX, enemy.centerY, 200,230) > 145:
                    enemy.active = False
                    if enemy.active == False:
                        nearDeathAnimationStart(True)
                    
                    enemy.centerY = 500
                    enemy.timer = 100
                elif enemy.behav == "passive":
                    enemy.centerY += 1
                    
                
                
                    
                    

                #if dist > radar > inactive

                
            
        
        #print(enemy.name,enemy.timer,enemy.behav)

   

