from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game - paulipotter")

snake = []
x_cor = 0
for _ in range(3):
    body = Turtle("square")
    body.color("white")
    body.setx(x_cor)
    x_cor -= 20
    snake.append(body)

screen.exitonclick()