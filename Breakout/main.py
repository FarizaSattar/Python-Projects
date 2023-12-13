# Breakout

''' The code will allow the user to play a simplifed version of Breakout. '''

import turtle

# Create screen
wn = turtle.Screen()
wn.title("Breakout Clone")
wn.bgcolor("black")
wn.setup(width=600, height=600)

# Prevent automatic screen updates for smoother animation
wn.tracer(0)  

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()

# Adjust ball speed as needed
ball.speed(1) 
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Ball's x-axis movement
ball.dx = 2  

# Ball's y-axis movement
ball.dy = -2  

# Functions for paddle movement
def paddle_move_right():
    x = paddle.xcor()
    
    # Adjust speed as needed
    x += 20  
    
    # Check boundary to prevent paddle from going off-screen
    if x > 250:  
        x = 250
    paddle.setx(x)

def paddle_move_left():
    x = paddle.xcor()
    
    # Adjust speed as needed
    x -= 20  
    
    # Check boundary to prevent paddle from going off-screen
    if x < -250:  
        x = -250
    paddle.setx(x)

# Keyboard bindings for paddle movement
wn.listen()
wn.onkeypress(paddle_move_right, "Right")
wn.onkeypress(paddle_move_left, "Left")

# Main game loop
while True:
    
    # Update the screen
    wn.update() 

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Collision detection with walls
    # Right wall
    if ball.xcor() > 290:  
        ball.setx(290)
        ball.dx *= -1

    # Left wall
    if ball.xcor() < -290:  
        ball.setx(-290)
        ball.dx *= -1

    # Top wall
    if ball.ycor() > 290:  
        ball.sety(290)
        ball.dy *= -1

    # Bottom wall
    if ball.ycor() < -290:  
        ball.goto(0, 0)
        ball.dy *= -1

    # Collision detection with the paddle
    if (ball.ycor() < -240) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.sety(-240)
        ball.dy *= -1

    # Check if the ball is missed
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1
