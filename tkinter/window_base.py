from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Root window")
root.iconbitmap('src/ninja_avatar.ico')
my_image = ImageTk.PhotoImage(Image.open('src/ninja.png'))


def on_click():
	top1 = Toplevel()
	top2 = Toplevel()
	l2 = Label(top1, text="Hello Root").pack()
	l3 = Label(top2, text="Hello New 2").pack()


my_label = Label(image=my_image)
my_label.pack()
exit_button = Button(text="Exit Program", command=root.quit)
new_button = Button(text="click", command=on_click).pack()
exit_button.pack()




root.mainloop()
