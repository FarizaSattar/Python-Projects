# Caesar Cipher

''' The code is a Caesar cipher program that encrypts or decrypts messages based on the user's choice and 
shift number, handling restart requests and addressing the possibility of entering non-alphabetic characters 
by preserving them in the encoded/decoded text. '''

# Define the alphabet as a list to handle shifts.
alphabet = ['a', 'b', 'c', ... , 'z']

# Define the Caesar cipher function that shifts the text based on the given direction and shift amount.
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1  # Reverse the shift if decoding.
    for char in start_text:
        # Preserve non-alphabetic characters during encoding/decoding.
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")

# Import and display the logo from art.py when the program starts.
from art import logo
print(logo)

# Create a loop to restart the cipher program based on user input.
should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    # Ensure the shift value is within the range of the alphabet by using modulus (%).
    shift = shift % 26
    
    # Call the caesar() function with user input.
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
