from turtle import Turtle, Screen
from random import randint
screen = Screen()
screen.setup(width=500, height=500)
racing = False

guess = screen.textinput(title="Make your bet!",prompt="Guess the color of the turtle that will win the race: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

x = -230
y = -100
for indx in range(len(colors)):
    turtle = Turtle(shape='turtle')
    turtle.color(colors[indx])
    turtle.penup()
    turtle.goto(x=x,y=y)
    y += 30
    all_turtles.append(turtle)
   
if guess:
    racing = True 

while racing:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            winner = turtle.pencolor()
            racing = False
            if winner == guess:
                print("You guessed it right!")
            else:
                print("You guessed it wrong :(")
        turtle.forward(randint(0,10))

screen.exitonclick()