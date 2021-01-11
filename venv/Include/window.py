from tkinter import *
from classes import *
from random import *

root = Tk()
root.title("blackjack")
root.config(bg = "black")
root.geometry("500x600")


def exit():
    root.destroy()


first =str(randint(1,13))

def but1():
    exit()

    root2 = Tk()
    root2.title("1 player")
    root2.config(bg = "black")
    root2.geometry("500x600")

    frame = LabelFrame(root2, padx = 30, pady = 30, bg = "grey")
    frame.grid(row = 0, column = 0)
    frame2 = LabelFrame(root2, padx=30, pady=30, bg="grey")
    frame2.grid(row = 0, column = 1)

    new_card = Button(frame, text="NEW CARD", command=but1, bg="green", padx = 50)
    new_card.grid()
    stop_card = Button(frame2, text = "I don't want other" ,command =but1, bg = "red", padx = 50)
    stop_card.grid()

    my_number = Label(root2, text = "my number is " + first, fg = "green", bg =  "black")
    my_number.grid(column = 0, row = 1,)

    root2.mainloop()


def but2():
    root3 = Tk()


    root3.mainloop()

def but3():
    root4 = Tk()


    root4.mainloop()
labelj= Label(root, text = "how many players?", fg = "dark green", bg = "black")
j1 = Button(root, text="1 player ", command = but1, padx = 2, bg = "green")
j2 = Button(root, text="2 players", command = but1, bg = "green")
j3 = Button(root, text="3 players", command = but1, bg = "green")




# poner los botones en pantalla

labelj.grid(row = 0, column = 1)
j1.grid(row = 1, column = 0)
j2.grid(row = 1, column = 1)
j3.grid(row = 1, column = 2)

root.mainloop()
