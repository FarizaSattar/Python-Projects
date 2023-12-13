from turtle import Turtle  
import random  

    # Class to represent food in the game
class Food(Turtle):

    # Constructor method to initialize the Food object
    def __init__(self):
        super().__init__()  # Initialize the Food object as a Turtle
        self.shape("circle")  # Set the shape of the Food object as a circle
        self.penup()  # Lift the pen to avoid drawing lines while moving
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Set the size of the food
        self.color("blue")  # Set the color of the food to blue
        self.speed("fastest")  # Set the speed of the food object
        self.refresh()  # Call the refresh method to position the food randomly

    # Method to refresh the position of the food
    def refresh(self):
        random_x = random.randint(-280, 280)  # Generate a random x-coordinate within the screen boundaries
        random_y = random.randint(-280, 280)  # Generate a random y-coordinate within the screen boundaries
        self.goto(random_x, random_y)  # Move the food to the randomly generated position
