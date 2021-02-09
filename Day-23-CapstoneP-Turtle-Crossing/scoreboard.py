from turtle import Turtle
FONT_SCORE = ("Courier", 18, "normal")
FONT_GAME_OVER = ("Courier", 24, "italic")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-230, 260)
        self.level = 1

    def update_scoreboard(self, level):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="center", font=FONT_SCORE)
        self.level = level

    def game_over(self):
        game_over = Turtle()
        game_over.penup()
        game_over.hideturtle()
        game_over.color('red')
        game_over.write(arg=f"Game Over.", align="center", font=FONT_GAME_OVER)
