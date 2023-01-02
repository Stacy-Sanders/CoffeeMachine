
# TODO: 1. Print a report of all coffee resources
# TODO: 2. Check resources sufficient to make drink order
# TODO: 3. Include current money in machine in resources
# TODO: 4. Create a function that checks resources based on consumer choice
# TODO: 5. Set global variable for coins

PENNY = 0.01
NICKEL = 0.05
DIME = 0.10
QUARTER = 0.25

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

resources = {
    "water": 300,  # 300
    "milk": 200,  # 200
    "coffee": 100,  # 100
    "money": 0,
}


def print_resources():
    """Prints the available amount of resources and money in machine."""
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g" +
          f"\nMoney: ${resources['money']:.2f}")


def check_resources(drink):
    """Watch video at about 15 minutes, her function is more streamlined, check need versus have with newly created
    variables, determine if sale is possible --> move to no_sale(resource) or payment(drink)"""
    # for item in MENU[drink]["ingredients"]:
    #     if MENU[drink]["ingredients"][item] > resources[item]:
    #         no_sale(item)
    # payment(drink)

    water_need = MENU[drink]["ingredients"]["water"]
    water_have = resources["water"]
    if water_need <= water_have:
        coffee_need = MENU[drink]["ingredients"]["coffee"]
        coffee_have = resources["coffee"]
        if coffee_need <= coffee_have:
            if "milk" in MENU[drink]["ingredients"]:
                milk_need = MENU[drink]["ingredients"]["milk"]
                milk_have = resources["milk"]
                if milk_need <= milk_have:
                    payment(drink)
                else:
                    no_sale("milk")
            else:
                payment(drink)
        else:
            no_sale("coffee")
    else:
        no_sale("water")


def reduce_resources(drink):
    """Rename-not reducing money, this function will add the total to our money and reduce the resources by the
    amount required by the drink"""
    resources["money"] += MENU[drink]["cost"]
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    if "milk" in MENU[drink]["ingredients"]:
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]


def payment(drink_cost):
    """Determines the cost based on the drink, Provide customer their total and ask them to insert coins.
    subtotal is calculated during each coin type step, if not enough money is refunded, no drink given. Else,
    give change if total is over cost, present drink, coffee emoji, and enjoy. If not change, skip that line."""
    cost = MENU[drink_cost]["cost"]
    print(f"Your total is {cost:.2f}. Please insert coins.")
    subtotal = QUARTER * int(input("How many quarters?  "))
    subtotal += DIME * int(input("How many dimes?  "))
    subtotal += NICKEL * int(input("How many nickels?  "))
    subtotal += PENNY * int(input("How many pennies?  "))
    total = round(subtotal, 2)
    if total < cost:
        print(f"Sorry, that's not enough money({total}). Money refunded.")
    else:
        change = total - cost
        reduce_resources(drink_cost)
        if change > 0:
            print(f"Here is ${round(change,2)} in change.\nHere is your {drink_cost} ☕️. Enjoy!")
        else:
            print(f"Here is your {drink_cost} ☕️. Enjoy!")


def no_sale(resource):
    """If resource is not sufficient provide customer with no sale message and what resource is not enough."""
    print(f"Sorry, there is not enough {resource}.")


def coffee_machine():  # want always on unless user enters end
    """Coffee machine function, to be repeated as long as machine_off is False. Checks for off, report, or
    coffee type. If invalid, starts over."""
    coffee_choice = input("What would you like? (espresso/latte/cappuccino):\n").lower()

    if coffee_choice == "off":
        return True
    elif coffee_choice == "report":
        print_resources()
    elif coffee_choice == "espresso" or coffee_choice == "latte" or coffee_choice == "cappuccino":
        check_resources(coffee_choice)
    else:
        print("Invalid selection.")


###############################################################
machine_off = False

while not machine_off:
    response = coffee_machine()
    if response:
        machine_off = True
    else:
        response

