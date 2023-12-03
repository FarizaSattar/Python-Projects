# Password Generator

''' The code generates a password based on user input for the number of letters, symbols, and numbers desired,
creating a randomized password with different difficulty levels. '''

# Importing the 'random' module to generate random numbers
import random

# Lists containing letters, numbers, and symbols
letters = ['a', 'b', 'c', ..., 'Z']  # List of letters
numbers = ['0', '1', ..., '9']  # List of numbers
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']  # List of symbols

# Displaying a welcome message for the password generator and prompting user for inputs
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Hard Level: Generating the password by combining characters into a list
password_list = []

# Adding random letters to the password list based on user input
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

# Adding random symbols to the password list based on user input
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

# Adding random numbers to the password list based on user input
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

# Displaying the generated password list before shuffling
print(password_list)

# Shuffling the password list to randomize the order of characters
random.shuffle(password_list)
print(password_list)

# Converting the password list into a string
password = ""
for char in password_list:
    password += char

# Displaying the final generated password to the user
print(f"Your password is: {password}")
