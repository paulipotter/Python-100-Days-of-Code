from turtle import Turtle, Screen

etch = Turtle()
screen = Screen()

def move_forwards():
    etch.forward(10)

def move_backwards():
    etch.backward(10)

def turn_left():
    etch.setheading(etch.heading() + 10)
    
def turn_right():
    etch.setheading(etch.heading() - 10)
        
def clear():
    etch.clear()
    etch.penup()
    etch.home()
    etch.pendown()
    
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()