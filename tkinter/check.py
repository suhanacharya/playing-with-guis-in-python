from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image

root = Tk()
root.title('Sliders')
root.iconbitmap('src/ninja_avatar.ico')
root.geometry("400x400")

var = IntVar()


def check_value():
	my_label = Label(root, text=var.get()).pack()


c = Checkbutton(root, text="Check this", variable=var)
c.pack()

my = Button(root, text="HELLO", command=check_value).pack()

root.mainloop()
