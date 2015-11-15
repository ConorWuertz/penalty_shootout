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




class Shootout(object):
    

    def __init__(self, teamA, teamB):
        



        self.teamA = Team(LEFT_POST,teamA,'red',1)              #create a team with the name of the first country
        self.teamB = Team(RIGHT_POST-200, teamB,'blue',1)             #create a team with the name of the second country
        self.teams = [self.teamA,self.teamB]

        self.shootingTeam = self.teamA      #teamA starts with shooting
        self.goalieTeam = self.teamB        #teamB starts with saving
        

        self.field = Field(teamA,teamB)             #create the field
        self.referee = Referee()                    #create the referee

        #create the logical representation of the goalie
        self.goalie = Goalie(LEFT_POST+GOAL_LENGTH/2,CROSSBAR_TOP+GOAL_HEIGHT -200, self.goalieTeam.color,1.5)
        self.kicker = Player(LEFT_POST+GOAL_LENGTH/2 - 30 ,CROSSBAR_TOP+GOAL_HEIGHT +60, self.shootingTeam.color,1.5)

        #create the logical representation of the ball
        self.ball = Ball(LEFT_POST+GOAL_LENGTH/2,CROSSBAR_TOP+GOAL_HEIGHT+150)
        
       
        #build the initial frame
        root = Tk()

        #create a drawing canvas
        self.canvas = Canvas(root,width=FIELD_LENGTH, height=FIELD_WIDTH,background='darkgreen')
 #       root.minsize(width=FIELD_LENGTH, height=FIELD_WIDTH)
 #       root.maxsize(width=FIELD_LENGTH, height=FIELD_WIDTH)
 #       root.configure(background='darkgreen')

        #bind the arrow keys to these functions
        self.canvas.bind("<Left>", self.leftKey)
        self.canvas.bind("<Right>", self.rightKey)
        self.canvas.bind("<Down>", self.downKey)
        self.canvas.bind("<Up>", self.upKey)

        #assign the keyboard focus to the canvas
        self.canvas.focus_set()
        self.canvas.pack()

        #do the initial paint
        self.repaint()
        root.mainloop()

    def playRound(self):

        #wait()                  #wait for 3 seconds
        #self.shootingTeam.shoot()
        #self.goalieTeam.save()
        self.repaint()
        pass

    def leftKey(self,event):

        #move the goalie to the left by reducing his x position. Mod by FIELD_LENGTH to wrap
        self.goalie.x = (self.goalie.x - 10) % FIELD_LENGTH
        self.repaint()

    def rightKey(self,event):
        #move the goalie to the right by increasing his x position. Mod by FIELD_LENGTH to wrap
        self.goalie.x = (self.goalie.x + 10) % FIELD_LENGTH
        self.repaint()

    def downKey(self,event):

        #Scale up the goalie dimennsions by 1.1 to give the illusion that he is approaching the viewer
        self.goalie.height = self.goalie.height * 1.1
        self.goalie.torsoThickness = self.goalie.torsoThickness * 1.1
        self.goalie.headRadius = self.goalie.headRadius * 1.1
        self.goalie.eyeRadius  = self.goalie.eyeRadius * 1.1
        self.goalie.eyeXOffset = self.goalie.headRadius/3
        self.repaint()

    def upKey(self,event):

        #Scale down the goalie dimenions by 1.1 to give the illusion that he the goalie is leaving the viewer
        self.goalie.height = self.goalie.height / 1.1
        self.goalie.torsoThickness = self.goalie.torsoThickness / 1.1
        self.goalie.headRadius = self.goalie.headRadius / 1.1
        self.goalie.eyeRadius = self.goalie.eyeRadius / 1.1
        self.goalie.eyeXOffset = self.goalie.headRadius/3
        self.repaint()


    def shotKeyDetected(self,event):
        pass


    def detectCollisions():
        pass    

    def repaint(self):

        #clear the canvas of prior drawings 
        self.canvas.delete('temp')

        #paint the players
        for team in self.teams:
            for player in team.players:
                self.drawPlayer(player)

        #paint the goal
        self.drawGoal()

        #paint the goalie
        self.drawPlayer(self.goalie)

        #paint the kicking player
        self.drawPlayer(self.kicker)


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



    def drawBall(self):

        self.canvas.create_oval(self.ball.x - self.ball.radius, self.ball.y- self.ball.radius, 
            self.ball.x + self.ball.radius, self.ball.y + self.ball.radius, fill=self.ball.color)

    def drawPlayer(self,player):


        #draw the player's head
        self.canvas.create_oval(player.x-player.headRadius, player.y - player.headRadius, 
            player.x + player.headRadius, player.y + player.headRadius, fill='white', tag='temp')

        #draw the player's eyes
        self.canvas.create_oval(player.x-player.eyeXOffset-player.eyeRadius, player.y - player.eyeRadius, 
            player.x -player.eyeXOffset+player.eyeRadius, player.y+player.eyeRadius,fill=player.color,tag='temp')

        self.canvas.create_oval(player.x+player.eyeXOffset-player.eyeRadius, player.y - player.eyeRadius, 
            player.x +player.eyeXOffset+player.eyeRadius, player.y+player.eyeRadius, fill=player.color,tag='temp')
        
        #draw the player's torso
        self.canvas.create_rectangle(player.x-player.torsoThickness/2, player.y+player.headRadius, 
            player.x+player.torsoThickness/2,player.y +player.height/2, fill=player.color,tag='temp')



class Team:

    def __init__(self, startX, name,color,scale):
        self.name = name
        self.color = color
        self.players = [Player(startX+ i*50, 400,color,scale) for i in range(5)]


    def shoot(self):
        #todo: fill in logic
        print(self.name + " shoots!")

    def save(self):
        #todo: fill in logic
        print(self.name + " saves!")

class Player:

    def __init__(self, x,y,color,scale):
        self.x = x
        self.y = y
        self.headRadius = 18 * scale
        self.eyeXOffset = self.headRadius/3
        self.eyeRadius = 2 * scale
        self.height = 200 * scale
        self.torsoThickness = 15 * scale
        self.color = color

class Goalie(Player):

    def __init__(self, x,y,color,scale):
        Player.__init__(self,x,y,color,scale)


class Referee:

    def __init__(self):
        pass


class Field:

    def __init__(self, teamA, teamB):
        self.teamA = teamA
        self.teamB = teamB



    

class Ball:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.radius = 16
        self.color = 'white'



