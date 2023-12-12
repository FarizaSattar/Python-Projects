# Hirst Painting
''' The code draws 100 dots in various colors arranged in a grid-like format. '''

import turtle as turtle_module
import random

# Create object to paint the dots
turtle_module.colormode(255)
turtle_paint = turtle_module.Turtle()
turtle_paint.speed("fastest")
turtle_paint.penup()
turtle_paint.hideturtle()

# List of colours to use for dots
list_of_colours = [(202, 164, 109), (238, 240, 245), (150, 75, 49),
                   (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30,
                                                                    19),
                   (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35),
                   (145, 178, 148), (13, 99, 71), (233, 175, 164),
                   (161, 142, 158), (105, 74, 77), (55, 46, 50),
                   (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129),
                   (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153),
                   (174, 94, 97), (176, 192, 209)]

# Format the dots in a grid
turtle_paint.setheading(225)
turtle_paint.forward(300)
turtle_paint.setheading(0)
number_of_dots = 100

# Go through all 100 dots
for dot_counter in range(1, number_of_dots + 1):
  turtle_paint.dot(20, random.choice(list_of_colours))
  turtle_paint.forward(50)

  # Go to the next row after every 10 dots
  if dot_counter % 10 == 0:
    turtle_paint.setheading(90)
    turtle_paint.forward(50)
    turtle_paint.setheading(180)
    turtle_paint.forward(500)
    turtle_paint.setheading(0)

# Exit window after user clicks on screen
screen = turtle_module.Screen()
screen.exitonclick()
