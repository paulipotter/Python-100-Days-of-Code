from turtle import Turtle, Screen


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.write(f"Score: {self.score}", align='center', font=('Arial', 24, 'normal'))
        self.color('white')
        self.goto(self.xcor(), self.ycor() + 280)
