from cmu_graphics import *

app.c = Oval(-10, 200, 300, 200,opacity=50)
app.c.yes = False
app.c.width *= 2
app.c.height *= 2
app.c.right = 0

def nearDeathAnimation():
    
    if app.c.yes:
        
        if app.c.left <= 400:
            app.c.centerX += 10
            app.c.toFront()
        
            

def nearDeathAnimationStart(bool):
    
    if bool == True:
        app.c.yes = True
    elif bool == False:
        app.c.yes = False
        app.c.right = 0


