# Tip Calculator

''' The code is a tip calculator that takes the total bill, desired tip percentage, and number of people to 
split the bill among, calculating the amount each person should pay and displaying it. '''

# Display a welcome message for the tip calculator
print("Welcome to the tip calculator!")

# Ask the user to input the total bill amount and convert it to a floating-point number
bill = float(input("What was the total bill? $"))

# Ask the user to input the desired tip percentage (10, 12, or 15)
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

# Ask the user to input the number of people to split the bill among
people = int(input("How many people to split the bill?"))

# Calculate the tip percentage as a decimal
tip_as_percent = tip / 100

# Calculate the total tip amount based on the bill and tip percentage
total_tip_amount = bill * tip_as_percent

# Calculate the total bill including the tip
total_bill = bill + total_tip_amount

# Calculate the amount each person should pay by dividing the total bill by the number of people
bill_per_person = total_bill / people

# Round the final amount to two decimal places
final_amount = round(bill_per_person, 2)

# Display the amount each person should pay
print(f"Each person should pay: ${final_amount}")
