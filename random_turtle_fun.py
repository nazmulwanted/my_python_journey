import turtle
import random

turtle.penup()
# List of colors
colors = ["red","green","blue","yellow","orange","black","purple"]

for x in range(50):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    # set a random position
    turtle.setposition(x,y)
    # set a random color from the color list
    i = random.randint(0,len(colors)-1)
    turtle.dot(colors[i])

turtle.done()
