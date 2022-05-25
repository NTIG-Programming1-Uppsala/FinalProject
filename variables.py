
from cmu_graphics import *

#playsound("sonarsoundeffect.wav")

##test

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
win = Circle(700,700,2)
### INSTRUCTIONS
arrowinstr = Image("Images/metal_rusty.jpg",50,50)
arrowinstr.width = 1
arrowinstr.height = 1
arrowinstr.centerX = 200
arrowinstr.centerY = 260
black = Rect(0,0,400,400)
instr1 = Label("instructions",200,70,fill="white",size=30)
instr2 = Label("Use A, D to switch between items",200,instr1.centerY+50,fill="white",size=20)
instr3 = Label("W to use the item, use the console for info",200,instr1.centerY+70,fill="white",size=20)
instr4 = Label("arrow keys to move",200,instr1.centerY+90,fill="white",size=15)
instr5 = Label("Press r to start",200,arrowinstr.bottom+10,fill="white",size=20)
instructions = Group(black,instr1, instr2,instr3, instr4,instr5,arrowinstr)
app.sonar = True

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

yellowButton = Circle(347,90,20,fill="yellow")
yellowButton.thing = yellowButton.fill
buttons.append(yellowButton)
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
    