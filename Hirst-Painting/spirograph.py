import turtle as t
from random import randint

def random_color():
    return (randint(0,255),randint(0,255),randint(0,255))

def draw_spirograph(size):
    for _ in range (int(360/size)):
        drawing.setheading(drawing.heading() + size)
        drawing.color(random_color())
        drawing.circle(100)
    
radius = 100
drawing = t.Turtle()
t.colormode(255)
drawing.speed('fastest')
draw_spirograph(5)

s = t.Screen()
s.exitonclick()

