from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.paddle = []
        self.create_paddle(pos)

    def create_paddle(self, pos):
        paddle = Turtle('square')
        paddle.color('white')
        paddle.penup()
        paddle.shapesize(stretch_len=1, stretch_wid=5)
        paddle.goto(pos)
        self.paddle.append(paddle)

    def move_up(self):
        y_pos = self.paddle[0].pos()[1]
        x_pos = self.paddle[0].pos()[0]
        if y_pos >= 240:
            return

        if x_pos == -360:
            self.paddle[0].setpos(-360, y_pos+20)
        else:
            self.paddle[0].setpos(350, y_pos+20)

    def move_down(self):
        y_pos = self.paddle[0].pos()[1]
        x_pos = self.paddle[0].pos()[0]
        if y_pos <= -240:
            return

        if x_pos == -360:
            self.paddle[0].setpos(-360, y_pos-20)
        else:
            self.paddle[0].setpos(350, y_pos-20)

