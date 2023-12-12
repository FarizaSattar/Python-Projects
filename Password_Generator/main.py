# Password Generator

''' The code allows the user to generate a random password. '''

import random

# These lists contain letters, numbers, and symbols for the randomly generated password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
           'W', 'X', 'Y', 'Z'] 
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'] 

# Welcome Message
print("Welcome to the Password Generator!")

# Asks the user to input the number of letters they want in their password
number_of_letters = int(input("How many letters would you like in your password?\n"))
# Asks the user to input the number of symbols they want in their password
number_of_symbols = int(input("How many symbols would you like in your password?\n"))
# Asks the user to input the number of numbers they want in their password
number_of_numbers = int(input("How many numbers would you like in your password?\n"))

# This list will contain the random letters, symbols, and numbers in our randomly generated password
password_list = []

# These for loops will add randomly generated letters, symbols, and numbers to the password list
for char in range(1, number_of_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, number_of_symbols + 1):
    password_list.append(random.choice(symbols))
    
for char in range(1, number_of_numbers + 1):
    password_list.append(random.choice(numbers))

# The letters, numbers, and symbols in the list will be randomly rearranged
random.shuffle(password_list)

# This string will contain all of the letters, symbols, and numbers from the password list
password = ""

# This for loop will add all of the letters, symbols, and numbers from the list to the string
for char in password_list:
    password += char
    
# The randomly generated password will be output to the console
print(f"Your password is: {password}")