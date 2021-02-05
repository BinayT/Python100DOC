from turtle import Turtle
from random import randrange

FOOD_COLOR = 'blue'
FOOD_SHAPE = 'circle'


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.color(FOOD_COLOR)
        self.update_spot()

    def update_spot(self):
        self.clear()
        self.penup()
        x_pos = randrange(-280, 280, 20)
        y_pos = randrange(-280, 280, 20)
        self.goto(x_pos, y_pos)