from turtle import Turtle
PADDLE_Y_MAX = 230
SHAPE = 'square'
COLOR = 'white'


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(pos)

    def move_up(self):
        paddle_pos_x = self.pos()[0]
        paddle_pos_y = self.pos()[1]
        if paddle_pos_y < PADDLE_Y_MAX:
            self.setpos(paddle_pos_x, paddle_pos_y+20)

    def move_down(self):
        paddle_pos_x = self.pos()[0]
        paddle_pos_y = self.pos()[1]
        if paddle_pos_y > -PADDLE_Y_MAX:
            self.setpos(paddle_pos_x, paddle_pos_y-20)


