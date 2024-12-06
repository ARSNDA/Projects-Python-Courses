from turtle import *

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")

class Scoreboard(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x, y)
        self.hideturtle()
        self.score_r = 0
        self.score_l = 0

    def refresh_score(self):
        self.clear()
        self.write(f"{self.score_l} | {self.score_r}", align=ALIGNMENT, font=FONT)

    def increase_score_r(self):
        self.score_r += 1
        self.refresh_score()

    def increase_score_l(self):
        self.score_l += 1
        self.refresh_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)