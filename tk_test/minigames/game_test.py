from tkinter import *
import random
root = Tk()
root.geometry("360x360")
root.title("Guessing game")

used_numbers = []
def user_guess(): #x is the highest number the computer can pick
    current = int(guessing.get())
    used_numbers.append(current)
    if current == random_number:
        turns = len(used_numbers)
        label_2 = Label(root, text=f"You guessed the number, {random_number}, in {turns} tries!")
        label_2.grid(row=3, column=0)
        guessing.delete(0, END)
        return
    elif current > random_number:
        label_2 = Label(root, text="Too high, try again")
        label_2.grid(row=3, column=0)
        guessing.delete(0, END)
    elif current < random_number:
        label_2 = Label(root, text="Too low, try again")
        label_2.grid(row=3, column=0)
        guessing.delete(0, END)
    else:
        used_numbers.remove(-1)
        label_2 = Label(root, text="That is invalid, try again")
        label_2.grid(row=3, column=0)
        guessing.delete(0, END)

label_2 = Label(root)

def reset():
    global random_number
    global label_2
    label_2.destroy()
    used_numbers.clear()
    label_2 = Label(root, text="                                 Game Reset!                               ")
    label_2.grid(row=3, column=0)
    random_number = random.randint(1, 101)



#defining stuff
label = Label(root, text="I'm thinking of a number between 1 and 100, try and guess it!")
guessing = Entry(root, width=50)
myButton = Button(root, text="Confirm as guess", command=user_guess)
reset_button = Button(root, text="Reset", command=reset)

#putting stuff on screen
label.grid(row=0, column=0, padx=15)
guessing.grid(row=1, column=0)
myButton.grid(row=2, column=0)
reset_button.grid(row=10, column=0, pady=240)

random_number = random.randint(1, 101)

#root.mainloop()