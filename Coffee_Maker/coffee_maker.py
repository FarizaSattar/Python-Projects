class CoffeeMaker:
    """Models the machine that makes the coffee"""

    def __init__(self):
        """Initialize the resources available in the coffee maker."""
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all available resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """
        Checks whether there are enough resources to make the drink.

        Args:
        - drink: An object representing the desired drink.

        Returns:
        - True if there are enough resources, False otherwise.
        """
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """
        Makes the specified drink by deducting the required ingredients from the resources.

        Args:
        - order: An object representing the ordered drink.
        """
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
