STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE = 280

from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.restart()

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def restart(self):
        self.goto(STARTING_POSITION)