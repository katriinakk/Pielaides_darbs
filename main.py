import tkinter as tk
from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import random
import string




class Parole_logs:
    def __init__(self, master):
        self.master = master
        self.master.title("Paroles ģenerātors")
        self.master.geometry("400x500")
        self.master.configure(bg= "azure")


    def leibeli(self):
        # teksti
        self.label = Label(text = "Paroļu ģenerātors", font=('Bookman Old Style', 12, 'bold'), bg = "LightBlue1")
        self.label.grid(row = 1, column = 2, padx = 125, pady = 20)

        self.label1 = Label(text = "Ievadiet vārdu, kuru vēlaties pielāgot parolei:", font=('Bookman Old Style', 10, 'normal'), bg = "azure")
        self.label1.grid(row = 2, column = 2, padx = 20, pady = 8)

        self.autputss = Label(text ='', fg= "OrangeRed2", font=('Bookman Old Style', 10, 'bold'), bg = "azure")
        self.papildu = Label(text= '', font=('Bookman Old Style', 10, 'normal'), bg = "azure")
        self.papildu.grid(row=6, column = 2)
        self.autputss.grid(row=5, column = 2, padx = 20, pady = 5)

    def entriji(self):
        # ievades logs
        self.entry = Entry(width = 25)
        self.entry.grid(row = 3, column = 2, padx = 20, pady = 8)

    def ievade(self): # funkcija, kura pārbauda, vai ievadē ir ievadīa vērtība un tiek definēts paroles vārds
        if not self.entry.get():
            # API
            try:
                url = "https://random-word-api.herokuapp.com/word"
                response = requests.get(url)
                words = response.json()
                self.parole = random.choice(words)
                print(self.parole)
            except:
                self.autputss['text'] = "Nevar saņemt datus no API,"
                self.papildu['text'] = "lūdzu ievadiet vārdu manuāli"

        else:
            self.parole = self.entry.get()
            print(self.parole)
            if self.parole.isalpha() == False:
                self.autputss['text'] = "Nepareizi ievadīts vārds"
                self.papildu['text'] = "Pārliecinieties, ka vārds satur tikai latīņu alfabēta burtus"
                

    def sifrejums(self): # funkcija, kura šifrē vārdu
        # tiek izveidota vārdnīca, pēc kuras tiek šifrēti burti:
        self.sifrs = {'a': '4','b': '6', 'c': '<', 'd': '.1', 'e': '3', 'f': 'i=', 'g': '8', 'h': 'iu', 'i': '1', 'j': ')', 'k': ')<', 'l': '[', 'm': 'nn', 'n': 'h', 'o': '0', 'p': '>',  'q': '9', 'r': ']*', 's': '5',  't': '7', 'u': 'v', 'v': '^', 'w': '^^', 'x': '//', 'y': '/', 'z': '2'}
        self.niu_pasvord = ""

        #cikls, kurš iet cauri katram burtam (33% tas tiks šifrēts, 33% - mainīts uz lielo burtu, 33% - nemainīts)
        for lett in self.parole:
            x = random.randint(1,3)
            if x == 1:
                lett = self.sifrs[lett]
            if x == 2:
                lett = lett.upper()

            self.niu_pasvord = self.niu_pasvord+lett

        print(self.niu_pasvord)

    def parbaude(self): # funkcija pārbauda, vai parole atbilst kritērijiem

        #vai parole ir diapazona no 10 līdz 16, ja nē, tad to labo
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
        #vai parolē ir vismaz viens lielais burts?
        for lett in self.niu_pasvord:
            if lett.isupper() == True:
                p +=1
        if p == 0:
            self.niu_pasvord = self.niu_pasvord+ random.choice(list(self.sifrs.keys())).upper()

        #vai parolē ir vismaz viena speciāla rakstzīme?
        for lett in self.niu_pasvord:
            if lett.isalnum() == False:
                t +=1
        if t == 0:       
                self.niu_pasvord = self.niu_pasvord + random.choice(string.punctuation)

        #vai parolē ir vismaz viens cipars?s
        for lett in self.niu_pasvord:
            if lett.isdigit() == True:
                y +=1
        if y == 0:
            self.niu_pasvord = self.niu_pasvord + str(random.randrange(10))


        # izvada paroli uz grafiskās saskarnes
        if self.parole.isalpha() == True:
            self.autputss['text'] = self.niu_pasvord
            tekstins = ' no vārda "'+ self.parole+'"'
            self.papildu['text'] = tekstins
        
        
        print(self.niu_pasvord)

    

    def imidzs(self):
        self.image = Image.open("keyboard.jpg")
        self.image = self.image.resize((200, 150))
        self.image2 = ImageTk.PhotoImage(self.image)
        self.labelss = tk.Label(self.master, image=self.image2)
        self.labelss.grid(row=7, column= 2, padx =20, pady=10)

    

    def buttons(self): # poga, kura palaiž visas funkcijas
        self.button = Button(text = "Ģenerēt paroli", font=('Bookman Old Style', 10, 'normal'), bg = "LightBlue1")
        self.button.grid(row=4, column = 2, padx = 20, pady = 8)
        self.button.configure(command=lambda: [Parole_logs.ievade(self), Parole_logs.sifrejums(self), Parole_logs.parbaude(self)])

        self.imagei = Image.open("info.png")
        self.imagei = self.imagei.resize((50, 50))
        self.image2i = ImageTk.PhotoImage(self.imagei)
        self.butonsi = Button(self.master, text = 'te', image = self.image2i, command =lambda: self.vindovs())
        self.butonsi.grid(row = 8, column = 2, padx =20, pady=10)

    def vindovs(self):
        messagebox.showinfo("Informācija",  "Sveicināti paroļu ģeneratorā !!!\nAr šo aplikācijas palīdzību, Jūs varēsiet bez grūtībām ģenerēt paroles.\n\
Ja Jūs vēlaties parolē iekļaut vārdu pēc savas izvēles, tad to ievadiet ievades lauciņā. Ja Jūs vēlaties, lai aplikācija ģenerē nejaušu paroli\
tad atstājiet lauciņu tukšu, un kods ņems nejaušus vārdus no angļu valodas vārdnīcas\n Lauciņā nedrīkst vadīt speciālas rakstzīmes, mīkstinājuma zīmes \
un garumzīmes !!!") 




logs = Tk()
a = Parole_logs(logs)
a.leibeli()
a.entriji()
a.imidzs()
a.buttons()


logs.mainloop()