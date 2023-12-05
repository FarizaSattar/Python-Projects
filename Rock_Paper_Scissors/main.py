# Rock Paper Scissors

''' The code simulates a Rock, Paper, Scissors game between a user and the computer, displaying ASCII art for 
the chosen items and determining the winner based on their selections. '''

# Importing the 'random' module to generate random numbers
import random

# ASCII art for Rock, Paper, and Scissors images
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

# Storing the ASCII images in a list for easy access
game_images = [rock, paper, scissors]

# Asking the user for their choice: Rock, Paper, or Scissors (0 for Rock, 1 for Paper, 2 for Scissors)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

# Displaying the ASCII art for the user's chosen item
print(game_images[user_choice])

# Generating a random choice for the computer (0 for Rock, 1 for Paper, 2 for Scissors)
computer_choice = random.randint(0, 2)

# Displaying the ASCII art for the computer's chosen item
print("Computer chose:")
print(game_images[computer_choice])

# Determining the winner based on the user's choice and the computer's choice
if user_choice >= 3 or user_choice < 0: 
    print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw")
