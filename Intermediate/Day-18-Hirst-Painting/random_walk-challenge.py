import turtle as t
from random import choice, randint

def random_color():
    return (randint(0,255),randint(0,255),randint(0,255))

timmy = t.Turtle()
t.colormode(255)
#colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0, 90, 180, 270]
timmy.pensize(10)
timmy.speed('fastest')
for _ in range(200):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(choice(direction))