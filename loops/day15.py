class CoffeeMachine:
    def __init__(self, menu, initial_resources):
        self.menu = menu
        self.profit = 0
        self.resources = initial_resources

    def is_resource_sufficient(self, order_ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in order_ingredients:
            if order_ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        total = int(input("how many quarters?: ")) * 0.25
        total += int(input("how many dimes?: ")) * 0.1
        total += int(input("how many nickels?: ")) * 0.05
        total += int(input("how many pennies?: ")) * 0.01
        return total

    def is_transaction_successful(self, money_received, drink_cost):
        """Return True when the payment is accepted, or False if money is insufficient."""
        if money_received >= drink_cost:
            change = round(money_received - drink_cost, 2)
            print(f"Here is ${change} in change.")
            self.profit += drink_cost
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

    def make_coffee(self, drink_name, order_ingredients):
        """Deduct the required ingredients from the resources."""
        for item in order_ingredients:
            self.resources[item] -= order_ingredients[item]
        print(f"Here is your {drink_name} ☕️. Enjoy!")

    def run(self):
        is_on = True
        while is_on:
            choice = input("What would you like? (espresso/latte/cappuccino): ")
            if choice == "off":
                is_on = False
            elif choice == "report":
                print(f"Water: {self.resources['water']}ml")
                print(f"Milk: {self.resources['milk']}ml")
                print(f"Coffee: {self.resources['coffee']}g")
                print(f"Money: ${self.profit}")
            else:
                drink = self.menu.get(choice)
                if drink:
                    if self.is_resource_sufficient(drink["ingredients"]):
                        payment = self.process_coins()
                        if self.is_transaction_successful(payment, drink["cost"]):
                            self.make_coffee(choice, drink["ingredients"])
                else:
                    print("Invalid selection. Please choose a valid drink from the menu.")


# Define MENU and initial resources
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

initial_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Create an instance of CoffeeMachine and run it
coffee_machine = CoffeeMachine(MENU, initial_resources)
coffee_machine.run()

