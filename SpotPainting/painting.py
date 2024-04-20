'''import colorgram
colors = colorgram.extract("image.jpg",10)

rgb_colors=[]
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)'''

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

colors = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 
148), (166, 58, 48), (141, 184, 162)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 101

for dot_count in range(1, number_of_dots):
   tim.dot(20,random.choice(colors))
   tim.forward(50)

   if dot_count % 10==0:
      tim.setheading(90)
      tim.forward(50)
      tim.setheading(180)
      tim.forward(500)
      tim.setheading(0)

screen = t.Screen()
screen.exitonclick()