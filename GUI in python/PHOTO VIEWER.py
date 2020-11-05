from tkinter import *
from PIL import ImageTk,Image
window = Tk()
window.iconbitmap("cal.ico")


def forward():
    global my_label
    global forward_b
    global backward_b
    global i
    i=0
    i=i+1

    img_label.grid_forget()
    img = Label(image=img_list[i])
    img.grid(row=0, column=0)

window.title("hello world") 
my_image1 = ImageTk.PhotoImage(Image.open("photos/pugb.jpg"))
my_image2 = ImageTk.PhotoImage(Image.open("photos/p1.jpg"))
my_image3 = ImageTk.PhotoImage(Image.open("photos/p2.jpg"))
my_image4 = ImageTk.PhotoImage(Image.open("photos/p3.jpg"))
my_image5 = ImageTk.PhotoImage(Image.open("photos/p4.jpg"))

img_list = [my_image1,my_image2,my_image3,my_image4,my_image5]

img_label = Label(window, image=my_image1)

exit_b= Button(text="exit", padx=50, command=window.quit)
forward_b= Button(text=">>", padx=50, command=forward)
backward_b= Button(text="<<", padx=50)

img_label.grid(row=0, column=0, columnspan=3)
backward_b.grid(row=1, column=0)
exit_b.grid(row=1,column=1) 
forward_b.grid(row=1, column=2)


window.mainloop()