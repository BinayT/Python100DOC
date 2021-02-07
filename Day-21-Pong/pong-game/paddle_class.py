from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.speed(0)
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(pos)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.y_move = 20

    def move_up(self):
        if self.ycor() < 270:
            self.goto(self.xcor(), self.ycor()+self.y_move)

    def move_down(self):
        if self.ycor() > -270:
            self.goto(self.xcor(), self.ycor()-self.y_move)