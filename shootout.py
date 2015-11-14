from Tkinter import *

#CONSTANTS
FIELD_LENGTH = 1000
FIELD_WIDTH = 600


class Shootout(object):
    

    def __init__(self, teamA, teamB):
 
        self.teamA = Team(teamA)            #create a team with the name of the first country
        self.teamB = Team(teamB)            #create a team with the name of the second country
        self.field = Field(teamA,teamB)     #create the field
        self.referee = Referee()            #create the referee
        self.shootingTeam = self.teamA
        self.goalieTeam = self.teamB
        root = Tk()
        canvas = Canvas(root,width=FIELD_LENGTH, height=FIELD_WIDTH,background='darkgreen')
 #       root.minsize(width=FIELD_LENGTH, height=FIELD_WIDTH)
 #       root.maxsize(width=FIELD_LENGTH, height=FIELD_WIDTH)
 #       root.configure(background='darkgreen')
        canvas.bind("<Left>", self.leftKey)
        canvas.bind("<Right>", self.rightKey)
        canvas.focus_set()
        canvas.pack()

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
        self.ball = Ball()

class Ball:

    def __init__(self):
        self.x = 250
        self.y = 250



