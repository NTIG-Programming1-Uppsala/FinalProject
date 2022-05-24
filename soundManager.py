from cmu_graphics import *

Label('Music In CMU Graphics Demo #3', 200, 20, size=18, bold=True)
Label('Click to play a sequence of notes!', 200, 40, size=15)

app.notesList = [ Note('C', 2, 1/4), Note('G', 2, 1/4), Note('E', 2, 1/4) ]
app.notesTuple = ( Note('C', 3, 1/4), Note('G', 3, 1/4), Note('F', 3, 1/4) )
app.notesListToTuple = tuple(app.notesList)

sequencerExample1 = Sequencer(app.notesTuple)
sequencerExample2 = Sequencer(app.notesListToTuple, instrument='bass', volume=0.4)

def onMousePress(mouseX, mouseY):
    sequencerExample1.play()
    sequencerExample2.play()



cmu_graphics.run()