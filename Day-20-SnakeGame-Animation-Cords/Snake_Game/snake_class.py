from turtle import Turtle


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for x in range(4):
            turtle = Turtle('square')
            turtle.color('white')
            turtle.penup()
            turtle.goto(0 - (x * 20), 0)
            self.snakes.append(turtle)

    def move(self):
        for x in range(len(self.snakes) - 1, 0, -1):
            self.snakes[x].goto(self.snakes[x - 1].pos())

        self.snakes[0].forward(20)
        if self.snakes[0].pos() >= (270, 0):
            self.snakes[0].left(90)

