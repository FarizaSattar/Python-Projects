# Pong

''' The code sets up a classic Pong game with two paddles, a ball, and a scoreboard using Turtle graphics, 
allowing players to control the paddles to hit the ball while keeping track of scores, running in an endless 
loop until exited by the user. '''

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
screen.tracer(0)  # Turn off automatic screen updates

# Create right and left paddles, ball, and scoreboard objects
r_paddle = Paddle((350, 0))  # Right paddle
l_paddle = Paddle((-350, 0))  # Left paddle
ball = Ball()  # Ball object
scoreboard = Scoreboard()  # Scoreboard object

# Listen for user inputs to control paddles
screen.listen()
screen.onkey(r_paddle.go_up, "Up")  # Right paddle moves up
screen.onkey(r_paddle.go_down, "Down")  # Right paddle moves down
screen.onkey(l_paddle.go_up, "w")  # Left paddle moves up
screen.onkey(l_paddle.go_down, "s")  # Left paddle moves down

game_is_on = True  # Flag to control the game loop
while game_is_on:
    screen.update()  # Update the screen manually
    ball.move()  # Move the ball in each iteration of the loop

    # Detect collision with top or bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()  # Reverse the vertical direction of the ball

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()  # Reverse the horizontal direction of the ball

    # Detect when right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()  # Reset the ball position
        scoreboard.l_point()  # Increase left player's score

    # Detect when left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()  # Reset the ball position
        scoreboard.r_point()  # Increase right player's score

# Exit the game when the screen is clicked
screen.exitonclick()
