from math import fabs
from art import *
import os
from subprocess import call

def add(n1, n2):
    """Returns the sum of both parameters"""
    return n1 + n2

def substract(n1, n2):
    """Returns the substraction of both parameters"""
    return n1 - n2

def multiply(n1, n2):
    """Returns the product of both parameters"""
    return n1 * n2

def divide(n1, n2):
    """Returns the product of both parameters"""
    return n1 / n2

def clear():
    # Clear function - source: https://www.geeksforgeeks.org/clear-screen-python/
    _ = call('clear' if os.name =='posix' else 'cls')

operations = {
                "+": add,
                "-": substract,
                "/": divide,
                "*": multiply
            }

def calculator():
    print(logo)
    
    keep_going = True
    first_number = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    while(keep_going):
        operation_request = input("Pick an operation from the line above: ")
        second_number = float(input("What's the first number?: "))

        #Get the desired 
        function = operations[operation_request]
        result = function(first_number, second_number)

        print(f"{first_number} {operation_request} {second_number} = {result}")
        
        choice = input(f"""Type 'y' to continue calculating with {result}
Type 'n' to start a new calculation
Type 'e' to exit: """)

        if  choice == 'y':
            first_number = result
            clear()
        elif choice == 'n':
            calculator()
        else:
            break


calculator()