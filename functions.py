from cmu_graphics import *
from variables import *
from textwrap import fill
from turtle import width
from playsound import playsound
import math

def pickup(item):
    if app.inventory < 5:
        item.centerX = blocks[app.blockindexselected].centerX
        item.centerY = blocks[app.blockindexselected].centerY
        item.slotPos = app.blockindexselected
        item.isPickedUp = True
        app.blockindexselected += 1
        app.inventory += 1
    else:
        print("full inventory")
        

 
            
    
    

def startMenu(bool):
    
    app.paused = bool
    instructions.visible = bool
    instructions.toFront()

def keyUpdatePos():
    
    for key in keys:
        if key.isPickedUp:
            key.centerX = blocks[key.slotPos].centerX
            key.centerY = blocks[key.slotPos].centerY

def itemMove(key):
    if key == "d":
        change = 1
    elif key == "a":
        change = -1
    
    
    
    for key in keys:
        if key.isPickedUp:
            if change > 0:
                key.slotPos += change
                if key.slotPos == app.inventory:
                    key.slotPos = 0
                
                
                
            else:
                key.slotPos += change
                if key.slotPos == -1:
                    key.slotPos = app.inventory-1
                
                
                
                elif key.slotPos >= app.inventory:
                    key.slotPos = 0
            
            
            keyUpdatePos()
            


def itemRemove(index):
    a = False
    for key in keys:
        if key.isPickedUp:
            if key.slotPos == index:
                key.visible = False
                key.isPickedUp = False
                ###return key                ###IT STOPS HERE IF IN USE
            if key.slotPos > index:
                key.slotPos -=1
                
            keyUpdatePos()
    #return None
    app.inventory -= 1
    app.blockindexselected -= 1
    
def getZeroItem():
    for key in keys:
        if key.isPickedUp and key.slotPos == 0:
            return key
    
    

def powerUse(item):
    
    if item.color == "yellow":
        speed.visible = True
        speed.time = 300
        speed.active = True
    elif item.color == "pink":
        jump_hud.visible = True
        jump_hud.time = 300
        jump_hud.active = True
    else:
        player_square.fill = item.color


def itemUse(index):
    for key in keys:
        if key.isPickedUp:
            if key.slotPos == index:
                powerUse(key)

def itemDrop():
    
            
            ### ITEM REMOVE AND THEN GET RETURN VALUE
    
    c = getZeroItem()
    if c != None:
        itemRemove(0)
        c.visible = True
        c.centerX = player.centerX
        c.centerY = player.centerY+20
    
    
    
    
    

def itemPickup():
    for key in keys:
        if key.hitsShape(player) and key.isPickedUp == False:
            pickup(key)

### MOVEMENT
  
def moveKey(x,y,color):
        for key in keys:
            if key.color == color:
                key.centerX = x
                key.centerY = y


def jump():
    if player.jump > 0:
        player.dy -= player.jumpPower
        player.jump -= 1

def makeDot(x,y,attr):
    c = Group()
    c.target = attr
    for i in range(10):
        a = Circle(x,y,1+i*4,fill="limeGreen",opacity=100-i*10)
        a.o_opacity = a.opacity
        c.add(a)
        
    if c.centerX > 200-c.centerX:
        pass

    enemies.append(c)

### ENEMY SPAWN

makeDot(250,200,"enemy")
makeDot(150,200,"enemy2")


def onKeyPress(key):
    
    if key == "a" or key == "d":
        itemMove(key)
    if key == "w":
        itemUse(0)
        itemRemove(0)
        
        
    if key == "r":
        startMenu(False)
    if key == "z":
        itemDrop()
    if key == "y":
        c = getZeroItem()
        
    
        


def onKeyHold(keys):
    app.limit = 8
    if "right" in keys:
        if player.dx < app.limit:
            player.dx += player.speed
            
    if "left" in keys:
        if player.dx > -app.limit:
            player.dx -= player.speed
        
    if "up" in keys:
        player.dy -= player.speed
    
    if "down" in keys:
        
        player.dy += player.speed
    if "x" in keys:
        itemPickup()
    
