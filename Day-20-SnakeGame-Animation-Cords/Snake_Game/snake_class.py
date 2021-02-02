from turtle import Turtle
MOVE_DISTANCE = 20
INITIAL_POSITION = [(0, 0), (-20, 0), (-40, 0)]
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

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

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
