from turtle import Turtle


class Snake:
    def __init__(self, x_pos, y_pos):
        self.turtle = Turtle('square')
        self.turtle.penup()
        self.turtle.color('white')
        self.turtle.setpos(x_pos, y_pos)
