from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("CALCULATOR by Ayan Chavand")
root.iconbitmap("cal.ico")

def add(number):
    #e.delete(0, END)
    no = e.get() 
    e.delete(0, END)
    e.insert(0,str(no) + str(number))

def clear():
    e.delete(0, END)

def  plus():
    f_n = e.get()
    global f_num 
    f_num = int(f_n)
    e.delete(0, END)

def eql():
    second_n = e.get()
    e.delete(0, END)
    e.insert(0,f_num + int(second_n))
e = Entry(root, width=10, borderwidth=2)

box_9 = Button(root, padx=30, pady=10, text="9", command=lambda: add(9))
box_8 = Button(root, padx=30, pady=10, text="8", command=lambda: add(8))
box_7 = Button(root, padx=30, pady=10, text="7", command=lambda: add(7))
box_6 = Button(root, padx=30, pady=10, text="6", command=lambda: add(6))
box_5 = Button(root, padx=30, pady=10, text="5", command=lambda: add(5))
box_4 = Button(root, padx=30, pady=10, text="4", command=lambda: add(4))
box_3 = Button(root, padx=30, pady=10, text="3", command=lambda: add(3))
box_2 = Button(root, padx=30, pady=10, text="2", command=lambda: add(2))
box_1 = Button(root, padx=30, pady=10, text="1", command=lambda: add(1))
box_0 = Button(root, padx=30, pady=10, text="0", command=lambda: add(0))
box_eql = Button(root, padx=30, pady=10, text="=", command=eql)
box_clear = Button(root, padx=25, pady=10, text="clear", command=clear)
box_add = Button(root, padx=30, pady=10, text="+", command=plus)
e.grid(row=0, column=0)

box_9.grid(row=1, column=2)
box_8.grid(row=1, column=1)
box_7.grid(row=1, column=0)

box_6.grid(row=2, column=2)
box_5.grid(row=2, column=1)
box_4.grid(row=2, column=0)

box_3.grid(row=3, column=2)
box_2.grid(row=3, column=1)
box_1.grid(row=3, column=0)

box_0.grid(row=4, column=1)

box_clear.grid(row=4, column=0)
box_add.grid(row=4, column=2)
box_eql.grid(row=5, column=1)


root.mainloop()