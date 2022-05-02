
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


money = 0


def deduct_resources(drink_choice):
    drink_recipe = MENU[drink_choice]['ingredients']
    for ingredient in drink_recipe:
        resources[ingredient] -= drink_recipe[ingredient]


def check_resources(drink_choice):
    enough_resources = True
    drink_recipe = MENU[drink_choice]['ingredients']
    for ingredient in drink_recipe:
        if drink_recipe[ingredient] > resources[ingredient]:
            print(f"Sorry, there's no enough {ingredient}.")
            enough_resources = False
    return enough_resources


def process_coins():
    total = 0
    total += float(input("How many quarters? ")) * 0.25
    total += float(input("How many dimes? ")) * 0.1
    total += float(input("How many nickles? ")) * 0.05
    total += float(input("How many pennies? ")) * 0.01
    return round(total, 2)


def process_transaction(drink, coins):
    success = False
    drink_cost = MENU[drink]['cost']
    if drink_cost > coins:
        print("Sorry that's not enough money. Money refunded.")
        return success
    elif drink_cost <= coins:
        success = True
        change = round(coins - drink_cost, 2)
        print(f"Here's ${change} in change.")
        global money
        money += drink_cost
        return success


def main_menu():
    machine_on = True
    while machine_on:
        menu_choice = input("What would you like? (espresso/latte/cappuccino): ")

        if menu_choice == 'espresso' or menu_choice == 'latte' or menu_choice == 'capuccino':
            if not check_resources(menu_choice):
                continue
            else:
                user_coins = process_coins()
                if process_transaction(menu_choice, user_coins):
                    deduct_resources(menu_choice)
                    print(f"Here's your {menu_choice}, Enjoy! ☕")
        elif menu_choice == 'off':
            print("The machine will now turn off.")
            machine_on = False
            quit()
        elif menu_choice == 'report':
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money}")


main_menu()
