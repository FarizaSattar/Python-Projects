# Tip Calculator
''' The code will help the user divide the bill amongst a group of people. '''

# Welcome Message
print("Welcome to the tip calculator!")

# Ask the user to input the total bill
total_bill = float(input("What is the total bill?\n$"))

# Ask the user to input the percent that they want to tip
tip_percent_int = int(
    input("How much tip do you want to give? Please type in a percent!\n"))

# Ask the user to input the number of people who will split the bill
total_people = int(input("How many people will be splitting the bill?\n"))

# Convert the percent from an integer to a decimal
tip_percent_decimal = tip_percent_int / 100

# Calculate the total bill with tip
total_bill_with_tip = total_bill * (1 + tip_percent_decimal)

# Calculate the bill per person
bill_per_person = total_bill_with_tip / total_people

# Round the answer to 2 decimal places
final_amount = "{:.2f}".format(bill_per_person)

# The final bill will be printed to the console
print(f"Each person should pay: ${final_amount}")
