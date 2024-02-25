COLORS = ["green","orange","blue","purple","yellow","red"]
MOVE =5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class Car():
    def __init__(self):
        self.all_cars =[]
        self.speed = MOVE

    def create_cars(self):
        chance = random.randint(1,6)
        if chance==1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            new_car.goto(300,random.randint(-250,250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def level_up(self):
        self.speed+=MOVE_INCREMENT


