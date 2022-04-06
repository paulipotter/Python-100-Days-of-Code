from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game - paulipotter")
screen.tracer(0)
boundaries = [-280, 280]
snake = []
x_cor = 0
for _ in range(3):
    body = Turtle("square")
    body.color("white")
    body.penup()
    body.setx(x_cor)
    x_cor -= 20
    snake.append(body)

screen.update()
game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    for segment in range(len(snake)-1, 0, -1):
        new_x = snake[segment-1].xcor()
        new_y = snake[segment-1].ycor()
        snake[segment].goto(new_x, new_y)
    snake[0].forward(20)







screen.exitonclick()