import random
from random import randint
import tkinter as tk
import hashlib

#hs = hashlib.md5(___.encord)

#ハッシュ関数を用いた判別を行う

Card = []
card_chack = []
row1 = []
row2 = []
row3 = []
row4 = []
row5 = []

def bingo_card(event):
    row1.append(random.sample(range(1,15), k=5))

    row2.append(random.sample(range(16,30), k=5))

    row3.append(random.sample(range(31,45), k=5))

    row4.append(random.sample(range(46,60), k=5))

    row5.append(random.sample(range(61,75), k=5))
    Card.extend([row1,row2,row3,row4,row5])
    print(Card)

#GUI
root = tk.Tk()

root.title(u"Bingo_Card")
root.geometry("400x300")

Button1 = tk.Button(text=u"test",width=10)
Button1.pack()

Button1.bind("<Button-1>",bingo_card)

root.mainloop()


# print(row1)
# print(row2)
# print(row3)
# print(row4)
# print(row5)
# print(card_chack)


#https://tomtom-stock.com/2023/02/05/tkinter-create-newwindow/