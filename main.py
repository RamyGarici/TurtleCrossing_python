import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Game")
player=Player()
screen.bgpic("./assets/racetrack.gif")
screen.listen()
screen.onkeypress(player.move_up,"Up")
game_is_on = True
cpt=0
scoreboard=Scoreboard()
car_manager=CarManager()
while game_is_on:
    cpt+=1
    if cpt==6:
        car_manager.create_car()
        cpt=0
    time.sleep(0.1)
    car_manager.move()
#collision voiture
    for car in car_manager.all_cars:
        if player.distance(car)<25:
            scoreboard.game_over()
            game_is_on=False
            
#collision fin niveau
    if player.finish():
        scoreboard.level_up()
         
        player.go_to_start()
        car_manager.speed_up()
    
  
    screen.update()

screen.exitonclick()