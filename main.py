import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✓"
timer = None

reps = 0

# ---------------------------- TIMER RESET ------------------------------- #
def reset_clock():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_clock():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_brake_sec = SHORT_BREAK_MIN * 60
    long_brake_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="WORK :(", font=(FONT_NAME, 24, "bold"),
                           bg=YELLOW,
                           fg=PINK)
    elif reps % 8 == 0:
        count_down(long_brake_sec)
        timer_label.config(text="BREAK :)", font=(FONT_NAME, 24, "bold"),
                           bg=YELLOW,
                           fg=GREEN)
    else:
        count_down(short_brake_sec)
        timer_label.config(text="BREAK :)", font=(FONT_NAME, 24, "bold"),
                           bg=YELLOW,
                           fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    global checkmark_label

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_clock()
        if reps % 2 == 0:
            mark = ""
            for _ in range(0, math.floor(reps/2)):
                mark += CHECKMARK
                checkmark_label.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(101, 130, text="00:00", fill="white",
                           font=(FONT_NAME, 24,
                                                               "bold"))
canvas.grid(row=1, column=1)


timer_label = tkinter.Label()
timer_label.config(text="Timer", font=(FONT_NAME, 24, "bold"), bg=YELLOW,
                   fg=GREEN)
timer_label.grid(row=0, column=1)

start_button = tkinter.Button(text="Start", command=start_clock, font=FONT_NAME)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", command=reset_clock, font=FONT_NAME)
reset_button.grid(row=2, column=2)

checkmark_label = tkinter.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME,
                                                                   24,
                                                               "bold"))
checkmark_label.grid(row=3, column=1)

window.mainloop()