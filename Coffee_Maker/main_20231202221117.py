# Coffee Maker

''' The code initializes a coffee machine system that interacts with a menu to enable users to select drinks, 
process payments, check resources, and make the chosen drink until turned off. '''

# Import necessary classes from respective modules
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Initialize instances of MoneyMachine, CoffeeMaker, and Menu
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# Set up a loop to keep the program running
is_on = True

while is_on:
    # Get available drink options from the menu
    options = menu.get_items()
    # Ask user for their choice
    choice = input(f"What would you like? ({options}): ")
    
    # Check the user's input
    if choice == "off":  # If the user wants to turn off the machine
        is_on = False
    elif choice == "report":  # If the user wants a report
        # Print reports for the CoffeeMaker and MoneyMachine
        coffee_maker.report()
        money_machine.report()
    else:
        # Find the chosen drink from the menu
        drink = menu.find_drink(choice)
        
        # Check if the coffee maker has enough resources and the user has made payment
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # If resources are sufficient and payment is made, make the drink
            coffee_maker.make_coffee(drink)
