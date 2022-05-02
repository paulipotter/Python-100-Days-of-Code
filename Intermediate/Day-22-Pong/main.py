from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Day-22-Pong! - paulipotter")
screen.tracer(0)

scoreboard = Scoreboard()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
game_over = False

while not game_over:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when paddle misses
    if ball.xcor() > 380:
        scoreboard.update_right()
        time.sleep(2)
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.update_left()
        time.sleep(2)
        ball.reset_position()

screen.exitonclick()
