# Hangman
''' The code will allow the user to play a game of Hangman with the computer. '''

import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

# Pick a random word from file hangman_words and find the number of letters in it
chosen_word = random.choice(word_list)
letters_in_word = len(chosen_word)

# Create variable to tell computer when the game ends and give the user 6 lives
end_of_game = False
lives = 6

# Print logo at the start of the game
print(logo)

# Create a list and have it contain as many dashes as there are letters
word_to_guess = []
for _ in range(letters_in_word):
  word_to_guess += "_"

# This code will run until the user wins or loses the game. It will repeat everytime the user makes a guess
while not end_of_game:
  
  # Allow the user to guess a letter
  guessed_letter = input("Please guess a letter: ").lower()

  # If the user already guessed the letter 
  if guessed_letter in word_to_guess:
    print(f"You've already guessed {guessed_letter}!")

  ''' If the user has not guessed the letter before, we need to replace the dashes everytime that letter appears 
  in the word '''
  for letter_position in range(letters_in_word):
    current_letter = chosen_word[letter_position]
    # Replace the dash with the guessed letter
    if current_letter == guessed_letter:
      word_to_guess[letter_position] = current_letter

  # If the letter that the user guesses is not in the word
  if guessed_letter not in chosen_word:

    # We need to decrease the number of lives by 1 and end the game if the user is at 0 lives
    print(
        f"You guessed {guessed_letter}, that's not in the word. You lose a life."
    )
    lives -= 1
    if lives == 0:
      end_of_game = True
      print(f"You lose! The word was {chosen_word}!")

  print(f"{' '.join(word_to_guess)}")

  # If the user guessed all of the letters and there are no dashes left
  if "_" not in word_to_guess:
    end_of_game = True
    print("Congrats! You win!")

  # We need to print the ASCII art for each stage at the end of each attempt
  print(stages[lives])
  
