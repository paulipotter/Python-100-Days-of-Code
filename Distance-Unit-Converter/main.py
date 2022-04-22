from tkinter import *
FONT = ("Arial", 14, "normal")
MILES = "Miles"
KM = "Km"
EQUAL = "is equal to"
MILES_KM = 1.609344
CALCULATE = "Calculate"

def button_clicked():
    converted_km = round(float(txt_input.get()) * MILES_KM, 2)
    conversion_label.config(text=str(converted_km))


# Window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=10, pady=10)
#window.minsize(width=300, height=200)

# Input
txt_input = Entry(width=7)
txt_input.grid(row=0, column=1)

# Labels
miles_label = Label(text=MILES, font=FONT)
miles_label.grid(row=0, column=2)

equal_label = Label(text=EQUAL, font=FONT)
equal_label.grid(row=1, column=0)

conversion_label = Label(text='0', font=FONT)
conversion_label.grid(row=1, column=1)

km_label = Label(text=KM, font=FONT)
km_label.grid(row=1, column=2)

# Button
button = Button(text=CALCULATE, command=button_clicked)
button.grid(row=3, column=1)





window.mainloop()