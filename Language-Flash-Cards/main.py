from tkinter import *
import pandas, time
from random import choice


BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
KEYWORD_FONT = ("Ariel", 60, "bold")
FRENCH = "French"
ENGLISH = "English"

data = pandas.read_csv('./data/french_words.csv')
# Read Dict
vocab_to_learn = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(vocab_to_learn)
    french_term = current_card[FRENCH]
    canvas.itemconfig(card_language, text=FRENCH, fill='black')
    canvas.itemconfig(card_term, text=french_term, fill='black')
    canvas.itemconfig(card_background, image=flash_card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    english_term = current_card[ENGLISH]
    canvas.itemconfig(card_language, text=ENGLISH, fill='white')
    canvas.itemconfig(card_term, text=english_term, fill='white')
    canvas.itemconfig(card_background, image=flash_card_back)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card_front = PhotoImage(file='./images/card_front.png')
flash_card_back = PhotoImage(file='./images/card_back.png')
card_background = canvas.create_image(400, 263, image=flash_card_front)
canvas.grid(row=0, column=0, columnspan=2)
card_language = canvas.create_text(400, 150, font=LANGUAGE_FONT, text='')
card_term = canvas.create_text(400, 263, font=KEYWORD_FONT, text='')

#flash_card_back = PhotoImage(file='./images/card_back.png')

right_logo = PhotoImage(file='./images/right.png')
right_button = Button(image=right_logo, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

wrong_logo = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_logo, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)


window.mainloop()
