# Space Invaders

''' The code uses Pygame to create a simple game where a player controls a spaceship to avoid collisions with 
falling aliens, implemented with movement, collision detection, and a game loop for continuous gameplay. '''

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

    for event in pygame.event.get():  # Check for events
        if event.type == pygame.QUIT:  # If the user clicks the close button
            running = False  # Exit the game loop

    keys = pygame.key.get_pressed()  # Get the state of all keyboard keys
    if keys[pygame.K_LEFT] and player_x > 0:  # Move the player to the left
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - SPACESHIP_WIDTH:  # Move the player to the right
        player_x += player_speed

    # Update alien position
    alien_y += alien_speed
    if alien_y > SCREEN_HEIGHT:  # If the alien reaches the bottom of the screen
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

    pygame.display.update()  # Update the display
    clock.tick(60)  # Control the frame rate

pygame.quit()  # Quit Pygame
