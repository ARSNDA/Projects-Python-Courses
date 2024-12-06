import time
from turtle import Screen

import scoreboard
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

arsen = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(arsen.up, "Up")

step_count = 0  # Счетчик шагов
car_creation_interval = 6  # Интервал создания машин


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_score()

    # Появление машин по заданному интервалу
    if step_count % car_creation_interval == 0:
        cars.create_car()

    cars.move_cars()

    if arsen.ycor() > 290:
        arsen.go_to_start()
        scoreboard.increase_level()
        cars.increase_speed()
        if car_creation_interval > 1:
            car_creation_interval -= 1

    for car in cars.all_cars:
        if arsen.distance(car) < 10:
            arsen.go_to_start()
            scoreboard.game_over()
            game_is_on = False

    step_count += 1


screen.exitonclick()