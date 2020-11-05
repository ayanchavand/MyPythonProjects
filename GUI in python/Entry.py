from tkinter import *

root = Tk()

def button():
    l1 = Label(root, text=e.get())
    l1.pack()
l = Label(root, text="enter your password")
e = Entry(root, )
b = Button(root, command=button, text="confirm")
l.pack()
e.pack()
b.pack()
root.mainloop()
