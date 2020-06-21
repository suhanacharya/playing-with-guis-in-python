from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Sliders')
root.iconbitmap('src/ninja_avatar.ico')
root.geometry("400x400")


def slide():
	my_label = Label(root, text=horizontal_slider.get()).pack()


vertical_slider = Scale(root, from_=0, to=200).pack()

horizontal_slider = Scale(root, from_=0, to=200,
						  orient=HORIZONTAL)
horizontal_slider.pack()

my_button = Button(root, text="Current pos", command=slide).pack()


root.mainloop()
