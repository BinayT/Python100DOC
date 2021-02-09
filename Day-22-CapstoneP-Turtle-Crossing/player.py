from turtle import Turtle
TURTLE_SHAPE = 'turtle'
INITIAL_POS_Y = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(TURTLE_SHAPE)
        self.penup()
        self.setheading(90)
        self.goto(INITIAL_POS_Y)

    def moveup(self):
        self.goto(self.xcor(), self.ycor()+MOVE_DISTANCE)

    def movedown(self):
        if self.ycor() >= -270:
            self.goto(self.xcor(), self.ycor()-MOVE_DISTANCE)

    def moveright(self):
        if self.xcor() < 280:
            self.goto(self.xcor()+MOVE_DISTANCE, self.ycor())

    def moveleft(self):
        if self.ycor() >= -280:
            self.goto(self.xcor()-MOVE_DISTANCE, self.ycor())
