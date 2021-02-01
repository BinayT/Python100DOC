from turtle import Turtle
import random


class MakeTurtle:

    def __init__(self, cor):
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.color(cor)
        self.turtle.shape("turtle")
        self.turtle.speed(3)

    def starting_position(self, position):
        self.turtle.goto(-240, position)

    def move(self):
        self.turtle.forward(random.randint(1, 10))
        self.turtle.pendown()
        self.turtle.pensize(4)
        self.turtle.pencolor(self.turtle.color()[0])

    def is_over(self):
        if self.turtle.pos()[0] >= 230.0:
            # Will return a Truthy Value ending the while loop and giving me the result
            return self.turtle.color()[0]
        else:
            return False