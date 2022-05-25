from cmu_graphics import *

app.c = Oval(-10, 200, 300, 200,opacity=50)
app.c.yes = False
app.c.width *= 2
app.c.height *= 2
app.c.right = 0

def nearDeathAnimation():
    print("1")
    if app.c.yes:
        
        if app.c.left < 410:
            app.c.centerX += 10
            app.c.toFront()
        
            

def nearDeathAnimationStart(bool):
    print("2")
    if bool == True:
        app.c.yes = True
    else:
        app.c.right = 0


