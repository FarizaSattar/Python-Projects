# Text to Morse Converter

''' The code converts text to Morse code by using a dictionary to map characters to their respective Morse 
code equivalents, iterating through the input text and replacing each character with its Morse code 
representation while preserving non-alphanumeric characters, and then displaying the converted Morse code. '''

# Morse code dictionary mapping characters to their Morse code equivalents
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'  # Adding space to be represented as a forward slash in Morse code
}

# Function to convert text to Morse code
def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '  # If character is in the dictionary, add its Morse code equivalent
        else:
            morse_code += char  # Keep non-alphanumeric characters as they are
    return morse_code.strip()  # Remove trailing space at the end

# Example usage:
text_input = input("Enter text to convert to Morse code: ")
converted_text = text_to_morse(text_input)
print(f"Morse code: {converted_text}")  # Display the converted Morse code
