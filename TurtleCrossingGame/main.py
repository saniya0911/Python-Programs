from turtle import Turtle,Screen
import time
from player import Player,FINISH_LINE
from car import Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move_forward,"Up")

is_on = True
car = Car()
score = Scoreboard()

while is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()

    #detect collision with cars
    for c in car.all_cars:
        if c.distance(player)<20:
            is_on = False
            score.game_over()

    #detect when the player wins
    if player.ycor()>FINISH_LINE:
        player.restart()
        car.level_up()
        score.increase_level()

screen.exitonclick()