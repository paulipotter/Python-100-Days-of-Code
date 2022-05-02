from turtle import Turtle
MOVE_DISTANCE = 20
SEGMENT_DISTANCE = -20
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]



class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

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

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
