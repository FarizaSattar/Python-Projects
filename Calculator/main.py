# Calculator

''' The code defines a simple calculator program that prompts the user for numerical inputs and operations, 
using functions for addition, subtraction, multiplication, and division, and includes a clear screen function
using the 'os' module to support a user-friendly interface in a loop until the user decides to exit. '''

import os  # Import the 'os' module for console screen clearing
from art import logo  # Import the logo for display

def clear_screen():
    os.system('clear')  # Use 'clear' for UNIX-based systems like VS Code

# Define arithmetic functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Store arithmetic operations in a dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Calculator function
def calculator():
    print(logo)  # Display the calculator logo

    num1 = float(input("What's the first number?: "))  # Prompt user for the first number
    for symbol in operations:  # Display available operation symbols
        print(symbol)
    should_continue = True  # Flag to control continuation of calculations
 
    while should_continue:
        operation_symbol = input("Pick an operation: ")  # Prompt user for operation choice
        num2 = float(input("What's the next number?: "))  # Prompt user for the second number
        calculation_function = operations.get(operation_symbol)  # Get the corresponding arithmetic function
        if calculation_function:
            answer = calculation_function(num1, num2)  # Perform calculation using chosen operation
            print(f"{num1} {operation_symbol} {num2} = {answer}")  # Display calculation result

            # Ask user to continue with the answer or start a new calculation
            if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
                num1 = answer  # Use the result as the new starting number
            else:
                should_continue = False  # Exit the loop to start a new calculation
                clear_screen()  # Clear the screen before starting a new calculation
                calculator()  # Restart the calculator function
        else:
            print("Invalid operation symbol!")  # Display an error for an invalid operation symbol
            should_continue = False  # Exit the loop due to invalid input

calculator()  # Start the calculator
