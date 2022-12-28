#api_testing
from tkinter import *
import mlbgame
import datetime
import requests
import json

root = Tk()
root.title("Do they have a game today?")

teams = [
    "Angels",
    "Astros",
    "Athletics",
    "Blue Jays",
    "Braves",
    "Brewers",
    "Cardinals",
    "Cubs",
    "Diamondbacks",
    "Dodgers",
    "Giants",
    "Indians",
    "Mariners",
    "Marlins",
    "Mets",
    "Nationals",
    "Orioles",
    "Padres",
    "Phillies",
    "Pirates",
    "Rangers",
    "Rays",
    "Red Sox",
    "Reds",
    "Rockies",
    "Royals",
    "Tigers",
    "Twins",
    "White Sox",
    "Yankees"
]


clicked = StringVar()
clicked.set(teams[0])

def find():
    now = datetime.datetime.today()
    day = mlbgame.games(now.year, now.month, now.day, home=clicked.get(), away=clicked.get())
    games = mlbgame.combine_games(day)
    if len(games) > 0:
        for game in games:
            game_label = Label(root, text="Game: " + str(game), font=("Helvetica", 20))
            game_label.grid(row=2, column=0, columnspan=2, stick=W+E+N+S)
    else:
        game_label = Label(root, text="Sorry, this team is not playing today", font=("Helvetica", 20))
        game_label.grid(row=2, column=0, columnspan=2, stick=W + E + N + S)



question = Label(root, text="Whose baseball team do you want to check?", font=("Helvetica", 15))
question.grid(row=0, column=0, stick=W+E+N+S)
teamInput = OptionMenu(root, clicked, *teams)
teamInput.grid(row=1, column=0, stick=W+E+N+S)
teamButton = Button(root, text="Lookup Team", font=("Helvetica", 15), command=find)
teamButton.grid(row=1, column=1, stick=W+E+N+S)


root.mainloop()