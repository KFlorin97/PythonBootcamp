from tkinter import *
import time
import math


# ----------------------- ADD Sounds --------------------------------- #
import winsound
frequency = 2500
duration = 1000     #1 second

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    title_label.config(text = "Timer")
    check_marks.config(text = "")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    workSeconds = WORK_MIN * 60
    shortBreakSeconds = SHORT_BREAK_MIN * 60
    longBreakSeconds = LONG_BREAK_MIN * 60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        winsound.Beep(frequency,duration)
        count_down(workSeconds)
        title_label.config(text="Work", fg=GREEN)
    elif reps == 2 or reps == 4 or reps == 6:
        winsound.Beep(frequency,duration)
        count_down(shortBreakSeconds)
        title_label.config(text="Short Break", fg=PINK)
    elif reps == 8:
        winsound.Beep(frequency,duration)
        count_down(longBreakSeconds)
        title_label.config(text="Break", fg = RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10 :
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text="{0}:{1}".format(minutes,seconds))
    if count > 0 :
        global timer
        timer = window.after(1000, count_down, count -1 )
    else:
        start_timer()
        marks = ""
        for i in range(math.floor(reps/2)):
            marks += "X"
        check_marks.config(text = marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg=YELLOW,)

title_label = Label(text = "Timer", fg = GREEN, bg = YELLOW,font = (FONT_NAME, 35, "bold"))
title_label.grid(column = 1, row = 0)


canvas = Canvas(width = 200, height = 224, bg = GREEN)
tomato_img  = PhotoImage(file = "tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row = 1)

start_button = Button(text="Start", highlightthickness = 0, command = start_timer)
start_button.grid(column = 0, row = 2)


reset_button = Button(text="Reset", highlightthickness = 0, command = reset_timer)
reset_button.grid(column = 2, row = 2)

check_marks = Label(fg=GREEN, bg=YELLOW, font = (FONT_NAME, 30, "bold"))
check_marks.grid(column = 1, row = 3)


window.mainloop()