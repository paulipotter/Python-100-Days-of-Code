from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game - paulipotter")
screen.tracer(0)
boundaries = [-280, 280]
snake = Snake()

screen.update()
game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()








screen.exitonclick()