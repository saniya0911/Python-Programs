from turtle import Turtle
class Paddle(Turtle):
   def __init__(self,x,y,player):
      super().__init__()
      self.shape("square")
      self.shapesize(stretch_len=1,stretch_wid=5)
      self.color("white")
      self.penup()
      self.goto(x,y)
      self.paddle= player

   def go_up(self):
      self.goto(self.xcor(),self.ycor()+20)

   def go_down(self):
      self.goto(self.xcor(),self.ycor()-20)
