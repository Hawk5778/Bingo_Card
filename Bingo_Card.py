import random
from random import randint
import tkinter as tk
import hashlib

#hs = hashlib.md5(___.encord)

#ハッシュ関数を用いた判別を行う

Card = []

def create_card():
    for n in range(5):
        Card.extend(random.sample(range(1+15*n,15*(n+1)), k=5))
    print(Card)

#def button_color():

def callback(button):
    def nothing():
        button.config(bg="#008000")
    return nothing

#GUI
root = tk.Tk()

root.title("Bingo_Card")
root.geometry("400x300")

#ボタンを押すとそのボタンの色が変わるようにする。
#列がそろった場合、BINGOと表示させたい。

#Button
row = 0
column = 0

for n in range(25):
        button = tk.Button(root, text="test")
        button.grid(column=column, row=row)
        button.config(command=callback(button))
root.mainloop()

#無理やり表示させる場合
# Button01 = tk.Button(root, text="01", command = button_color).grid(row=0,column=0)
# Button02 = tk.Button(root, text="02", command = create_card).grid(row=1,column=0)
# Button03 = tk.Button(root, text="03", command = create_card).grid(row=2,column=0)
# Button04 = tk.Button(root, text="04", command = create_card).grid(row=3,column=0)
# Button05 = tk.Button(root, text="05", command = create_card).grid(row=4,column=0)
# Button06 = tk.Button(root, text="06", command = create_card).grid(row=0,column=1)
# Button07 = tk.Button(root, text="07", command = create_card).grid(row=1,column=1)
# Button08 = tk.Button(root, text="08", command = create_card).grid(row=2,column=1)
# Button09 = tk.Button(root, text="09", command = create_card).grid(row=3,column=1)
# Button10 = tk.Button(root, text="10", command = create_card).grid(row=4,column=1)
# Button11 = tk.Button(root, text="11", command = create_card).grid(row=0,column=2)
# Button12 = tk.Button(root, text="12", command = create_card).grid(row=1,column=2)
# Button13 = tk.Button(root, text="13", command = create_card).grid(row=2,column=2)
# Button14 = tk.Button(root, text="14", command = create_card).grid(row=3,column=2)
# Button15 = tk.Button(root, text="15", command = create_card).grid(row=4,column=2)
# Button16 = tk.Button(root, text="16", command = create_card).grid(row=0,column=3)
# Button17 = tk.Button(root, text="17", command = create_card).grid(row=1,column=3)
# Button18 = tk.Button(root, text="18", command = create_card).grid(row=2,column=3)
# Button19 = tk.Button(root, text="19", command = create_card).grid(row=3,column=3)
# Button20 = tk.Button(root, text="20", command = create_card).grid(row=4,column=3)
# Button21 = tk.Button(root, text="21", command = create_card).grid(row=0,column=4)
# Button22 = tk.Button(root, text="22", command = create_card).grid(row=1,column=4)
# Button23 = tk.Button(root, text="23", command = create_card).grid(row=2,column=4)
# Button24 = tk.Button(root, text="24", command = create_card).grid(row=3,column=4)
# Button25 = tk.Button(root, text="25", command = create_card).grid(row=4,column=4)


#Button1.grid(row=0,column=0)
#Button1.pack()

#Button1.bind("<Button-1>",create_card)



#https://tomtom-stock.com/2023/02/05/tkinter-create-newwindow/
#https://qiita.com/igor-bond16/items/39c8b75d844f30cea197
