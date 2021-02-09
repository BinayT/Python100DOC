from turtle import Turtle
import time
SNAKE_SHAPE = 'square'
SNAKE_BODY_COLOR = 'white'
SNAKE_INITIAL_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_body = []
        self.snake_body_creator()
        self.snake_head = self.snake_body[0]

    def snake_body_creator(self):
        for position in SNAKE_INITIAL_POSITION:
            snake = Turtle(SNAKE_SHAPE)
            snake.color(SNAKE_BODY_COLOR)
            snake.penup()
            snake.goto(position)
            self.snake_body.append(snake)

    def snake_body_update(self):
        snake = Turtle(SNAKE_SHAPE)
        snake.color(SNAKE_BODY_COLOR)
        snake.penup()
        snake.goto(self.snake_body[-1].pos())
        self.snake_body.append(snake)

    def snake_reset(self):
        for x in self.snake_body:
            x.goto(1000, 1000)
        self.snake_body.clear()
        self.snake_body_creator()
        self.snake_head = self.snake_body[0]

    def move(self):
        for x in range(len(self.snake_body)-1, 0, -1):
            self.snake_body[x].setposition(self.snake_body[x-1].pos())
        self.snake_head.fd(20)

    def move_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def move_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def move_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def move_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
