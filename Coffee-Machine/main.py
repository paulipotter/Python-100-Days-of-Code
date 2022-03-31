
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


def check_resources(drink_choice):
    enough_resources = True
    drink_recipe = MENU[drink_choice]['ingredients']
    for ingredient in drink_recipe:
        if drink_recipe[ingredient] > resources[ingredient]:
            print(f"Sorry, there's no enough {ingredient}.")
            enough_resources = False
    return enough_resources


def process_coins():
    print()

def main_menu():
    machine_on = True
    money = 0
    while machine_on:
        menu_choice = input("What would you like? (espresso/latte/cappuccino):")

        if menu_choice == 'espresso' or menu_choice == 'latte' or menu_choice == 'capuccino':
            if not check_resources(menu_choice):
                continue
            else:
                print()
        elif menu_choice == 'off':
            print("The machine will now turn off.")
            machine_on = False
            quit()
        elif menu_choice == 'report':
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: {money}")


main_menu()