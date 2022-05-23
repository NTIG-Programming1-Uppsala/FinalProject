from textwrap import fill
from turtle import width
from cmu_graphics import *
from playsound import *
from cmu_graphics import Sound
import math

from cmu_graphics import Sound




### inventory management through using list.pop as a value and list.append

obstacles = Group()
obstacles.color = rgb(206,230,242)
app.counter = 0
app.counter2 = 0
friction = 0.2
enemies = []
'''
note = Sound("https://s3.amazonaws.com/cmu-cs-academy.lib.prod/sounds/tada.mp3")
note.play()'''

#obstacles.color.player = rgb(206,230,242)

##import sound, images, scripts


#https://stackoverflow.com/questions/20309456/call-a-function-from-another-file

###circular list!

### INSTRUCTIONS
arrowinstr = Image("Images/metal_rusty.jpg",50,50)
arrowinstr.width *= 0.1
arrowinstr.height *= 0.1
arrowinstr.centerX = 200
arrowinstr.centerY = 260
black = Rect(0,0,400,400)
instr1 = Label("instructions",200,70,fill="white",size=30)
instr2 = Label("Use A, D to switch between items",200,instr1.centerY+50,fill="white",size=20)
instr3 = Label("W to use the item",200,instr1.centerY+70,fill="white",size=20)
instr4 = Label("z to drop and x to pick up items",200,instr1.centerY+90,fill="white",size=15)
instr5 = Label("Press r to start",200,arrowinstr.bottom+10,fill="white",size=20)
instructions = Group(black,instr1, instr2,instr3, instr4,instr5,arrowinstr)

### HUD
speed = Rect(50,50,50,50)
jump_hud = Image("https://cdn.discordapp.com/attachments/877485859086172180/968157388270075965/pngegg_1.png",50,50)
jump_hud.width *=0.07
jump_hud.height *=0.07
speed.width *=0.2
speed.height *=0.2
jump_hud.centerX = 20
jump_hud.centerY = 70
speed.centerX = jump_hud.centerX + 40
speed.centerY = jump_hud.centerY
app.hudtimer = 100
hud = [speed,jump_hud]
app.counter3 = 0

for hu in hud:
    hu.time = 0
    hu.visible = False
    hu.active = False
### BUTTONS

buttons = []

redButton = Circle(37,110,20,fill="red")
redButton.thing = redButton.fill
buttons.append(redButton)
print(buttons)





### PLAYER
player_square = Rect(200,200,40,40,fill=None)
player_text = Label("",200,150)
player = Group()
player_text.centerX = player_square.centerX
player.add(player_square, player_text)
player.dy = 0
player.dx = 0
player.speed = 2
player.floor = False
player.jump = 5
player.jumpPower = 2
gravity = 0.8



ship = Image("Images/metal_rusty.jpg",0,0)
ship.width = 400
ship.height = 400

### SHIP PROPERTIES

ship.silent = False
ship.silentHud = Rect(0,0,400,400,fill="red",opacity=50,visible=False)

### RADAR GRAPHICS
radar = Group()

radar_c = Circle(200,230,150,fill=gradient("gray","black"))
radar.add(radar_c)
for i in range(7):
    if i == 6:
        c = Circle(radar.centerX,radar.centerY,(50*i)/2+1,fill=None,border="darkGray",borderWidth=5,opacity=90)
    else:
        c = Circle(radar.centerX,radar.centerY,(50*i)/2+1,fill=None,border="mediumSpringGreen",borderWidth=5,opacity=50)
    radar.add(c)

obstacles.add(
    Rect(0,370,400,30, fill=None),
    
    
    )
#sonarLine = Group(Line(radar.centerX,radar.centerY,radar.centerX,radar.centerY-150,fill="gray",lineWidth=2),Circle(radar.centerX,radar.centerY-150,4,fill="gray"))
sonarLine = Arc(radar.centerX,radar.centerY,300,200,80,10,fill="gray")
sonarLine.mode = 360

###--------------------------


app.limit = 8
### BLOCKS
blocks = []
keys = Group()
app.blockindexselected = 0
colours = ["blue","green","salmon","gray", "pink", "yellow"]
app.inventory = 0
for i in range(5):
    c = Rect(0, 0, 50,50,fill="cyan")
    c.filled = False
    c.slotNumb = i
    c.centerX = 30 + 60*i
    c.centerY = 30
    blocks.append(c)




selected = Rect(0,0,50,50,fill=None,borderWidth = 4, border = rgb(247,138,238))
selected.centerY = 30
selected.centerX = 30
selected.anim = 0
    

### KEYS

for i in range(len(colours)):
    
    colour = colours[i]
    key = Circle(40+60*i,120,20,fill=colour)
    key.color = colour
    key.isPickedUp = False
    key.slotPos = 9
    key.dropped = False
    keys.add(key)
    
for block in blocks:
    
    block.toBack()
    ship.toBack()
    
### LOGISTICS
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
    


def onStep():
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


###game start

startMenu(False)

for colour in colours:
    moveKey(77,500,colour)




cmu_graphics.run()