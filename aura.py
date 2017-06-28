from turtle import *
import math
import random

# Name your Turtle.
t = Turtle()

my_colors = ["green", "orange", "red"]

setup(500,280)



x_pos=0
y_pos=0


t.setposition(x_pos, y_pos)

### Write your code below:


begin_fill()
while True :
	forward (200)
	pencolor(random.choice(my_colors))
	left (170)
	if abs (pos()) < 1:
		break








# Close window on click.
exitonclick()
