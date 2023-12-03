# Hirst Painting

''' The code uses the Turtle module in Python to draw a visual pattern of 100 dots in various colors arranged 
in a particular grid-like format. '''

import turtle as turtle_module  # Import the turtle module and alias it as turtle_module
import random  # Import the random module

turtle_module.colormode(255)  # Set the color mode to 255
tim = turtle_module.Turtle()  # Create a Turtle object and name it 'tim'
tim.speed("fastest")  # Set the drawing speed to the fastest
tim.penup()  # Lift the pen to prevent drawing
tim.hideturtle()  # Hide the turtle icon on the screen
color_list = [(202, 164, 109), (238, 240, 245), ...]  # List of RGB color tuples
tim.setheading(225)  # Set the initial heading direction
tim.forward(300)  # Move the turtle forward by 300 units
tim.setheading(0)  # Reset the heading direction to the default east
number_of_dots = 100  # Set the total number of dots to be drawn

# Loop to draw dots and navigate the turtle to form a grid-like pattern
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))  # Draw a dot with a random color from color_list
    tim.forward(50)  # Move the turtle forward by 50 units

    if dot_count % 10 == 0:  # Check if 10 dots have been drawn
        tim.setheading(90)  # Turn the turtle to face upwards
        tim.forward(50)  # Move the turtle upwards by 50 units
        tim.setheading(180)  # Turn the turtle to face left
        tim.forward(500)  # Move the turtle left by 500 units
        tim.setheading(0)  # Reset the turtle's direction to the right

# Create a turtle screen and keep it open until clicked
screen = turtle_module.Screen()
screen.exitonclick()
