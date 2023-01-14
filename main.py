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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def is_resources_sufficient(order_ingredients):
    """Return True when order can be made , false when insufficient resources"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is no enough {item}")
            is_enough = False
    return is_enough


def process_coins():
    """Returns the total calculated amount if inserted coins"""
    print("Please insert coins")
    total = int(input("How many quarters?"))*0.25
    total += int(input("How many dimes?"))*0.10
    total += int(input("How many nickles?"))*0.05
    total += int(input("How many pennies?"))*0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is the change {change}$")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(order_ingredients):
    """Reduce the resources from machine"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]


should_continue = True


while should_continue:
    choice = input("What would you like?espresso/latte/cappuccino\n")
    if choice == "off":
        should_continue = False
    elif choice == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money : ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, MENU[choice]["cost"]):
                make_coffee(drink["ingredients"])
                print(f"There is your {choice}☕")









