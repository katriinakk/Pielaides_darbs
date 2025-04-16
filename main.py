import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk
import requests
import random
import string




class Parole_logs:
    def __init__(self, master):
        self.master = master
        self.master.title("Paroles ģenerātors")
        self.master.geometry("330x500")
        self.master.configure(bg= "azure")


    def leibeli(self):
        self.label = Label(text = "Paroļu ģenerātors", font=('Bookman Old Style', 12, 'bold'), bg = "LightBlue1")
        self.label.grid(row = 1, column = 2, padx = 10, pady = 20)

        self.label1 = Label(text = "Ievadiet vārdu, kuru vēlaties pielāgot parolei:", font=('Bookman Old Style', 10, 'normal'), bg = "azure")
        self.label1.grid(row = 2, column = 2, padx = 10, pady = 8)

        self.autputss = Label(text ='', fg= "OrangeRed2", font=('Bookman Old Style', 10, 'bold'))
        self.papildu = Label(text= '', font=('Bookman Old Style', 10, 'normal'))
        # self.teksts = Text(self.master, height = 5, width = 20)
        self.autputss.grid(row=5, column = 2, padx = 10, pady = 5)

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
                self.autputss['text'] = "Nevar saņemt datus no API, lūdzu ievadiet vārdu manuāli"
                # erors = "Nevar saņemt datus no API, lūdzu ievadiet vārdu manuāli"
                # self.text = erors
                # Parole_logs.autputs(self)

        else:
            self.parole = self.entry.get()
            print(self.parole)

    def sifrejums(self):
        self.sifrs = {'a': '4','b': '6', 'c': '<', 'd': '.1', 'e': '3', 'f': 'i=', 'g': '8', 'h': 'iu', 'i': '1', 'j': ')', 'k': ')<', 'l': '[', 'm': 'nn', 'n': 'h', 'o': '0', 'p': '>',  'q': '9', 'r': ']*', 's': '5',  't': '7', 'u': 'v', 'v': '^', 'w': '^^', 'x': '//', 'y': '/', 'z': '2'}
        self.niu_pasvord = ""

        for lett in self.parole:
            x = random.randint(1,3)
            if x == 1:
                lett = self.sifrs[lett]
            if x == 2:
                lett = lett.upper()

            self.niu_pasvord = self.niu_pasvord+lett

        print(self.niu_pasvord)

    def parbaude(self):

        if not 10 < len(self.niu_pasvord):
            x = 10-len(self.niu_pasvord)
            for i in range(x):
                self.niu_pasvord = self.niu_pasvord + random.choice(list(self.sifrs.keys()))
        if len(self.niu_pasvord) > 16:
                x = len(self.niu_pasvord) - 16
                self.niu_pasvord = self.niu_pasvord[:-x] 

        t = 0
        y = 0
        p = 0
        for lett in self.niu_pasvord:
            if lett.isupper() == True:
                p +=1
        if p == 0:
            self.niu_pasvord = self.niu_pasvord+ random.choice(list(self.sifrs.keys())).upper()

        for lett in self.niu_pasvord:
            if lett.isalnum() == False:
                t +=1
        if t == 0:       
                self.niu_pasvord = self.niu_pasvord + random.choice(string.punctuation)

        for lett in self.niu_pasvord:
            if lett.isdigit() == True:
                y +=1

        if y == 0:
            self.niu_pasvord = self.niu_pasvord + str(random.randrange(10))

        self.autputss['text'] = self.niu_pasvord
        tekstins = ' no vārda "'+ self.parole+'"'
        self.papildu['text'] = tekstins
        self.papildu.grid(row=6, column = 2)
        
        print(self.niu_pasvord)

    def buttons(self):
        self.button = Button(text = "Ģenerēt paroli", font=('Bookman Old Style', 10, 'normal'), bg = "LightBlue1")
        self.button.grid(row=4, column = 2, padx = 10, pady = 8)
        self.button.configure(command=lambda: [Parole_logs.ievade(self), Parole_logs.sifrejums(self), Parole_logs.parbaude(self)]) #[Person.getting_values(self), Person.maths(self), Person.outputs(self)]

    def imidzs(self):
        self.image = Image.open("keyboard.jpg")
        self.image = self.image.resize((200, 150))
        self.image2 = ImageTk.PhotoImage(self.image)
        self.labelss = tk.Label(self.master, image=self.image2)
        self.labelss.grid(row=7, column= 2, padx =10, pady=10)

logs = Tk()
a = Parole_logs(logs)
a.leibeli()
a.entriji()
a.buttons()
a.imidzs()


logs.mainloop()