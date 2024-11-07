import random
from random import randint
import tkinter as tk
import tkinter.font as tkFont
import hashlib

#ハッシュ関数を用いた判別を行う
#ビンゴと表示させる
#色の変更


number_list = []
hash_list = []
green_list = []

def create_list():
    for n in range(5):
        number_list.extend(random.sample(range(1+15*n,15*(n+1)), k=5))
    create_hash()

def create_hash():
    list_text =  ''.join(map(str, number_list))
    #print(list_text)
    hash_md5 = hashlib.md5(list_text.encode()).hexdigest()
    #print(f'MD5: {hash_md5}')
    hash_list.append(hash_md5)


def change_color(button):
    def color():
        button.config(bg = "green")
        #ここで関数を作ってもいいかもしれない。
        x = button.cget("text")
        if x == "X":
            green_list.append("X")
        else:
            green_list.append(number_list.index(x))
        print(green_list)
        bingo()
    return color

#いい記法が思いつかないので放置
#変数を動的にするとなぜか正常に動かないため要検証
def bingo():
    #縦
    x0  = [0,1,2,3,4] 
    x1  = [5,6,7,8,9]
    x2  = [10,11,"X",13,14]
    x3  = [15,16,17,18,19]
    x4  = [20,21,22,23,24]
    #横
    x5  = [0,5,10,15,20]
    x6  = [1,6,11,16,21]
    x7  = [2,7,"X",17,22]
    x8  = [3,8,13,18,23]
    x9  = [4,9,14,19,24]
    #斜め
    x10 = [0,6,"X",18,24]
    x11 = [4,8,"X",16,20] 

    if set(x0).issubset(green_list) == True:
        print("bingo")
    elif set(x1).issubset(green_list) == True:
        print("bingo")
    elif set(x2).issubset(green_list) == True:
        print("bingo")
    elif set(x3).issubset(green_list) == True:
        print("bingo")
    elif set(x4).issubset(green_list) == True:
        print("bingo")
    elif set(x5).issubset(green_list) == True:
        print("bingo")
    elif set(x5).issubset(green_list) == True:
        print("bingo")
    elif set(x6).issubset(green_list) == True:
        print("bingo")
    elif set(x7).issubset(green_list) == True:
        print("bingo")
    elif set(x8).issubset(green_list) == True:
        print("bingo")
    elif set(x9).issubset(green_list) == True:
        print("bingo")
    elif set(x10).issubset(green_list) == True:
        print("bingo")
    elif set(x11).issubset(green_list) == True:
        print("bingo")
    else: 
        print("continue")

create_list()
print(hash_list)


#GUI
root = tk.Tk()

root.title("Bingo_Card")
root.geometry("400x450")

#Button

row    = 0
column = 0
text   = 0

for x in range(5):
    row = 0
    column += 1
    for y in range(5):
        row += 1
        if x == 2 and y == 2:
            button = tk.Button(root, text="X",width = 10, height = 5)
        else:
            button = tk.Button(root, text=number_list[text],width = 10, height = 5)
        button.grid(column=column, row=row)
        button.config(command=change_color(button))
        text += 1

root.mainloop()

#メモ
#gridでpackと同じ様になる。
#set(x).issubset(y)ではformatやexecは使えない模様。なんで？
#https://tomtom-stock.com/2023/02/05/tkinter-create-newwindow/
#https://qiita.com/igor-bond16/items/39c8b75d844f30cea197
#https://www.delftstack.com/ja/howto/python-tkinter/how-to-change-the-tkinter-button-size/
#https://tomtom-stock.com/2023/02/05/tkinter-create-newwindow/
