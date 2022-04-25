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
def add_information():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    # Validate Entries
    if validate_entries(website, username, password):
        account_data = f"{website} | {username} | {password}"
        print(account_data)
        pyperclip.copy(password)

        # Write information to data file
        with open("data.txt", "a") as file:
            file.write(account_data)
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

website_input = Entry(width=38)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

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
add_info_btn = Button(text="Add", width=36, command=add_information)
add_info_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
