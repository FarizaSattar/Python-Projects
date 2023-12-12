# Caesar Cipher
''' The code will be able to encrypt and decrypt secret messages for the user. '''

from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# This function will encrypt or decrypt the user's secret message
def caesar(input_text, input_shift, input_direction):
  converted_text = ""
  if input_direction == "decode":
    input_shift *= -1
  for char in input_text:
    if char in alphabet:
      current_position = alphabet.index(char)
      new_position = current_position + input_shift
      converted_text += alphabet[new_position]
    else:
      converted_text += char

  print(f"Here's the {user_direction}d result: {converted_text}")

# Print logo to console
print(logo)

# This variable will indicate the end of the program
end_of_caesar_cipher = False

while not end_of_caesar_cipher:
  # The user will input if they want to encrypt or decrypt, secret message, and shift number
  user_direction = input(
      "Type 'encode' to encrypt and type 'decode' to decrypt\n").lower()
  user_text = input("Type your message:\n").lower()
  user_shift = int(input("Type the shift number:\n"))

  # For shift numbers greater than 26, we need to use the modulus to figure out which letter to use
  user_shift = user_shift % 26

  # Call the function above for the conversion
  caesar(input_text=user_text,
         input_shift=user_shift,
         input_direction=user_direction)

  # Ask the user if they want to continue using the program
  restart_caesar_cipher = input(
      "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart_caesar_cipher == "no":
    end_of_caesar_cipher = True
    print("Goodbye! Thank you for using Caesar Cipher today!")
