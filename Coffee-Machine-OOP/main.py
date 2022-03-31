from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
coffee_maker = CoffeeMaker()
main_menu = Menu()
coin_processor = MoneyMachine()

while machine_on:
    menu_choice = input(f"What would you like? ({main_menu.get_items()}): ")
    if menu_choice == 'off':
        print("The machine will now turn off.")
        machine_on = False
    elif menu_choice == 'report':
        coffee_maker.report()
        coin_processor.report()
    elif menu_choice == 'espresso' or menu_choice == 'latte' or menu_choice == 'capuccino':
        chosen_drink = main_menu.find_drink(menu_choice)
        if coffee_maker.is_resource_sufficient(chosen_drink) and coin_processor.make_payment(chosen_drink.cost):
            coffee_maker.make_coffee(chosen_drink)
