from tkinter import *

root = Tk()

def login(email,pswd):
     text_3 = Label(root,text="E-mail:  ") 
     text_3.grid(row=4,column=0)
    if email =="asdfg" and pswd == 1234:
       text_3 = Label(root,text="E-mail:  ") 
       text_3.grid(row=4,column=0)
        
root.title("Login window")
root.geometry("200x200")
text_1 = Label(root,text="E-mail:  ")
box_1 = Entry(root,width=20)
text_2 = Label(root,text="Password:  ")
box_2 = Entry(root,width=20)
button = Button(root,text="Login!!",command = lambda: login(box_1.get(),box_2.get()),padx=30)

text_1.grid(row=0,column=0,columnspan=1)
box_1.grid(row=0,column=1)
text_2.grid(row=1,column=0,columnspan=1)
box_2.grid(row=1,column=1)
button.grid(row=3,column=0,columnspan=30)


root.mainloop()