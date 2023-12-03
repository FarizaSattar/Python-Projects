from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        # Initialize a Ball object
        super().__init__()  # Call the constructor of the superclass (Turtle)
        self.color("white")  # Set color of the ball to white
        self.shape("circle")  # Set the shape of the ball to a circle
        self.penup()  # Lift the pen to avoid drawing when moving
        self.x_move = 3  # Set initial horizontal movement
        self.y_move = 3  # Set initial vertical movement
        self.move_speed = 0.1  # Set the initial speed of the ball

    def move(self):
        # Move the ball by adding x_move and y_move to its current position
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)  # Set the new position of the ball

    def bounce_y(self):
        # Reverse the vertical direction of the ball's movement
        self.y_move *= -1

    def bounce_x(self):
        # Reverse the horizontal direction of the ball's movement
        self.x_move *= -1
        # Speed up the ball movement by reducing the move_speed
        self.move_speed *= 0.9

    def reset_position(self):
        # Reset the ball's position to the center of the screen
        self.goto(0, 0)
        self.move_speed = 0.1  # Reset the ball's speed
        self.bounce_x()  # Reverse the horizontal direction of movement
