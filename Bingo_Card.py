import random
from random import randint
import tkinter as tk
import tkinter.font as tkFont
import hashlib

random_list = []
hash_list = []
green_list = []

class card:
    def __init__(self):
        self.random_list = random_list  
        self.hash_list = hash_list
        self.green_list = green_list
    
    def create_list(): 
        for i in range(5):
            random_list.extend(random.sample(range(1+15*i, 15*(i+1)), k=5))
        card.creat_hash()

    def creat_hash():
        list_text =  ''.join(map(str, random_list))
        hash_md5 = hashlib.md5(list_text.encode()).hexdigest()
        #if 
        hash_list.append(hash_md5)
        print(hash_list)

    def change_color(button):
        def color():
            button.config(bg = "green")
            x = button.cget("text")
            if x == "X":
                green_list.append("X")
            else:
                green_list.append(random_list.index(x))
            card.bingo()
        return color

    def bingo():
        x0  = [0,1,2,3,4] 
        x1  = [5,6,7,8,9]
        x2  = [10,11,13,14]
        x3  = [15,16,17,18,19]
        x4  = [20,21,22,23,24]
        x5  = [0,5,10,15,20]
        x6  = [1,6,11,16,21]
        x7  = [2,7,17,22]
        x8  = [3,8,13,18,23]
        x9  = [4,9,14,19,24]
        x10 = [0,6,18,24]
        x11 = [4,8,16,20] 

        if (set(x0).issubset(green_list) or set(x1).issubset(green_list)  or set(x2).issubset(green_list)   or 
            set(x3).issubset(green_list) or set(x4).issubset(green_list)  or set(x5).issubset(green_list)   or
            set(x6).issubset(green_list) or set(x7).issubset(green_list)  or set(x8).issubset(green_list)   or 
            set(x9).issubset(green_list) or set(x10).issubset(green_list) or set(x11).issubset(green_list)) == True:
            print("bingo")
            window.label.config(text="BINGO!!",bg="red")

        elif (len(set(x0)&set(green_list)) or len(set(x1)&set(green_list)) or len(set(x3)&set(green_list)) or 
              len(set(x4)&set(green_list)) or len(set(x5)&set(green_list)) or len(set(x6)&set(green_list)) or
              len(set(x8)&set(green_list)) or len(set(x9)&set(green_list))) == 4:
            print("uno")
            window.label.config(text="UNO!",bg="yellow")

        elif (len(set(x2)&set(green_list)) or len(set(x7)&set(green_list)) or
               len(set(x10)&set(green_list)) or len(set(x11)&set(green_list))) == 3:
            print("uno")
            window.label.config(text="UNO!",bg="yellow")

        else: 
            print("continue")


class window:
    label = None

    def main_window():
        main_window = tk.Tk()

        main_window.title("BINGO System")
        main_window.geometry("400x300")

        tk.Label(main_window, text="BINGO System").pack()

        tk.Button(text="creat new card", command = window.sub_window).pack()
        tk.Button(text="view hash list").pack()

        main_window.mainloop()

    def sub_window():
        card.create_list()

        sub_window = tk.Toplevel()

        sub_window.title("BINGO Card")
        sub_window.geometry("700x430")
        
        tk.Label(sub_window, text="BINGO Card", font=("Arial", 25)).place(x=450,y=10)
        window.label = tk.Label(sub_window, text="No BINGO", font=("Arial",25))
        window.label.place(x=470,y=200)

        row    = 0
        column = 0
        text   = 0

        for x in range(5):
            row = 1
            column += 1
            for y in range(5):
                row += 1
                if x == 2 and y == 2:
                    button = tk.Button(sub_window, text="X",width = 10, height = 5, bg = "green")
                else:
                    button = tk.Button(sub_window, text=random_list[text],width = 10, height = 5)
                button.grid(column=column, row=row)
                button.config(command=card.change_color(button))
                text += 1        

        sub_window.mainloop()

window.main_window()
