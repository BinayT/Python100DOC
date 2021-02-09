from turtle import Turtle
SCOREBOARD_COLOR = 'white'
GAME_OVER_COLOR = 'red'
SCOREBOARD_FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.update_score()

    def update_score(self):
        self.penup()
        self.ht()
        self.color(SCOREBOARD_COLOR)
        self.goto(0, 270)
        self.clear()
        self.write(arg=f"Score: {self.score}  HighScore: {self.highscore}", align='center', font=SCOREBOARD_FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()

    # def game_over(self, score):
    #     self.penup()
    #     self.ht()
    #     self.color(GAME_OVER_COLOR)
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER!\nTotal: {score}", align='center', font=SCOREBOARD_FONT)