def powersActive():
    
    if speed.active:
        
        app.limit = 100
        player.speed = 30
        
    else:
        app.limit = 8
        player.speed = 2
    
    if jump_hud.active:
        player.jumpPower = 50
    else:
        player.jumpPower =  2

def enemyUpdate():
    detect = 1
    for enemy in enemies:
        enemy.centerX -= player.dx
        enemy.centerY -= player.dy
        #print(distance(enemy.centerX,enemy.centerY,200,230))
        if 145 > distance(enemy.centerX,enemy.centerY,200,230):
            for shape in enemy.children:
                if shape.opacity > 1:
                    shape.opacity -= detect
        else:
            for shape in enemy.children:
               
                shape.opacity = 0
            
        
        

def sonarMove():
    speed = 5
    sonarLine.rotateAngle += speed

def sonarDetect():
    for enemy in enemies:
        if sonarLine.hits(enemy.centerX,enemy.centerY):
            
            for shape in enemy:
                shape.opacity = shape.o_opacity

### SUB HUD

ship.silentHud = Rect(0,0,400,400,fill="black",opacity=100,visible=False)
blackscreen = Rect(0,0,400,400,fill="black",opacity=50,visible=False)

def hitButton(color):
    for button in buttons:
        if color == "red":
            if ship.silent == True:
                ship.silent = False
                ship.silentHud.visible = False
            elif ship.silent == False:
                ship.silent = True
                ship.silentHud.toFront()
                ship.silentHud.visible = True
            print(ship.silent)




def onMousePress(mouseX,mouseY):
    for button in buttons:
        if button.hits(mouseX,mouseY):
            print(button.fill," hit!")
            hitButton(button.thing)
    print(mouseX,mouseY)
    


def everyFrame():
    #print(player.dx, player.dy)
    app.counter3 += 1
    
    if player.dy > 0:
        player.dy -= friction*player.dy
    elif player.dy < 0:
        player.dy -= friction*player.dy

    if player.dx > 0:
        player.dx -= friction*player.dx
    elif player.dx < 0:
        player.dx -= friction*player.dx
    sonarMove()
    enemyUpdate()
    sonarDetect()

    
    powersActive()
    
    player.centerX += player.dx
    player.centerY += player.dy
    
    for key in keys:
        if key.isPickedUp == False:
            change = math.sin(app.counter2%360)
            key.centerY += change*0.09
    
    for hu in hud:
        
        if hu.active == True:
            hu.time -= 1
        if hu.time <= 0:
            hu.active = False
            hu.visible = False
            
    
    for obstacle in obstacles:
        if player.hitsShape(obstacle) and player.bottom > obstacle.top:
            
            player.jump = 5
            player.floor = True
            player.dy = 0
            player.bottom = obstacle.top
            if player.dx > 0:
                player.dx -= 1
            elif player.dx < 0:
                player.dx += 1
        
    
    
    
    
    
    
    
    
    ### WALL COLLISION
    
    
    ###animation
    
    app.counter +=1
    app.counter2 += 4
    
    if app.counter%12 == 0:
        if selected.anim == 0:
            selected.border = rgb(247,138,238)
                
        for hu in hud:
                if hu.active == True and hu.time <= app.hudtimer:
                    hu.visible = False
            
        if selected.anim == 1:
            selected.border = rgb(245,171,239)
            
            for hu in hud:
                if hu.active == True and hu.time <= app.hudtimer:
                    hu.visible = True
                
        if selected.anim == 2:
            selected.border = rgb(245,131,239)
            
            for hu in hud:
                if hu.active == True and hu.time <= app.hudtimer:
                    hu.visible = False
        
        selected.anim += 1
        if selected.anim > 2:
            selected.anim= 0
