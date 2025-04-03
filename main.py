import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk

class Parole:
    def __init__(self, master):
        self.master = master
        self.master.title("Paroles ģenerātors")
        self.master.geometry("330x430")
        self.master.configure(bg= "azure")
        self.parole = ""

    def leibeli(self):
        self.label = Label(text = "Paroļu ģenerātors", font=('Bookman Old Style', 12, 'bold'), bg = "LightBlue1")
        self.label.grid(row = 1, column = 2, padx = 10, pady = 20)

        self.label1 = Label(text = "Ievadiet vārdu, kuru vēlaties pielāgot parolei:", font=('Bookman Old Style', 10, 'normal'), bg = "azure")
        self.label1.grid(row = 2, column = 2, padx = 10, pady = 8)

        self.teksts = Text(self.master, height = 1, width = 20)
        self.teksts.grid(row=5, column = 2, padx = 10, pady = 25)

    def entriji(self):
        self.entry = Entry(width = 25)
        self.entry.grid(row = 3, column = 2, padx = 10, pady = 8)

    def autputs(self):
        self.text = self.entry.get()
        self.teksts.insert(tk.END, self.text)

    def buttons(self):
        self.button = Button(text = "Ģenerēt paroli", font=('Bookman Old Style', 10, 'normal'), bg = "LightBlue1")
        self.button.grid(row=4, column = 2, padx = 10, pady = 8)
        #self.button.configure(command=lambda: [Person.getting_values(self), Person.maths(self), Person.outputs(self)])

    def imidzs(self):
        self.image = Image.open("keyboard.jpg")
        self.image = self.image.resize((200, 150))
        self.image2 = ImageTk.PhotoImage(self.image)
        self.labelss = tk.Label(self.master, image=self.image2)
        self.labelss.grid(row=6, column= 2, padx =10, pady=10)

logs = Tk()
a = Parole(logs)
a.leibeli()
a.entriji()
a.buttons()
a.imidzs()


logs.mainloop()