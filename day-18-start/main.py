from doctest import DocTest
from turtle import *
import random

timmy = Turtle()
# Form
timmy.shape("turtle")
# Colors
# RGB
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)
# Speed
timmy.pensize(1)
timmy.speed("fastest")
#-------------------------------------------------
def turnleft():
    timmy.left(90)
    timmy.forward(30)
    timmy.left(90)

def turnright():
    timmy.right(90)
    timmy.forward(30)
    timmy.right(90)

def point():
    for _ in range(20):
        timmy.dot(20, random_color())
        timmy.forward(30)
        timmy.dot(20, random_color())
# dot
timmy.penup() 

timmy.setheading(225)
timmy.forward(400)
timmy.setheading(0)

while True:
    point()
    turnleft()
    point()
    turnright()







timmy.color(random_color())

#-----------------------------------------
# Draw circle
# def draw_circle():
#     for _ in range(360):
#         timmy.forward(1)
#         timmy.left(1)
# Draw spirograph
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         timmy.pencolor(random.choice(colors))
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + size_of_gap)


# range

# colors = ["red","orange","yellow","green","blue","indigo","purple"]

# color_list = [(237, 251, 245), (249, 228, 17), (213, 13, 9),
#               (198, 12, 35), (231, 228, 5), (197, 69, 20),
#               (33, 90, 188), (43, 212, 71)]


# Random walk

# while True:
#     timmy.color(random_color())
#     random_choice = random.randint(-1, 1)
#     print(random_choice)
#     timmy.right(random_choice * 90)
#     go_forward = [25, 25, 30 ]
#     timmy.forward(random.choice(go_forward))

# Random Walk
# directions = [0, 90, 180, 270]
# while True:
#     timmy.color(random.choice(colors))
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))
# # Screen
screen = Screen()
screen.exitonclick()
# Deplace


