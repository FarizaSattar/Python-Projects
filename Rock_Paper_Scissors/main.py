# Rock Paper Scissors
''' The code allows the user to play a Rock, Paper, Scissors game against the computer. '''

import random

# ASCII art 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Create an array that contains all of the images for rock, paper, and scissors
game_images = [rock, paper, scissors]

# Asks the user to choose between rock, paper, and scissors
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

# Prints the user's choice to the console
print(game_images[user_choice])

# Generate a random integer between 0 to 2 for the computer
computer_choice = random.randint(0, 2)

# Prints the computer's choice to the console
print("Computer chose:")
print(game_images[computer_choice])

# Checks to make sure that the user does not find an integer greater than 2 or less than 0
if user_choice >= 3 or user_choice < 0:
    print("You lose! You typed an invalid number!")

# Checks to see if the user's choice and computer's choice is the same
elif user_choice == computer_choice:
    print("It's a draw!")
    
# Checks to see if the user has rock and the computer has scissors
elif user_choice == 0 and computer_choice == 2:
    print("You win!")

# Checks to user has scissors and the computer has rock
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
    
# Checks if the user has paper and the computer has rock or if the user has scissors and the computer has paper
elif user_choice > computer_choice:
    print("You win!")

# Checks if the user has rock and the computer has paper or if the user has paper and the computer has scissors
elif user_choice < computer_choice:
    print("You lose!")