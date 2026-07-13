from tkinter import *

root = Tk()

root.title("Welcome to Habr")

root.geometry('350x200')

# метка
lbl = Label(root, text = "Are you a Geek?")
lbl.grid()

# поле ввода
txt = Entry(root, width=10)
txt.grid(column =1, row =0)

def clicked():

    res = "You wrote" + txt.get()
    lbl.configure(text = res)

btn = Button(root, text = "Click me" ,

             fg = "red", command=clicked)

# меняем расположение

btn.grid(column=2, row=0)

root.mainloop() 