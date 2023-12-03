# Band Name Generator

''' The code prompts users to input their city of upbringing and pet's name to generate a band name by 
concatenating these inputs. '''

# Display a welcome message for the Band Name Generator
print("Welcome to the Band Name Generator.")

# Ask the user to input the name of the city they grew up in and store it in the variable 'street'
street = input("What's the name of the city you grew up in?\n")

# Ask the user to input their pet's name and store it in the variable 'pet'
pet = input("What's your pet's name?\n")

# Display a generated band name by combining the city name and the pet's name
print("Your band name could be " + street + " " + pet)
