from turtle import Turtle
PADDLE_SHAPE = 'square'
PADDLE_COLOR = 'white'
Y_LIMIT = 260


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape(PADDLE_SHAPE)
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=6)
        self.color(PADDLE_COLOR)
        self.goto(pos)

    def up(self):
        if self.ycor() <= Y_LIMIT:
            self.goto(self.xcor(), self.ycor()+20)

    def down(self):
        if self.ycor() >= -Y_LIMIT:
            self.goto(self.xcor(), self.ycor()-20)
