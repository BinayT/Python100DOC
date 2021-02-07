from turtle import Turtle
import winsound
SCORE_1 = 0
SCORE_2 = 0


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape('circle')
        self.color('white')
        self.penup()
        self.move_distance_x = 10
        self.move_distance_y = 10
        self.max_y = 286
        self.max_x = 330
        self.send_scores()

    def move(self, p1, p2):
        global SCORE_1, SCORE_2
        self.goto(self.xcor()+self.move_distance_x, self.ycor()+self.move_distance_y)
        if self.xcor() > 350 or self.xcor() < -350:
            self.goto(0, 0)
            self.move_distance_x *= -1

        if self.ycor() > self.max_y:
            self.sety(self.max_y)
            self.move_distance_y *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if self.ycor() < -self.max_y:
            self.sety(-self.max_y)
            self.move_distance_y *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if (self.xcor() == self.max_x) and (p1.ycor()+50 > self.ycor() > p1.ycor()-50):
            self.move_distance_x *= -1
            SCORE_1 += 1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        if (self.xcor() == -self.max_x) and (p2.ycor()+50 > self.ycor() > p2.ycor()-50):
            self.move_distance_x *= -1
            SCORE_2 += 1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    def send_scores(self):
        return (SCORE_1, SCORE_2)