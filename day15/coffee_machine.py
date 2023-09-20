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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def make_coffee(user_order, order_ingredients):
    global resources
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {user_order} ☕️. Enjoy!")

def is_resource_sufficient(user_order):
    for item in MENU[user_order]["ingredients"]:
        if MENU[user_order]["ingredients"][item] > resources[item]:
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def resource_report():
    """function to print remaining resources"""
    print(f"""
    Water: {resources['water']}ml
    Milk: {resources['milk']}ml
    Coffee: {resources['coffee']}g
    Money: ${profit}
    """)
is_on = True
while is_on:
    def what_to_do(user_order):
        global is_on
        if user_order == "off":
            is_on = False
        elif user_order in MENU:
            if is_resource_sufficient(user_order):
                print(f"The cost of {user_order} is ${MENU[user_order]['cost']}.")
                money_received = process_coins()
                if is_transaction_successful(money_received, MENU[user_order]['cost']):
                    make_coffee(user_order, MENU[user_order]['ingredients'])
            else:
                print(f"Sorry, not enough resources for {user_order}.")
        elif user_order == "report":
            resource_report()
        else:
            print("You entered an invalid choice.")

    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    what_to_do(user_input)
