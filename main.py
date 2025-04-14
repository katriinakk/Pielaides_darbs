import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk
import requests
import random




class Parole_logs:
    def __init__(self, master, parole):
        self.master = master
        self.master.title("Paroles ģenerātors")
        self.master.geometry("330x500")
        self.master.configure(bg= "azure")
        self.parole = parole

    def leibeli(self):
        self.label = Label(text = "Paroļu ģenerātors", font=('Bookman Old Style', 12, 'bold'), bg = "LightBlue1")
        self.label.grid(row = 1, column = 2, padx = 10, pady = 20)

        self.label1 = Label(text = "Ievadiet vārdu, kuru vēlaties pielāgot parolei:", font=('Bookman Old Style', 10, 'normal'), bg = "azure")
        self.label1.grid(row = 2, column = 2, padx = 10, pady = 8)

        self.teksts = Text(self.master, height = 5, width = 20)
        self.teksts.grid(row=5, column = 2, padx = 10, pady = 25)

    def autputs(self):
        self.teksts.insert(tk.END, self.text)

    def entriji(self):
        self.entry = Entry(width = 25)
        self.entry.grid(row = 3, column = 2, padx = 10, pady = 8)

    def ievade(self):
        if not self.entry.get():
            #API
            try:
                url = "https://random-word-api.herokuapp.com/word"
                response = requests.get(url)
                words = response.json()
                self.parole = random.choice(words)
                print(self.parole)
            except:
                erors = "Nevar saņemt datus no API, lūdzu ievadiet vārdu manuāli"
                self.text = erors
                Parole_logs.autputs(self)

        else:
            self.parole = self.entry.get()
            print(self.parole)

    def sifrejums(self):
        sifrs = {'a': '4','b': '6', 'c': '<', 'd': '.1', 'e': '3', 'f': 'i=', 'g': '8', 'h': 'iu', 'i': '1', 'j': ')', 'k': ')<', 'l': '[', 'm': 'nn', 'n': 'h', 'o': '0', 'p': '>',  'q': '9', 'r': ']*', 's': '5',  't': '7', 'u': 'v', 'v': '^', 'w': '^^', 'x': '//', 'y': '/', 'z': '2'}

    def buttons(self):
        self.button = Button(text = "Ģenerēt paroli", font=('Bookman Old Style', 10, 'normal'), bg = "LightBlue1")
        self.button.grid(row=4, column = 2, padx = 10, pady = 8)
        self.button.configure(command=lambda: Parole_logs.ievade(self)) #[Person.getting_values(self), Person.maths(self), Person.outputs(self)]

    def imidzs(self):
        self.image = Image.open("keyboard.jpg")
        self.image = self.image.resize((200, 150))
        self.image2 = ImageTk.PhotoImage(self.image)
        self.labelss = tk.Label(self.master, image=self.image2)
        self.labelss.grid(row=6, column= 2, padx =10, pady=10)

logs = Tk()
a = Parole_logs(logs, 1)
a.leibeli()
a.entriji()
a.buttons()
a.imidzs()


logs.mainloop()