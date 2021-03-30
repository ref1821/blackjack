from tkinter import *
from classes import *
from random import *

root = Tk()
root.title("blackjack")
root.config(bg = "black")
root.geometry("500x600")


def exit():
    root.destroy()




def but1():
    exit()

    root2 = Tk()
    root2.title("1 player")
    root2.config(bg = "black")
    root2.geometry("500x600")

    first = randint(1, 13)
    second = randint(1, 13)
    global final
    final = first + second


    def another_card():
        new = randint(1, 13)
        final = new + final
        printl = Label(root2, text = "your number is" + str(final), fg = "white")
        printl.grid()
    def no_another():
        no_label = Label(root2, text = "your final number is" + str(final), fg = "white")
        no_label.grid()



    frame = LabelFrame(root2, padx = 30, pady = 30, bg = "grey")
    frame.grid(row = 0, column = 0)
    frame2 = LabelFrame(root2, padx=30, pady=30, bg="grey")
    frame2.grid(row = 0, column = 1)

    new_card = Button(frame, text="NEW CARD", command=another_card, bg="green", padx = 50)
    new_card.grid()
    stop_card = Button(frame2, text = "I don't want other" ,command =no_another(), bg = "red", padx = 50)
    stop_card.grid()

    my_number = Label(root2, text = "my number is " + str(first) + " and " + str(second), fg = "green", bg =  "black")
    my_number.grid(column = 0, row = 1,)






    root2.mainloop()


def but2():
    root3 = Tk()
    root2.title("2 player")
    root2.config(bg="black")
    root2.geometry("500x600")

    root3.mainloop()

def but3():
    root4 = Tk()
    root2.title("3 player")
    root2.config(bg="black")
    root2.geometry("500x600")

    root4.mainloop()
labelj= Label(root, text = "how many players?", fg = "dark green", bg = "black")
j1 = Button(root, text="1 player ", command = but1, padx = 2, bg = "green")
j2 = Button(root, text="2 players", command = but2, bg = "green")
j3 = Button(root, text="3 players", command = but3, bg = "green")




# poner los botones en pantalla

labelj.grid(row = 0, column = 1)
j1.grid(row = 1, column = 0)
j2.grid(row = 1, column = 1)
j3.grid(row = 1, column = 2)

root.mainloop()
