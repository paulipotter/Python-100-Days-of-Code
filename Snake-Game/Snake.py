from turtle import Turtle


class Snake:
    def __init__(self):
        snake = []
        x_cor = 0
        for _ in range(3):
            body = Turtle("square")
            body.color("white")
            body.penup()
            body.setx(x_cor)
            x_cor -= 20
            snake.append(body)

    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment - 1].xcor()
            new_y = self.snake[segment - 1].ycor()
            self.snake[segment].goto(new_x, new_y)
        self.snake[0].forward(20)
