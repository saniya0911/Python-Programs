from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width = 500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
y_positions = [-70,-40,-10,20,50,80]
is_race_on = False
all_turtles =[]

for turtle_index in range(0,6):
   tim = Turtle(shape="turtle")
   tim.color(colors[turtle_index])
   tim.penup()
   tim.goto(x=-240, y=y_positions[turtle_index])
   all_turtles.append(tim)

if user_bet:
   is_race_on=True

while is_race_on:
   for turtles in all_turtles:
      if turtles.xcor()>230:
         is_race_on = False
         winning_color = turtles.pencolor()
         if winning_color == user_bet:
            print(f"You've won! The {winning_color} turtle is the winner!")
         else:
            print(f"You've lost! The {winning_color} turtle is the winner!")
      paces = random.randint(0,10)
      turtles.forward(paces)


screen.exitonclick()