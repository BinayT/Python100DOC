from turtle import Screen,Turtle


screen = Screen()

screen.setup(width=500, height=400, startx=-100, starty=-100)

colors = ['red', 'green', 'orange', 'blue', 'yellow',  'purple']

# user_choice_turtle = int(screen.numinput(title="Make your bet:", prompt='''Choose the color of your turtle:\n
# Red = 1, Blue = 2, Purple = 3, Yellow = 4, Green = 5''', minval=1, maxval=5))

y_pos = -150
for x in range(len(colors)):
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(colors[x])
    new_turtle.goto(-230, y_pos)
    y_pos += 60


screen.exitonclick()