from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        # Set the shape of the paddle to a square
        self.shape("square")  
        # Set the color of the paddle to white
        self.color("white")  
        # Set the dimensions of the paddle
        self.shapesize(stretch_wid=5, stretch_len=1)  
        # Lift the pen to avoid drawing when moving
        self.penup()  
        # Set the initial position of the paddle to the given position
        self.goto(position)  

    def go_up(self):
        # Move the paddle upwards by 20 units and calculate the new y-coordinate
        new_y = self.ycor() + 20  
        # Move the paddle to the new position
        self.goto(self.xcor(), new_y)  

    def go_down(self):
        # Move the paddle downwards by 20 units and calculate the new y-coordinate
        new_y = self.ycor() - 20  
        # Move the paddle to the new position
        self.goto(self.xcor(), new_y)  
