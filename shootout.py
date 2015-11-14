from Tkinter import *
import math

#CONSTANTS
FIELD_LENGTH = 1000
FIELD_WIDTH = 600
GOAL_LENGTH = FIELD_LENGTH *.75
GOAL_HEIGHT = GOAL_LENGTH *.4
LEFT_POST = (FIELD_LENGTH-GOAL_LENGTH)/2
RIGHT_POST = LEFT_POST + GOAL_LENGTH
CROSSBAR_TOP = FIELD_WIDTH - FIELD_WIDTH * .9
BAR_THICKNESS = 5

HEAD_RADIUS = 18
EYE_X_OFFSET = HEAD_RADIUS/3
EYE_RADIUS = 2
GOALIE_HEIGHT = 200
GOALIE_TORSO_THICKNESS = 15


class Shootout(object):
    

    def __init__(self, teamA, teamB):
 
        self.teamA = Team(teamA,'red')            #create a team with the name of the first country
        self.teamB = Team(teamB,'blue')            #create a team with the name of the second country
        self.field = Field(teamA,teamB)     #create the field
        self.referee = Referee()            #create the referee
        self.goalie = Goalie(LEFT_POST+GOAL_LENGTH/2,CROSSBAR_TOP+GOAL_HEIGHT -GOALIE_HEIGHT)
        
        self.shootingTeam = self.teamA      #teamA starts with shooting
        self.goalieTeam = self.teamB        #teamB starts with saving
        
        root = Tk()
        self.canvas = Canvas(root,width=FIELD_LENGTH, height=FIELD_WIDTH,background='darkgreen')
 #       root.minsize(width=FIELD_LENGTH, height=FIELD_WIDTH)
 #       root.maxsize(width=FIELD_LENGTH, height=FIELD_WIDTH)
 #       root.configure(background='darkgreen')
        self.canvas.bind("<Left>", self.leftKey)
        self.canvas.bind("<Right>", self.rightKey)
        self.canvas.bind("<Down>", self.downKey)
        self.canvas.bind("<Up>", self.upKey)
        self.canvas.focus_set()
        self.canvas.pack()

        self.playRound()
        root.mainloop()

    def playRound(self):

        #wait()                  #wait for 3 seconds
        #self.shootingTeam.shoot()
        #self.goalieTeam.save()
        self.repaint()
        pass

    def leftKey(self,event):
        self.goalie.x = (self.goalie.x - 10) % FIELD_LENGTH
        self.repaint()

    def rightKey(self,event):
        self.goalie.x = (self.goalie.x + 10) % FIELD_LENGTH
        self.repaint()

    def downKey(self,event):
        global GOALIE_HEIGHT
        global GOALIE_TORSO_THICKNESS
        global HEAD_RADIUS
        global EYE_RADIUS
        global EYE_X_OFFSET
        GOALIE_HEIGHT = GOALIE_HEIGHT * 1.1
        GOALIE_TORSO_THICKNESS = GOALIE_TORSO_THICKNESS * 1.1
        HEAD_RADIUS = HEAD_RADIUS * 1.1
        EYE_RADIUS  = EYE_RADIUS * 1.1
        EYE_X_OFFSET = HEAD_RADIUS/3
        self.repaint()

    def upKey(self,event):
        global GOALIE_HEIGHT
        global GOALIE_TORSO_THICKNESS
        global HEAD_RADIUS
        global EYE_RADIUS
        global EYE_X_OFFSET
        GOALIE_HEIGHT = GOALIE_HEIGHT / 1.1
        GOALIE_TORSO_THICKNESS = GOALIE_TORSO_THICKNESS / 1.1
        HEAD_RADIUS = HEAD_RADIUS / 1.1
        EYE_RADIUS = EYE_RADIUS / 1.1
        EYE_X_OFFSET = HEAD_RADIUS/3
        self.repaint()


    def shotKeyDetected(self,event):
        pass
    def repaint(self):

        self.drawGoal()
        
        self.drawGoalie()

        self.drawBall()
       

    def drawGoal(self):

        #draw the goal's crossbar
        self.canvas.create_rectangle(LEFT_POST, CROSSBAR_TOP, RIGHT_POST+BAR_THICKNESS,
                                     CROSSBAR_TOP-BAR_THICKNESS, fill='white')
        #draw the goal's left post
        self.canvas.create_rectangle(LEFT_POST, CROSSBAR_TOP, LEFT_POST+BAR_THICKNESS,
                                     CROSSBAR_TOP+GOAL_HEIGHT, fill='white')
        #draw the goal's right post
        self.canvas.create_rectangle(RIGHT_POST, CROSSBAR_TOP, RIGHT_POST+BAR_THICKNESS,
                                     CROSSBAR_TOP+GOAL_HEIGHT, fill='white')

    def drawGoalie(self):

        self.canvas.delete('temp')
        #draw the goalie's head
        self.canvas.create_oval(self.goalie.x-HEAD_RADIUS, self.goalie.y - HEAD_RADIUS, 
            self.goalie.x + HEAD_RADIUS, self.goalie.y+HEAD_RADIUS, fill='white', tag='temp')

        #draw the goalie's eyes
        self.canvas.create_oval(self.goalie.x-EYE_X_OFFSET-EYE_RADIUS, self.goalie.y - EYE_RADIUS, 
            self.goalie.x -EYE_X_OFFSET+EYE_RADIUS, self.goalie.y+EYE_RADIUS,fill=self.goalieTeam.color,tag='temp')

        self.canvas.create_oval(self.goalie.x+EYE_X_OFFSET-EYE_RADIUS, self.goalie.y - EYE_RADIUS, 
            self.goalie.x +EYE_X_OFFSET+EYE_RADIUS, self.goalie.y+EYE_RADIUS, fill=self.goalieTeam.color,tag='temp')

        #draw the goalie's torso
        self.canvas.create_rectangle(self.goalie.x-GOALIE_TORSO_THICKNESS/2, self.goalie.y+HEAD_RADIUS, 
            self.goalie.x+GOALIE_TORSO_THICKNESS/2,self.goalie.y +GOALIE_HEIGHT/2, fill=self.goalieTeam.color,tag='temp')
        
        #draw the goalie's arms


    def drawBall(self):
        pass



class Team:

    def __init__(self, name,color):
        self.name = name
        self.color = color


    def shoot(self):
        #todo: fill in logic
        print(self.name + " shoots!")

    def save(self):
        #todo: fill in logic
        print(self.name + " saves!")


class Goalie:

    def __init__(self, x,y ):
        self.x = x
        self.y = y

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



