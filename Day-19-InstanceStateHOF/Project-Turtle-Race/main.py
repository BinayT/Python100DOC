from turtle import Screen, Turtle

screen = Screen()

screen.setup(width=500, height=400, startx=-100, starty=-100)

colors = ['red', 'green', 'orange', 'blue', 'yellow',  'purple']
all_turtles = {}

user_choice_turtle = int(screen.numinput(title="Make your bet:", prompt='''Choose from number for your preferred color:
1:Red, 2:Blue, 3:Orange, 4:Blue, 5:Yellow, 6:Purple''', minval=1, maxval=5))

y_pos = -150
for x in range(len(colors)):
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(colors[x])
    new_turtle.goto(-230, y_pos)
    all_turtles[x+1] = colors[x]
    y_pos += 60

#TODO = While turtle isn't on positon 220, don't stop the game




screen.exitonclick()