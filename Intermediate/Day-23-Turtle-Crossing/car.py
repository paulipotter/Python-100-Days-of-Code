from turtle import Turtle
from random import choice, randint

RANDOM_COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "brown"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(choice(RANDOM_COLORS))
        self.penup()
        self.goto(290, randint(-240, 240))
        self.move_distance = 5

    def move_x(self):
        new_x = self.xcor() - self.move_distance
        self.goto(new_x, self.ycor())

    def level_up(self):
        self.move_distance += 2

