from turtle import Turtle
from random import randint
BALL_COLOR = 'white'
MAX_MIN_WIDTH = 400
MAX_MIN_HEIGHT = 300
randheading = randint(0, 360)


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.create_middle_line()
        self.color(BALL_COLOR)
        self.shape('circle')
        self.penup()

    def ball_move(self, paddle1, paddle2):
        global randheading
        if self.pos()[1] >= MAX_MIN_HEIGHT or self.pos()[1] <= -MAX_MIN_HEIGHT:
            randheading = -randheading
            self.setheading(randheading)
        if paddle1.distance(self) < 51 and self.pos()[0] <= 360:
            randheading = -randheading
            self.setheading(randheading)
        elif paddle2.distance(self) < 51 and self.pos()[0] > -360:
            randheading = -randheading
            self.setheading(randheading)
        else:
            self.setheading(randheading)
        self.fd(20)

    def bounce_x(self):
        self.setposition(-self.xcor(), self.ycor())

    def create_middle_line(self):
        line = Turtle()
        line.hideturtle()
        line.penup()
        line.color(BALL_COLOR)
        line.goto(0, 300)
        line.setheading(270)
        line.pendown()
        while line.pos()[1] >= -300:
            line.fd(20)
            line.penup()
            line.fd(20)
            line.pendown()

