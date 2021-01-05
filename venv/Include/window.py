from tkinter import *
from classes import *

root = Tk()


def but1():
    labelb1 = Label(root, text="hello world")
    labelb1.grid()

def but2():
    return

def but3():
    return

j1 = Button(root, text="1 player", command = but1)
j2 = Button(root, text="2 players", command = but1)
j3 = Button(root, text="3 players", command = but1)


# poner los botones en pantalla

j1.grid()
j2.grid()
j3.grid()

root.mainloop()
