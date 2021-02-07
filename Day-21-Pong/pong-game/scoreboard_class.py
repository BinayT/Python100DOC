from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.score1 = 0
        self.score2 = 0

    def update_score(self, score1, score2):
        self.clear()
        self.score1 = score1
        self.score2 = score2
        self.write(arg=f"Player1: {self.score2}  Player2: {self.score1}", align='center',font=("Courier", 24, "normal"))
