from art import *

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

operations = {
                "+": add,
                "-": substract,
                "/": divide,
                "*": multiply
            }
boolean = {
                "y": True,
                "n": False
            }
keep_going = True

while(keep_going):
    first_number = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    operation_request = input("Pick an operation from the line above: ")
    second_number = float(input("What's the first number?: "))

    #Get the desired 
    function = operations[operation_request]
    result = function(first_number, second_number)

    print(f"{first_number} {operation_request} {second_number} = {result}")
    choice = input("Would you like to do another calculation? y/n: ")
    keep_going = boolean[choice]

