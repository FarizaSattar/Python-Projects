from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")  # Set the shape of the paddle to a square
        self.color("white")  # Set the color of the paddle to white
        self.shapesize(stretch_wid=5, stretch_len=1)  # Set the dimensions of the paddle
        self.penup()  # Lift the pen to avoid drawing when moving
        self.goto(position)  # Set the initial position of the paddle to the given position

    def go_up(self):
        # Move the paddle upwards by 20 units
        new_y = self.ycor() + 20  # Calculate the new y-coordinate
        self.goto(self.xcor(), new_y)  # Move the paddle to the new position

    def go_down(self):
        # Move the paddle downwards by 20 units
        new_y = self.ycor() - 20  # Calculate the new y-coordinate
        self.goto(self.xcor(), new_y)  # Move the paddle to the new position
