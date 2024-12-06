from turtle import *

UP = 90

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.goto(x, y)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(UP)
        self.penup()


    def up(self):
        self.forward(20)

    def down(self):
        self.forward(-20)
