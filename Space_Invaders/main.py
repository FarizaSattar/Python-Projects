# Space Invaders

''' The code allows the user to play Space Invaders. '''

import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 50, 50
ALIEN_WIDTH, ALIEN_HEIGHT = 50, 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shoot the Aliens!")

clock = pygame.time.Clock()

# Load images
spaceship_img = pygame.image.load('spaceship.png')  # Replace 'spaceship.png' with your spaceship image
alien_img = pygame.image.load('alien.png')  # Replace 'alien.png' with your alien image

# Scale images
spaceship_img = pygame.transform.scale(spaceship_img, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
alien_img = pygame.transform.scale(alien_img, (ALIEN_WIDTH, ALIEN_HEIGHT))

# Initialize variables
player_x = (SCREEN_WIDTH - SPACESHIP_WIDTH) // 2
player_y = SCREEN_HEIGHT - SPACESHIP_HEIGHT - 20
player_speed = 5

alien_x = random.randint(0, SCREEN_WIDTH - ALIEN_WIDTH)
alien_y = -ALIEN_HEIGHT
alien_speed = 3

# Game loop
running = True
while running:
    screen.fill(BLACK)  # Fill the screen with black color

    # Check for events
    for event in pygame.event.get():  
        # If the user clicks the close button
        if event.type == pygame.QUIT:  
            # Exit the game loop
            running = False  

    # Get the state of all keyboard keys
    keys = pygame.key.get_pressed()  
    # Move the player to the left
    if keys[pygame.K_LEFT] and player_x > 0:  
        player_x -= player_speed
    # Move the player to the right
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - SPACESHIP_WIDTH:  
        player_x += player_speed

    # Update alien position
    alien_y += alien_speed
    # If the alien reaches the bottom of the screen
    if alien_y > SCREEN_HEIGHT:  
        alien_x = random.randint(0, SCREEN_WIDTH - ALIEN_WIDTH)  # Reset its position randomly
        alien_y = -ALIEN_HEIGHT

    # Collision detection between player and alien
    if (player_x < alien_x + ALIEN_WIDTH and player_x + SPACESHIP_WIDTH > alien_x
            and player_y < alien_y + ALIEN_HEIGHT and player_y + SPACESHIP_HEIGHT > alien_y):
        # Game over if there is a collision between player and alien
        running = False

    # Display the player's spaceship and the alien on the screen
    screen.blit(spaceship_img, (player_x, player_y))
    screen.blit(alien_img, (alien_x, alien_y))

    # Update the display
    pygame.display.update() 

    # Control the frame rate
    clock.tick(60)  

# Quit Pygame
pygame.quit()  
