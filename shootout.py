from Tkinter import *


class Shootout(object):
    

    def __init__(self, teamA, teamB):
 
        self.teamA = Team(teamA) #create a team with the name of the first country
        self.teamB = Team(teamB) #create a team with the name of the second country
        self.field = Field(teamA,teamB)     #create the field
        self.referee = Referee() #create the referee
        self.shootingTeam = teamA
        self.goalieTeam = teamB
        root = Tk()
        frame = Frame(root)
        frame.pack()

        bottomframe = Frame(root)
        bottomframe.pack( side = BOTTOM )

        redbutton = Button(frame, text="Red", fg="red")
        redbutton.pack( side = LEFT)

        greenbutton = Button(frame, text="Brown", fg="brown")
        greenbutton.pack( side = LEFT )

        bluebutton = Button(frame, text="Blue", fg="blue")
        bluebutton.pack( side = LEFT )

        blackbutton = Button(bottomframe, text="Black", fg="black")
        blackbutton.pack( side = BOTTOM)

        root.mainloop()

    def playRound(self, row, col):

        wait()                  #wait for 3 seconds
        shootingTeam.shoot()
        goalieTeam.save()

    def getpixel(self, row, col):
        return self.data[row][col]

    def display(self):
        print "\n".join(["".join(row) for row in self.data])

