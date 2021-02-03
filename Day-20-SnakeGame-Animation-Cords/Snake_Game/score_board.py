from turtle import Turtle
ALIGN = 'center'
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)

    def increase_score(self, score):
        self.score = score
        self.clear()
        self.update_scoreboard()


