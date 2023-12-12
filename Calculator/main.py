# Calculator
''' The code will allow the user to solve basic addition, subtraction, multiplication and division calculations. '''

import os
from art import logo


# This function will clear the console
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  


# Functions that perform all math operations
def addition(n1, n2):
  return n1 + n2


def subtraction(n1, n2):
  return n1 - n2


def multiplication(n1, n2):
  return n1 * n2


def division(n1, n2):
  return n1 / n2


# Dictionary that will contain the signs for all math operations
all_math_operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

# Print logo to console
print(logo)


def perform_calculation():
  # Ask the user to input the first number in the math calculation
  num1 = float(input("What is the first number?\n"))

  # Print all of the math operations that the calculator can perform for the user
  for sign in all_math_operations:
    print(sign)

  # Ask the user to input the operation in the math calculator
  math_operation_key = input("Please pick a math operation?\n")

  # Check to make sure that the user entered a valid math operation
  while True:
    if math_operation_key in all_math_operations:
      break
    else:
      print("That is an invalid operation symbol! Please try again!")
      math_operation_key = input("Please pick a math operation?\n")

  # Ask the user to input the second number in the math calculation
  num2 = float(input("What is the second number?\n"))

  # Obtain the value associated with the key in the math operation dictionary
  math_operation_value = all_math_operations.get(math_operation_key)

  # Check to make sure that there is a value inside math_operation_value. If there is, the calculation will be executed
  if math_operation_value:
    final_answer = math_operation_value(num1, num2)
    print(f"{num1} {math_operation_key} {num2} = {final_answer}")

  # Ask the user if they would like to continue using the calculator
  continue_calculator = input(
      f"Type 'y' to continue using the calculator, or type 'n' to leave the calculator:\n"
  )

  # Check to make sure that the user entered a valid value
  continue_calculator_values = ['y', 'n', 'Y', 'N']

  while True:
    if continue_calculator in continue_calculator_values:
      break  # Break the loop if the input is valid
    else:
      print("That is an invalid value! Please try again!")
      continue_calculator = input(
          f"Type 'y' to continue using the calculator, or type 'n' to leave the calculator:\n"
      )

  # If the user wants to continue using the calculator
  if continue_calculator == 'y':
    clear_screen()
    perform_calculation()

  # If the user does not want to use the calculator anymore
  else:
    clear_screen()
    print("Goodbye! Thank you for using the calculator!")

# Start the calculator
perform_calculation()