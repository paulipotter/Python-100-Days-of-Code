from random import choice
import colorgram
import turtle as t
s = t.Screen()
s.setup(width=500, height=500)
rgb_list = []
colors = colorgram.extract('img.png', 15)

for color in colors:
    rgb_list.append((color.rgb.r, color.rgb.g, color.rgb.b))

draw = t.Turtle()  
dot_distance = 40
width = 10
height = 10
t.colormode(255)
draw.penup()
draw.speed('fastest')
draw.hideturtle()
draw.bk(200)
draw.pensize(10)
draw.setheading(90)
draw.forward(170)
draw.setheading(360)

for _ in range(height):
    for __ in range(width):
        draw.color(choice(rgb_list))
        draw.dot()
        draw.forward(dot_distance)
    draw.backward(dot_distance * width)
    draw.right(90)
    draw.forward(dot_distance)
    draw.left(90)
    

s.exitonclick()

    