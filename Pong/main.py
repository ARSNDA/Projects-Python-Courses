from turtle import *
from ball import *
from paddle import *
import time

from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)


# Paddles----------------------------
PADDLE_R = Paddle(350, 0)
PADDLE_L = Paddle(-350, 0)
# Ball------------------------------
BALL = Ball(0, 0)
BALL.speed(7)

SCOREBOARD = Scoreboard(0, 240)

# Listen ----------------------------
screen.listen()
screen.onkey(PADDLE_R.up, "Up")
screen.onkey(PADDLE_R.down, "Down")

screen.onkey(PADDLE_L.up, "w")
screen.onkey(PADDLE_L.down, "s")
#------------------------------------
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    SCOREBOARD.refresh_score()
    BALL.move()



    if BALL.ycor() > 270 or BALL.ycor() < -270:
        BALL.bounce_y()

    if BALL.distance(PADDLE_R) < 50 and BALL.xcor() > 320 or BALL.distance(PADDLE_L) < 50 and BALL.xcor() < -320:
        BALL.bounce_x()

    if BALL.xcor() > 380:
        BALL.reset_position()
        SCOREBOARD.increase_score_l()
    elif BALL.xcor() < -380:
        BALL.reset_position()
        SCOREBOARD.increase_score_r()


screen.exitonclick()