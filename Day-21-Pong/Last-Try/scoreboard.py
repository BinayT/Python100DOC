from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 260)
        self.score1 = 0
        self.score2 = 0

    def update_score(self, s1, s2):
        self.clear()
        self.write(arg=f"Player1: {s1}  Player2: {s2}", align="center", font=("Courier", 24, "normal"))
        self.score1 += s1
        self.score2 += s2

