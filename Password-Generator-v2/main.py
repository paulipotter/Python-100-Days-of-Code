import json
from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '.', '-', '_', '@', '#', '$', '%', '&', '*']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_numbers + password_letters
    shuffle(password_list)

    password_str = "".join(password_list)
    password_input.insert(0, password_str)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    # Validate Entries
    if validate_entries(website, username, password):
        new_data = {website: {
            "email": username,
            "password": password
        }}
        print(new_data)
        pyperclip.copy(password)
        try:
            # Write information to data file
            with open("data.json", "r") as file:
                # Read/Import json to python dict
                data = json.load(file)
        except FileNotFoundError:
            # Create new data.json file
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # If file exists, Update dict to add new data
            data.update(new_data)
            with open("data.json", "w") as file:
                # Add python dict to json
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            display_messagebox("Your info was added successfully!")
    else:
        display_messagebox("Please make sure to not leave any fields empty.")


def display_messagebox(message_text):
    messagebox.showinfo(title="Password Generator", message=message_text)


def validate_entries(website, username, password):
    if len(website) < 2 or '@' not in username or len(password) < 2:
        return False
    else:
        return True


def find_password():
    website = website_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        display_messagebox("No data file found.")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            display_messagebox(f"Email: {email} \nPassword: {password}")
            pyperclip.copy(password)
        else:
            display_messagebox(f"No details for the {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=50)

logo = Canvas(width=202, height=202)
logo_img = PhotoImage(file="logo.png")
logo.create_image(100, 100, image=logo_img)
logo.grid(row=0, column=1)

# Website Input
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()

website_search = Button(text="Search", width=13, command=find_password)
website_search.grid(row=1, column=2)

# Username Input
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_input = Entry(width=38)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "email@example.com")

# Password Input
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

password_btn = Button(text="Generate Password", width=13, command=generate_password)
password_btn.grid(row=3, column=2)

# Add to list button
add_info_btn = Button(text="Add", width=36, command=save)
add_info_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
