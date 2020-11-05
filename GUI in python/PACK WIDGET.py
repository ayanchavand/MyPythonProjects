from tkinter import *

root = Tk()

def click():
    myLabel = Label(root, text="clicked it!!", style="bold"  )
    myLabel.pack()
myLabel = Label(root, text="hello world!")
myButton = Button(root, text="click me!!", padx=50, pady=50, command=click,bg="white")

myLabel.pack()
myButton.pack()

root.mainloop()
