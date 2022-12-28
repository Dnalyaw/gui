from tkinter import *
import time
from tkinter import messagebox

root = Tk()
root.title("Timer")
#root.iconbitmap("D:/wL/calculator-icon.ico")

startTime, endTime, running, duration_time = 0, 0, False, 0

def warning_1():
    messagebox.showinfo("Error", "You already clicked start")
def warning_2():
    messagebox.showinfo("Error", "You already clicked stop")
def warning_3():
    messagebox.showinfo("Error", "Your timer is still running")
def start_timer():
    global running
    global startTime
    if running:
        warning_1()
    else:
        running = True
        startTime = time.time()
def stop_timer():
    global running
    global duration_time
    if not running:
        warning_2()
    else:
        running = False
        endTime = time.time()
        seconds = endTime - startTime
        duration_time += seconds
def duration_timer(running, duration_time):
    global output
    if not running:
        output = Label(root, text=str(round(duration_time, 3)) + ' seconds', padx=40, pady=20, font=("Helvetica", 30))
        output.grid(row=2, column=1, stick=W + E + N + S)
    else:
        warning_3()
def reset_timer():
    global startTime, endTime, running, duration_time
    startTime, endTime, running, duration_time = 0, 0, False, 0
    output = Label(root, text='0 seconds', padx=40, pady=20, font=("Helvetica", 30))
    output.grid(row=2, column=1, stick=W + E + N + S)

#defining buttons
start = Button(root,text="START", padx=40, pady=20, font=("family", 15), command=lambda: start_timer())
stop = Button(root,text="STOP", padx=40, pady=20, font=("family", 15), command=lambda: stop_timer())
reset = Button(root,text="RESET", padx=40, pady=20, font=("family", 15), command=lambda: reset_timer())
duration = Button(root,text="FIND DURATION TIME", padx=40, pady=20, font=("family", 15), command=lambda: duration_timer(running, duration_time))

#put buttons on screen
start.grid(row=3, column=0)
stop.grid(row=3, column=1)
reset.grid(row=3, column=3)
duration.grid(row=3, column=2)


root.mainloop()