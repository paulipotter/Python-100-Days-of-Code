PLACEHOLDER = "[name]"

with open("Input/Names/guest_list.txt") as guest_list:
    names = guest_list.readlines()

with open("Input/Letter/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for item in names:
        name = item.strip().lower()
        new_letter = letter.replace(PLACEHOLDER, name)
        with open(f"./Output/Ready/letter_for_{name}.txt", mode="w") as finished_letter:
            finished_letter.write(new_letter)