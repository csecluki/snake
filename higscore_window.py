from tkinter import *
import csv


class HighscoreWindow(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.geometry("380x200")
        self.title("Highscores")

        self.lp_frame = Frame(self)
        self.score_frame = Frame(self)
        self.date_frame = Frame(self)
        self.player_frame = Frame(self)

        self.lp_frame.grid(row=0, column=0, padx=5, pady=10)
        self.score_frame.grid(row=0, column=1, padx=5, pady=10)
        self.date_frame.grid(row=0, column=2, padx=5, pady=10)
        self.player_frame.grid(row=0, column=3, padx=5, pady=10)

        self.lp = Label(self.lp_frame, text="Lp", font=("Calibri", 14))\
            .grid(row=0, column=0, padx=10, pady=10)
        self.score = Label(self.score_frame, text="SCORE", font=("Calibri", 14))\
            .grid(row=0, column=0, padx=10, pady=10)
        self.date = Label(self.date_frame, text="DATE", font=("Calibri", 14))\
            .grid(row=0, column=0, padx=25, pady=10)
        self.player = Label(self.player_frame, text="PLAYER", font=("Calibri", 14))\
            .grid(row=0, column=0, padx=20, pady=10)

    def load_data(self):
        with open("highscores.csv", "r") as file:
            reader = csv.reader(file, delimiter=";")
            table = sorted(reader, key=lambda elem: int(elem[0]), reverse=True)
            for i in range(5):
                number = Label(self.lp_frame, text=f"{i + 1}", font=("Calibri", 12)) \
                    .grid(row=i + 1, column=0)
                points = Label(self.score_frame, text=f"{table[i][0]}", font=("Calibri", 12)) \
                    .grid(row=i + 1, column=0)
                day = Label(self.date_frame, text=f"{table[i][1]}", font=("Calibri", 12)) \
                    .grid(row=i + 1, column=0)
                name = Label(self.player_frame, text=f"{table[i][2]}", font=("Calibri", 12)) \
                    .grid(row=i + 1, column=0)

    def show(self):
        self.mainloop()
