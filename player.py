from turtle import Turtle,Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

screen=Screen()
screen.register_shape("Jour23_TurtleCrossing/assets/player.gif")
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("Jour23_TurtleCrossing/assets/player.gif")
        self.color('black')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        
    def move_up(self):
        self.forward(MOVE_DISTANCE)
    def finish(self):
        if self.ycor()>=FINISH_LINE_Y:
            return True
    def go_to_start(self):
        self.goto(STARTING_POSITION)
   
    
    
