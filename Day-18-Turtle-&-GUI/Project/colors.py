import colorgram
import random

colors = colorgram.extract('image.jpg', 30)

colors_list = []
for x in range(len(colors)):
    colors_list.append((colors[x].rgb.r, colors[x].rgb.g, colors[x].rgb.b))


def choose_random():
    return random.choice(colors_list)