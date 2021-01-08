from tkinter import *
from classes import *

root = Tk()
root.title("blackjack")
root.config(bg = "black")

def but1():
    root2 = Tk()
    new_card = Button(root2, text="NEW CARD", command=but1, bg="green")
    new_card.grid()

    root2.mainloop()


def but2():
    return

def but3():
    return

labelj= Label(root, text = "how many players?", fg = "dark green")
j1 = Button(root, text="1 player ", command = but1, padx = 2, bg = "green")
j2 = Button(root, text="2 players", command = but1, bg = "green")
j3 = Button(root, text="3 players", command = but1, bg = "green")




# poner los botones en pantalla

labelj.grid(row = 0, column = 1)
j1.grid(row = 1, column = 0)
j2.grid(row = 1, column = 1)
j3.grid(row = 1, column = 2)

root.mainloop()
