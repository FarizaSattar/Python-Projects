# NATO Alphabet
''' The code allows users to input a word and retrieve its phonetic representation using the NATO alphabet. '''

import pandas

# Read CSV file 
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create dictionary mapping letters to corresponding phonetic codes
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)  

# Retrieve the phonetic code words for a word entered by the user
word = input("Please enter a word: ").upper()  
output_list = [phonetic_dict[letter] for letter in word]

# List phonetic code words for entered word
print(output_list)  