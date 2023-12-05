# NATO Alphabet

''' The code utilizes Pandas to read a CSV file containing the NATO phonetic alphabet, creating a dictionary 
mapping letters to their corresponding phonetic codes and allowing users to input a word to retrieve its 
phonetic representation using the NATO alphabet. '''

# Import the Pandas library for data manipulation
import pandas

# Read the CSV file containing the NATO phonetic alphabet
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary mapping letters to their corresponding phonetic codes
# Use dictionary comprehension to iterate through rows in the DataFrame and create the dictionary
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)  # Display the created phonetic dictionary

# Retrieve the phonetic code words for a word entered by the user
word = input("Enter a word: ").upper()  # Prompt the user to input a word and convert it to uppercase
# Create a list comprehension to get the phonetic codes corresponding to each letter in the input word
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)  # Display the list of phonetic code words for the entered word
