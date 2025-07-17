from turtle import Turtle,Screen
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
screen=Screen()
screen.register_shape("./assets/car1.gif")
screen.register_shape("./assets/car2.gif")
screen.register_shape("./assets/car3.gif")
screen.register_shape("./assets/car4.gif")
car_list=["./assets/car1.gif","./assets/car2.gif","./assets/car3.gif","./assets/car4.gif"]


class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE
  
        
      
        
    def move(self):
        for car in self.all_cars:
            
            car.backward(self.car_speed)
    def create_car(self):
        car=Turtle()
        car.shape(random.choice(car_list))
        car.shapesize(stretch_wid=1,stretch_len=2)
        car.color(random.choice(COLORS))
        car.penup()
        car.goto(310,random.randint(-250,250))
    
       
        self.all_cars.append(car)
    def speed_up(self):
        self.car_speed+=MOVE_INCREMENT
     
    
