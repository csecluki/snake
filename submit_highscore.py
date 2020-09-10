from tkinter import *
import datetime


class SubmitHighscore(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.geometry("420x140")
        self.title("New highscore!")
        self.font = ("calibri", 13)
        self.nick = "Player1"
        self.length = 0

        self.frame_up = Frame(self)
        self.ask = Label(self.frame_up, text="Enter your name", font=self.font)
        self.ask.grid(row=0, column=0, padx=10)
        self.player_name = Entry(self.frame_up, font=self.font)
        self.player_name.grid(row=0, column=1, padx=10)
        self.frame_up.pack(side=TOP, pady=20)

        self.frame_down = Frame(self)
        self.cancel_button = Button(self.frame_down, text="Cancel", command=self.cancel).grid(row=0, column=0, padx=20)
        self.submit_button = Button(self.frame_down, text="Submit", command=self.submit).grid(row=0, column=1, padx=20)
        self.frame_down.pack(side=BOTTOM, pady=20)

    def set_length(self, length):
        self.length = length

    def show(self):
        self.mainloop()

    def submit(self):
        self.nick = self.player_name.get()
        self.destroy()
        self.save()

    def cancel(self):
        self.destroy()
        self.save()

    def save(self):
        with open("highscores.csv", "a") as file:
            file.write(f"{self.length};{datetime.date.today()};{self.nick}\n")
