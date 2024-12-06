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
            "milk": 100,
            "water": 250,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
# TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
# TODO: 3. Print report.
# TODO: 4. Check resources sufficient?
# TODO: 5. Process coins.
# TODO: 6. Check transaction successful?
# TODO: 7. Make Coffee.

def check_resource():
    for position, resource in resources.items():
        print(f"{position} = {resource}")


def sufficient_resources(ingredients):
    for item in ingredients:
        if ingredients[item] > resources.get(item, 0):
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def subtract_resources(ingredients):
    """Deduct the required ingredients from the resources."""
    for item in ingredients:
        resources[item] -= ingredients[item]

def process_coins(cost):
    quarters = int(input("How much quarters? "))
    dimes = int(input("How much dimes? "))
    nickles = int(input("How much nickles? "))
    pennies = int(input("How much pennies? "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

    if total < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif total > cost:
        change = round(total - cost, 2)
        print(f"Here is ${change} in change.")
    elif total == cost:
        pass

    print("Transaction successful!")
    return True

def user_choice():
    off = True

    while off:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == "report":
            check_resource()

        elif choice == 'off':
            print("Turning off the coffee machine.")
            off = False

        elif choice in MENU:
            if sufficient_resources(MENU[choice]["ingredients"]):
                subtract_resources(MENU[choice]["ingredients"])
                process_coins(MENU[choice]["cost"])
                print(f"Here is your {choice}. Enjoy!")
            else:
                print(f"Sorry, unable to prepare {choice}.")


        else:
            print("Invalid choice. Please try again.")


user_choice()
