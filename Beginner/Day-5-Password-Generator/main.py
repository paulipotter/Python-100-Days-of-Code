from random import choice, shuffle

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','.','-','_','@','#','$','%','&','*']

print("Welcome to the PyPassword Generator!")
print("Please choose the number of each item for your password:")
count_letters = int(input("Letters: "))
count_numbers = int(input("Numbers: "))
count_symbols = int(input("Symbols: "))

password_list = []

for char in range(1, count_letters + 1):
    password_list.append(choice(alphabet))

for char in range(1, count_numbers + 1):
    password_list.append(choice(numbers))

for char in range(1, count_symbols + 1):
    password_list.append(choice(symbols))

shuffle(password_list)
print(*password_list, sep="")
