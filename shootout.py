from Tkinter import *


class Shootout(object):
    

    def __init__(self, teamA, teamB):
 
        self.teamA = Team(teamA)            #create a team with the name of the first country
        self.teamB = Team(teamB)            #create a team with the name of the second country
        self.field = Field(teamA,teamB)     #create the field
        self.referee = Referee()            #create the referee
        self.shootingTeam = self.teamA
        self.goalieTeam = self.teamB
        root = Tk()
        frame = Frame(root, width = 500, height = 500)
        frame.bind("<Left>", self.leftKey)
        frame.bind("<Right>", self.rightKey)
        frame.focus_set()
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
        self.playRound()
        root.mainloop()

    def playRound(self):

        #wait()                  #wait for 3 seconds
        #self.shootingTeam.shoot()
        #self.goalieTeam.save()
        pass

    def leftKey(self,event):
        print(self.shootingTeam.name + " shot left!")

    def rightKey(self,event):
        print(self.shootingTeam.name + " shot right!")


    def shotKeyDetected(self,event):
        print(self.shootingTeam.name + " shot!")


class Team:

    def __init__(self, name):
        self.name = name


    def shoot(self):
        #todo: fill in logic
        print(self.name + " shoots!")

    def save(self):
        #todo: fill in logic
        print(self.name + " saves!")





class Referee:

    def __init__(self):
        pass


class Field:

    def __init__(self, teamA, teamB):
        self.teamA = teamA
        self.teamB = teamB



