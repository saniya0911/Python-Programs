from turtle import Turtle
ALIGN = "center"
FONT = ("Courier",16,"normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score =0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align =ALIGN, font =FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over! Your Final Score is: {self.score}",align=ALIGN,font=FONT)