# Higher Lower

''' The code utilizes Flask to create a simple number guessing game where a random number between 0 and 9 is 
generated, and users can guess the number through a web interface, receiving feedback based on their 
guesses. '''

from flask import Flask
import random

# Generate a random number between 0 and 9
random_number = random.randint(0, 9)
print(random_number)  # Print the generated random number

app = Flask(__name__)  # Create a Flask web application instance


@app.route('/')
def home():
    # Display initial message for the user to guess a number
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        # If guessed number is higher than the random number, display a message indicating it's too high
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < random_number:
        # If guessed number is lower than the random number, display a message indicating it's too low
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        # If guessed number matches the random number, display a success message
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app in debug mode