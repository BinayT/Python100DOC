from turtle import Turtle
BALL_COLOR = 'white'
MAX_MIN_WIDTH = 400
MAX_MIN_HEIGHT = 300


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.create_middle_line()
        self.current_ball = None
        self.create_ball()

    def create_ball(self):
        ball = Turtle('circle')
        ball.color(BALL_COLOR)
        ball.penup()
        self.current_ball = ball

    def ball_move(self):
        ball = self.current_ball
        new_x = ball.xcor() + 10
        new_y = ball.xcor() + 10
        ball.goto(new_x, new_y)


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

