from turtle import Turtle
POSITION = [(0, 20), (0, 0), (0, -20)]


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddles = []
        self.create_paddle()

    def create_paddle(self):
        for x in POSITION:
            self.paddle_body(x)

    def paddle_body(self, pos):
        paddle = Turtle('square')
        paddle.penup()
        paddle.color('white')
        paddle.goto(pos)
        self.paddles.append(paddle)

    def move_up(self):
        for x in range(1, len(self.paddles), -1):
            self.paddles[x].setpos(x-1)
        self.paddles[0].setheading(90)
        self.paddles[0].forward(20)
