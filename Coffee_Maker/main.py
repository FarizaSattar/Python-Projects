# Coffee Maker
''' The code creates a coffee maker where the user can order drinks. '''

# Import classes from modules
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Instances
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# Keep program running
coffee_maker_is_on = True

# While the coffee maker is on
while coffee_maker_is_on:

# Get drink options for the user
  drink_options = menu.get_items()
  
  # Ask the user to choose a drink
  user_choice = input(f"What would you like to drink? ({drink_options}):\n")

# If the user wants to turn off the coffee maker
  if user_choice == "off":
    coffee_maker_is_on = False
    
# If the user wants a report on the coffee maker
  elif user_choice == "report":
    coffee_maker.report()
    money_machine.report()
    
# Get the drink that the user wants from the menu
  else:
    user_drink = menu.find(user_choice)

    # Check if the coffee maker has enough resources and if the user has paid for the drink
    if coffee_maker.is_resource_sufficient(
        user_drink) and money_machine.make_payment(user_drink.cost):
      coffee_maker.make_coffee(user_drink)
