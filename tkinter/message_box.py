from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

root = Tk()
root.title("Radio button program")
root.iconbitmap('src/ninja_avatar.ico')


def popup():
	messagebox.showinfo("Help me Obi-wan Kenobi!", "You're my only hope")


my_button = Button(root, text="Hope", command=popup)
my_button.pack()

mainloop()
