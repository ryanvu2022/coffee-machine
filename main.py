from data import MENU, resource

money = 0


def is_resource_sufficient(order_ingredients):
    """Check resources sufficient to make drink order."""
    for item in order_ingredients:
        if order_ingredients[item] > resource[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Process coins and return the total money received."""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01


def is_transaction_successful(money_received, cost_of_drink):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= cost_of_drink:
        change = round(money_received - cost_of_drink, 2)
        print(f"Here is ${change} in change.")
        global money
        money += cost_of_drink
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resource[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


coffee = ["espresso", "latte", "cappuccino"]

is_machine_off = False

while not is_machine_off:
    # Prompt user by asking what kind of coffee they want
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # Turn off the Coffee Machine by entering “ off ” to the prompt.
    if choice == "off":
        is_machine_off = True

    # Print report when user enters "report"
    elif choice == "report":
        print(f"Water: {resource['water']}ml")
        print(f"Milk: {resource['milk']}ml")
        print(f"Coffee: {resource['coffee']}g")
        print(f"Money: ${money}")

    elif choice in coffee:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid Input")
