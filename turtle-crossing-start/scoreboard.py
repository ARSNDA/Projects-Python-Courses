from turtle import *

FONT = ("Courier", 24, "normal")

level = 1

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.color("black")
        self.write(f"Level: {level}", align="left", font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Level: {level}", align="left", font=FONT)

    def game_over(self):
        self.color("black")
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)


    def increase_level(self):
        global level
        self.color("black")
        level += 1
        self.clear()
