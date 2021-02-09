from turtle import Turtle
BALL_COLOR = 'white'
BALL_SHAPE = 'circle'
Y_MAX = 278


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOR)
        self.penup()
        self.move_x = 10
        self.move_y = 10

    def create_line(self):
        turtle = Turtle()
        turtle.hideturtle()
        turtle.penup()
        turtle.color(BALL_COLOR)
        turtle.goto(0, Y_MAX+20)
        turtle.setheading(270)
        while turtle.ycor() >= -Y_MAX-20:
            turtle.pendown()
            turtle.fd(20)
            turtle.penup()
            turtle.fd(20)

    def move(self):
        new_x = self.xcor()+self.move_x
        new_y = self.ycor()+self.move_y
        self.goto(new_x, new_y)

        if self.ycor() > Y_MAX or self.ycor() < -Y_MAX:
            self.move_y *= -1

    def bounce_paddle(self):
        self.move_x *= -1



