from turtle import Turtle
MOVE_DISTANCE = 20
SEGMENT_DISTANCE = -20


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()

    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment - 1].xcor()
            new_y = self.snake[segment - 1].ycor()
            self.snake[segment].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)

    def create_snake(self):
        x_cor = 0
        for _ in range(3):
            body = Turtle("square")
            body.color("white")
            body.penup()
            body.setx(x_cor)
            x_cor -= SEGMENT_DISTANCE
            self.snake.append(body)
