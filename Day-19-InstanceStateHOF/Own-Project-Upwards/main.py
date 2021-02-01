from turtle import Turtle, Screen
# from random_color import random_color, random_forward

# screen = Screen()
# screen.colormode(255)
# screen.setup(width=700, height=640)

# colors = []
# for _ in range(6):
#     colors.append(random_color())

# turtles = []
# x_pos = -300
# for x in range(len(colors)):
#     tim = Turtle('turtle')
#     tim.color(colors[x])
#     tim.penup()
#     tim.setpos(x_pos+(x*120), -290)
#     tim.setheading(90)
#     turtles.append(tim)

# game_running = True
# while game_running:
#     for x in range(len(turtles)):
#         turtles[x].pendown()
#         turtles[x].pensize(6)
#         turtles[x].pencolor('red')
#         turtles[x].forward(random_forward())

        # if turtles[x].pos()[1] >= 290:
        #     game_running = False

# screen.exitonclick()

from turtle_class import MakeTurtle

screen = Screen()
screen.setup(width=700,height=640)
position=[-200,-100,0,100,150,200]
turtles = []
colors=['blue','red','yellow','green','black','purple']
for x in range(6):
    turtles.append(MakeTurtle(colors[x]))
    turtles[x].starting_position(-300+(x*120))

game_running = True
while game_running:
    for x in range(len(turtles)):
        turtles[x].move()
        if turtles[x].is_over():
            game_running = False



screen.exitonclick()






















