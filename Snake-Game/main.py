from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game - paulipotter")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

screen.update()
game_over = False
while not game_over:
    screen.update()
    time.sleep(0.09)
    snake.move()

    if snake.head.distance(food) < 15:
        food.new_location()








screen.exitonclick()