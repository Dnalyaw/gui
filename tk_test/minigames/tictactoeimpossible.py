from tkinter import *
from tkinter import messagebox
import math
import random

root = Tk()
root.title("Tic-Tac-Toe vs Computer")


#x starts so true
clicked = True
count = 0


b1 = Button(root, text=" ", font=("Helvectica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Helvectica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Helvectica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b3))

b4 = Button(root, text=" ", font=("Helvectica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Helvectica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Helvectica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b6))

b7 = Button(root, text=" ", font=("Helvectica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b7))
b8 = Button(root, text=" ", font=("Helvectica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Helvectica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b9))

#disables all buttons
def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


#Check to see if someone won
def checkifwon():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="yellow")
        b2.config(bg="yellow")
        b3.config(bg="yellow")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X won!")
        disable_all_buttons()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="yellow")
        b5.config(bg="yellow")
        b6.config(bg="yellow")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X won!")
        disable_all_buttons()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="yellow")
        b8.config(bg="yellow")
        b9.config(bg="yellow")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X won!")
        disable_all_buttons()
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="yellow")
        b4.config(bg="yellow")
        b7.config(bg="yellow")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X won!")
        disable_all_buttons()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="yellow")
        b5.config(bg="yellow")
        b8.config(bg="yellow")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X won!")
        disable_all_buttons()
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="yellow")
        b6.config(bg="yellow")
        b9.config(bg="yellow")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X won!")
        disable_all_buttons()
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="yellow")
        b5.config(bg="yellow")
        b9.config(bg="yellow")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X won!")
        disable_all_buttons()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="yellow")
        b5.config(bg="yellow")
        b7.config(bg="yellow")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X won!")
        disable_all_buttons()
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="yellow")
        b2.config(bg="yellow")
        b3.config(bg="yellow")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Good Game! O won!")
        disable_all_buttons()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="yellow")
        b5.config(bg="yellow")
        b6.config(bg="yellow")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Good Game! O won!")
        disable_all_buttons()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="yellow")
        b8.config(bg="yellow")
        b9.config(bg="yellow")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Good Game! O won!")
        disable_all_buttons()
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="yellow")
        b4.config(bg="yellow")
        b7.config(bg="yellow")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Good Game! O won!")
        disable_all_buttons()
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="yellow")
        b5.config(bg="yellow")
        b8.config(bg="yellow")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Good Game! O won!")
        disable_all_buttons()
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="yellow")
        b6.config(bg="yellow")
        b9.config(bg="yellow")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Good Game! O won!")
        disable_all_buttons()
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="yellow")
        b5.config(bg="yellow")
        b9.config(bg="yellow")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Good Game! O won!")
        disable_all_buttons()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="yellow")
        b5.config(bg="yellow")
        b7.config(bg="yellow")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Good Game, O won!")
        disable_all_buttons()

    if count == 9 and winner == False:
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        disable_all_buttons()


# reset game
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0

    # Build our buttons
    b1 = Button(root, text=" ", font=("Helvectica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvectica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvectica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b3))

    b4 = Button(root, text=" ", font=("Helvectica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helvectica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvectica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b6))

    b7 = Button(root, text=" ", font=("Helvectica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvectica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helvectica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b9))

    #place buttons onto screen
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

#Check to see who won
def checkwhowon():
    if b1["text"] == b2["text"] and b2["text"] == b3["text"]:
        mark = b1["text"]
        return mark
    elif b4["text"] == b5["text"] and b5["text"] == b6["text"]:
        mark = b4["text"]
        return mark
    elif b7["text"] == b8["text"] and b8["text"] == b9["text"]:
        mark = b7["text"]
        return mark
    elif b1["text"] == b4["text"] and b4["text"] == b7["text"]:
        mark = b4["text"]
        return mark
    elif b2["text"] == b5["text"] and b5["text"] == b8["text"]:
        mark = b2["text"]
        return mark
    elif b3["text"] == b6["text"] and b6["text"] == b9["text"]:
        mark = b3["text"]
        return mark
    elif b1["text"] == b5["text"] and b5["text"] == b9["text"]:
        mark = b1["text"]
        return mark
    elif b3["text"] == b5["text"] and b5["text"] == b7["text"]:
        mark = b3["text"]
        return mark
    else:
        return ' '

empty_squares = []
def best_move(game):
    computer = 'O'
    if len(empty_squares) == 9:
        square = random.choice(game.empty_squares)
    else:
        square = minimax(game, computer)["position"]
    return square

def minimax(state, player):
    global winner
    max_player = 'O'
    other_player = 'O' if player == 'X' else 'X'
    current_winner = checkwhowon()
    if current_winner == other_player:
        return{'position': None,
                    'score': 1 * (state.empty_squares + 1) if other_player == max_player else -1 * (state.empty_squares + 1)
                    }
    elif len(state.empty_squares) == 0:
        return{'position': None, 'score':0}
    if player == max_player:
        best = {'position':None, 'score': -math.inf}
    else:
        best = {'position': None, 'score': math.inf}

    for possible_move in state.empty_squares:
        state.make_move(possible_move, player)

        sim_score = minimax(state, other_player)

        possible_move["text"] = ' '
        winner = False
        sim_score["position"] = possible_move

        if player == max_player:
            if sim_score["score"] > best['score']:
                best = sim_score
        else:
            if sim_score['score'] < best['score']:
                best = sim_score
    return best


#Button clicked function
def b_click(b):
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    #parameter is the button, and ["text"] can get and change the text
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkifwon()
    elif b["text"] != " " and clicked == True:
        messagebox.showerror("Tic Tac Toe", "That box has already been selected")

    if winner == False and clicked == False:
        if b1["text"] == " ":
            empty_squares.append(b1)
        if b2["text"] == " ":
            empty_squares.append(b2)
        if b3["text"] == " ":
            empty_squares.append(b3)
        if b4["text"] == " ":
            empty_squares.append(b4)
        if b5["text"] == " ":
            empty_squares.append(b5)
        if b6["text"] == " ":
            empty_squares.append(b6)
        if b7["text"] == " ":
            empty_squares.append(b7)
        if b8["text"] == " ":
            empty_squares.append(b8)
        if b9["text"] == " ":
            empty_squares.append(b9)
    if winner == False or len(empty_squares) != 0:
        best_move()
        empty_squares.clear()
        clicked = True
        count += 1
        checkifwon()

#menu
my_menu = Menu(root)
root.config(menu=my_menu)

#options menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)



reset()

root.mainloop()