from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        
        super().__init__()
        self.penup()
        self.goto(-270,270)
        self.hideturtle()
        self.level=0
        self.write(f"Level: {self.level}",font=FONT)
    def level_up(self):
        self.level+=1
        self.clear()
        self.write(f"Level: {self.level}",font=FONT)
    def game_over(self):
        
        self.goto(0,0)
        self.write(f"Game Over.",align="center",font=FONT)
       
        
        
        
    
