# EXAMPLE: new list =  [item for item in list]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Square all numbers
print([n**2 for n in numbers])

# Filter even numbers
print([n for n in numbers if n % 2 == 0])

# Get numbers in common from 2 files
with open("file1.txt") as file1:
    file1_data = [int(i) for i in file1.readlines()]
with open("file2.txt") as file2:
    file2_data = [int(i) for i in file2.readlines()]

print([number for number in file1_data if number in file2_data])
