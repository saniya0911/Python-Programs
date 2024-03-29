from turtle import  Screen
import time
from snake import Snake
from food import Food 
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.4)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) <15:
        food.refresh()
        score.increase_score()
        snake.extend()

    #detect collision with walls
    if snake.head.xcor() >290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        snake.reset()
        game_is_on=False
        score.game_over()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            game_is_on=False
            score.game_over()
        
screen.exitonclick()