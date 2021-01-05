from random import *

# clase para el juego

class game :
    def __init__(self):
        a = randint(1, 13)
        b = randint(1, 13)
        print("number 1=")
        print(a)
        print("number 2=")
        print(b)
        c = a + b
        print("total=")
        print(c)
        while c < 21:
            print("another?"  "yas/no")
            d = input()
            if d == "yes":
                ran1 = randint(1, 13)
                c = c + ran1
                print(ran1)
                print(c)

            elif d == "no":
                print("your number still =")
                print(c)
                break
            else:
                print("no out put")
        if c == 21:
            print("you win")
        elif c > 21:
            print("you lose")

class no_j:
    def _init_(self):
        self = "yyyy"
        print(self)

    def two(s):
        s = "zzz"
        print(s)

    def three(y):
        y = "iii"
        print(y)
