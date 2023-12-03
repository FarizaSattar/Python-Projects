class MoneyMachine:

    # Define currency
    CURRENCY = "$"

    # Define coin values
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        # Initialize the MoneyMachine object with profit and money received attributes
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        # Display the current profit in the console
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        # Ask the user to insert coins and calculate the total money received
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        # Process coins and check if the payment is sufficient for the cost
        self.process_coins()
        if self.money_received >= cost:
            # If payment is sufficient, calculate change, update profit, and reset money received
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            # If payment is insufficient, refund money and reset money received
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
