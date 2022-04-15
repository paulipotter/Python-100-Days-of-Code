from turtle import Screen
from tortoise import Tortoise
import time
#from scoreboard import Scoreboard
#from car import Car


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing - paulipotter")
screen.tracer(0)
screen.listen()


t = Tortoise()
screen.onkey(t.move_up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


screen.exitonclick()