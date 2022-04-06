from turtle import Turtle
MOVE_DISTANCE = 20
SEGMENT_DISTANCE = -20
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment - 1].xcor()
            new_y = self.snake[segment - 1].ycor()
            self.snake[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def create_snake(self):
        x_cor = 0
        for _ in range(3):
            body = Turtle("square")
            body.color("white")
            body.penup()
            body.setx(x_cor)
            x_cor -= SEGMENT_DISTANCE
            self.snake.append(body)

    def up(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)
            self.move()

    def down(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)
            self.move()

    def left(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)
            self.move()

    def right(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)
            self.move()
