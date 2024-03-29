from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-50,200)
        self.write(self.l_score, align="center", font = ("Courier",50,"normal"))
        self.goto(50,200)
        self.write(self.r_score, align="center", font = ("Courier",50,"normal"))

    def left_score(self):
        self.l_score+=1
        self.clear()
        self.update_scoreboard()

    def right_score(self):
        self.r_score+=1
        self.clear()
        self.update_scoreboard()

    def game_over(self,player):
        self.goto(0,0)
        self.write(f"{player.paddle} paddle wins!",align ="center",font = ("Courier",30,"normal"))