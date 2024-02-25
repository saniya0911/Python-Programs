from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("Pong")
screen.tracer(0)

rpaddle = Paddle(350,0,"Right")
lpaddle = Paddle(-350,0,"Left")

ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(rpaddle.go_up,"Up")
screen.onkey(rpaddle.go_down,"Down")
screen.onkey(lpaddle.go_up,"w")
screen.onkey(lpaddle.go_down,"s")

is_on = True
while is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with upper and lower balls
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(rpaddle) <50 and ball.xcor()>320 or ball.distance(lpaddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
        ball.move_speed*=0.9

    #detect when right paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        score.left_score()

    #detect when left paddle misses
    if ball.xcor()<-380:
        ball.reset_position()
        score.right_score()

    #game over
    if score.l_score==10 or score.r_score==10:
        is_on = False
    
if score.l_score==10:
    score.game_over(lpaddle)
else:
    score.game_over(rpaddle)

screen.exitonclick()