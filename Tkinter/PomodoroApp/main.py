from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    checkmark_label.config(text="")
    canvas.itemconfig(timer_text,text="00:00")
    timer_heading_label.config(text="Work")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = int(WORK_MIN * 60)
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_heading_label.config(text="Long Break",fg=RED)
        return
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_heading_label.config(text="Short Break",fg=PINK)
        return
    else:
        count_down(work_sec)
        timer_heading_label.config(text="Work Time",fg=GREEN)
        return
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    final_text = f"{count_min}:{str(count_sec).zfill(2)}"

    canvas.itemconfig(timer_text, text=str(final_text))
    if(count > 0):
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""

        for _ in range(math.floor(reps/2)):
            marks += "✔"
        checkmark_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title = "Pomodoro"
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, highlightthickness=0, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.grid(row=1, column=1)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")

timer_heading_label = Label(text="Timer", fg=GREEN,bg=YELLOW,font=(FONT_NAME,50,"bold"))
timer_heading_label.grid(row=0, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 8, "bold"),command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 8, "bold"),command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark_label = Label(text="", fg=GREEN,bg=YELLOW)
checkmark_label.grid(row=3, column=1)

window.mainloop()