from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image

root = Tk()
root.title('Sliders')
root.iconbitmap('src/ninja_avatar.ico')
root.geometry("400x400")

var = IntVar()


def show():
	my_label = Label(root, text=clicked.get()).pack()


opts = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
clicked = StringVar()
clicked.set(opts[0])
drop = OptionMenu(root, clicked, *opts)
drop.pack()

my_button = Button(root, text="show", command=show).pack()
# my = Button(root, text="HELLO", command=check_value).pack()

root.mainloop()
