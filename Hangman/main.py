# Hangman

''' The code implements a Hangman game where the user guesses letters to reveal a word from a predefined word
list, displaying hangman stages upon incorrect guesses, importing visuals and word lists from external files.
'''

import random

# Update the word list to use the 'word_list' from hangman_words.py
# Importing the 'word_list' from hangman_words.py module
from hangman_words import word_list

# Selecting a random word from the word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.
# Importing the 'logo' from hangman_art.py module and displaying it at the start
from hangman_art import logo
print(logo)

# Create blanks for the word to be guessed
display = []
for _ in range(word_length):
    display += "_"

# Main game loop
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter and update display if correct
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong and reduce lives
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Display the current state of the guessed word
    print(f"{' '.join(display)}")

    # Check if user has guessed all letters in the word
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Import the stages from hangman_art.py and make this error go away.
    # Importing 'stages' from hangman_art.py to display hangman stages based on remaining lives
    from hangman_art import stages
    print(stages[lives])
