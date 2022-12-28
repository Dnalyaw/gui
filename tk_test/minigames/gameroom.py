from tkinter import *

main = Tk()
main.title("Gameroom")
#main.geometry("360x360")
main.configure(bg="Orange")



def open1():
    from gui_test.tk_test.minigames.game_test import root
    root.mainloop()
def open2():
    from gui_test.tk_test.minigames.tictactoegame import root
    root.mainloop()
def open3():
    from gui_test.tk_test.minigames.tictactoecomputer import root
    root.mainloop()

lbl = Label(main, text="Pick a game, any game!", font=("Helvectica", 20), bg="Orange")
btn1 = Button(main, text="Open Guessing Game", font=("Helvectica", 15), command=open1)
btn2 = Button(main, text="Tic-Tac-Toe Two Player", font=("Helvectica", 15), command=open2)
btn3 = Button(main, text="Tic-Tac-Toe vs. Computer", font=("Helvectica", 15), command=open3)

lbl.grid(row=0, column=0, columnspan=2)
btn1.grid(row=1, column=0, stick=W+E+N+S)
btn2.grid(row=1, column=1, stick=W+E+N+S)
btn3.grid(row=2, column=0, stick=W+E+N+S)

main.mainloop()