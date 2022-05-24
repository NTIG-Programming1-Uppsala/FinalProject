from cmu_graphics import *
from functions import *
from variables import *



def enemySpawn(x,y,enemyName):
    for enemy in enemies:
        if enemy.name == enemyName:
            enemy.timer = 100
            enemy.centerX = x
            enemy.centerY = y
            enemy.active = True

# BEHAVIOUR

#Randomspawn

def enemyRandom():
    if app.counter%400 == 0: #400
        enemySpawn(randrange(130,250),150,"enemy1")
        print("spawned")

def enemyBehav():

    for enemy in enemies:
        if enemy.behav == "agressive":
                enemySpeed = 50

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

                if distance(enemy.centerX, enemy.centerY, 200,230) > 146:
                    enemy.active = False
                    enemy.centerY = 500
                    enemy.timer = 100
                elif enemy.behav == "passive":
                    enemy.centerY += 1
                    
                
                
                    
                    

                #if dist > radar > inactive

                
            
        
        #print(enemy.name,enemy.timer,enemy.behav)

    pass

