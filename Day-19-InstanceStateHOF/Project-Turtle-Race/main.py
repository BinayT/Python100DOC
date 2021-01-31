from turtle import Screen, Turtle
import random

screen = Screen()

screen.setup(width=500, height=400, startx=-100, starty=-100)

colors = ['red', 'green', 'orange', 'blue', 'yellow',  'purple']
all_turtles = {}

user_choice_turtle = int(screen.numinput(title="Make your bet:", prompt='''Choose from number for your preferred color:
1:Red, 2:Green, 3:Orange, 4:Blue, 5:Yellow, 6:Purple''', minval=1, maxval=6))

y_pos = -150
for x in range(len(colors)):
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(colors[x])
    new_turtle.goto(-230, y_pos)
    all_turtles[x+1] = new_turtle
    y_pos += 60


game_running = True
winner = None
while game_running:
    position = 220
    for key in all_turtles:
        all_turtles[key].pendown()
        all_turtles[key].pencolor(all_turtles[key].color()[0])
        all_turtles[key].pensize(3)
        all_turtles[key].forward(random.randint(0, 10))
        if all_turtles[key].pos()[0] >= 220:
            game_running = False
            winner = key

if winner == user_choice_turtle:
    print(f"Your {all_turtles[winner].color()[0]} turtle won the race!")
else:
    print(f"You lost. The {all_turtles[winner].color()[0]} turtle won the race!")
screen.exitonclick()