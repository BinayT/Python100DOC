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
        self.current_ball = None
        self.create_ball()
        self.y = self.current_ball.pos()[1]

    def create_ball(self):
        ball = Turtle('circle')
        ball.color(BALL_COLOR)
        ball.penup()
        self.current_ball = ball

    def ball_move(self):
        global randheading
        ball = self.current_ball
        if ball.pos()[1] >= MAX_MIN_HEIGHT or ball.pos()[1] <= -MAX_MIN_HEIGHT:
            randheading = -randheading

        ball.setheading(randheading)
        ball.fd(20)

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

