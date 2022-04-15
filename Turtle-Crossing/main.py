from turtle import Screen
from tortoise import Tortoise
import time
from scoreboard import Scoreboard
from car import Car

FINISH_LINE_Y = 260

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing - paulipotter")
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()

player = Tortoise()
screen.onkey(player.move_up, "Up")

game_is_on = True

cars = []
i = 0
while game_is_on:
    time.sleep(0.1)
    if i % 6 == 0:
        c = Car()
        cars.append(c)
    for car in cars:
        car.move_x()
        # Detect collision with cars
        if player.distance(car) < 17:
            scoreboard.game_over()
            game_is_on = False
            time.sleep(2)
        if player.ycor() > FINISH_LINE_Y:
            scoreboard.increase_level()
            car.level_up()
            time.sleep(0.5)
            player.reset_position()
            screen.update()
            time.sleep(1)

    i += 1
    screen.update()

screen.exitonclick()
