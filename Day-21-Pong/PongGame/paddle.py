from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle = []
        self.create_paddle()
        self.y_pos = self.paddle[0].pos()[1]
        self.x_pos = self.paddle[0].pos()[0]

    def create_paddle(self):
        paddle = Turtle('square')
        paddle.color('white')
        paddle.penup()
        paddle.shapesize(stretch_len=1, stretch_wid=5)
        paddle.goto(350, 0)
        self.paddle.append(paddle)

    def move_up(self):
        y_pos = self.paddle[0].pos()[1]
        if y_pos >= 240:
            return
        self.paddle[0].setpos(350, y_pos+20)

    def move_down(self):
        y_pos = self.paddle[0].pos()[1]
        if y_pos <= -240:
            return
        self.paddle[0].setpos(350, y_pos-20)

