# Pong
''' The code allows the user to play a game of Pong. '''

# Import necessary modules and classes
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
# Turn off automatic screen updates
screen.tracer(0)  

# Create right and left paddles, ball, and scoreboard objects
# Right paddle
r_paddle = Paddle((350, 0))  
# Left paddle
l_paddle = Paddle((-350, 0))  
# Ball object
ball = Ball()  
# Scoreboard object
scoreboard = Scoreboard()  

# Listen for user inputs to control paddles
screen.listen()
# Right paddle moves up
screen.onkey(r_paddle.go_up, "Up") 
# Right paddle moves down
screen.onkey(r_paddle.go_down, "Down")  
# Left paddle moves up
screen.onkey(l_paddle.go_up, "w")  
# Left paddle moves down
screen.onkey(l_paddle.go_down, "s")  

# Flag to control the game loop
game_is_on = True  
while game_is_on:
    # Update the screen manually
    screen.update()  
    # Move the ball in each iteration of the loop
    ball.move()  

    # Detect collision with top or bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Reverse the vertical direction of the ball
        ball.bounce_y()  

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        # Reverse the horizontal direction of the ball
        ball.bounce_x()  

    # Detect when right paddle misses the ball
    if ball.xcor() > 380:
        # Reset the ball position
        ball.reset_position()  
        # Increase left player's score
        scoreboard.l_point()  

    # Detect when left paddle misses the ball
    if ball.xcor() < -380:
        # Reset the ball position
        ball.reset_position()  
        # Increase right player's score
        scoreboard.r_point()  

# Exit the game when the screen is clicked
screen.exitonclick()
