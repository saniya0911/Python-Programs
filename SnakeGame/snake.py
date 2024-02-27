from turtle import Turtle, Screen
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN=270
LEFT=180
RIGHT=0

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)

    def add_segments(self,position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_pos = self.segments[seg-1]
            self.segments[seg].goto(new_pos.xcor(),new_pos.ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(10000,10000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]