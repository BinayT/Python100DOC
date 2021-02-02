from turtle import Turtle
MOVE_DISTANCE = 20
INITIAL_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for x in range(3):
            turtle = Turtle('square')
            turtle.color('white')
            turtle.penup()
            turtle.goto(INITIAL_POSITION[x])
            self.snakes.append(turtle)

    def move(self):
        for x in range(len(self.snakes) - 1, 0, -1):
            self.snakes[x].goto(self.snakes[x - 1].pos())

        self.snakes[0].forward(MOVE_DISTANCE)
        # if self.snakes[0].pos() >= (270, 0):
        #     self.snakes[0].left(90)

    def up(self):
        if self.snakes[0].heading() == 0 or self.snakes[0].heading() == 180:
            self.snakes[0].setheading(90)

    def down(self):
        if self.snakes[0].heading() == 0 or self.snakes[0].heading() == 180:
            self.snakes[0].setheading(270)

    def left(self):
        if self.snakes[0].heading() == 90 or self.snakes[0].heading() == 270:
            self.snakes[0].setheading(180)

    def right(self):
        if self.snakes[0].heading() == 90 or self.snakes[0].heading() == 270:
            self.snakes[0].setheading(0)
