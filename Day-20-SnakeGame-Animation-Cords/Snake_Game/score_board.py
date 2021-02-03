from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def increase_score(self, score):
        self.score = score
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))


