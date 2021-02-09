from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from cars import Cars
from time import sleep

screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
cars = Cars()

screen.onkey(player.moveup, 'w')
screen.onkey(player.moveup, 'Up')
screen.onkey(player.movedown, 's')
screen.onkey(player.movedown, 'Down')
screen.onkey(player.moveright, 'Right')
screen.onkey(player.moveright, 'd')
screen.onkey(player.moveleft, 'a')
screen.onkey(player.moveleft, 'Left')


level = 1
game_on = True
while game_on:
    screen.update()
    scoreboard.update_scoreboard(level)
    cars.move_car(level)
    if player.ycor() >= 285:
        level += 1
        sleep(0.5)
        player.goto(0, -280)

    for car in cars.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_on = False


screen.exitonclick()
