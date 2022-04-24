from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
FONT_SETTINGS = (FONT_NAME, 32, "bold")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

window_title = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
window_title.grid(row=0, column=1)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
canvas.create_text(103, 130, text="00:00", fill="white", font=FONT_SETTINGS)
canvas.grid(row=1, column=1)

start_btn = Button(text="Start", highlightthickness=0, bg=YELLOW)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Stop", highlightthickness=0, bg=YELLOW)
reset_btn.grid(row=2, column=2)

check_marks = Label(text="✓", highlightthickness=0, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30))
check_marks.grid(row=3, column=1)


window.mainloop()
