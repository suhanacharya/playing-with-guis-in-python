from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title('Opening files')
root.iconbitmap('src/ninja_avatar.ico')


def open_file():
	global my_image
	root.filename = filedialog.askopenfilename(initialdir=".s",
		title="Select a file", filetypes=(("PNG Files", "*.png"),
			("All files", "*.*")))
	my_image = ImageTk.PhotoImage(Image.open(root.filename))
	my_label = Label(image=my_image).pack()


my_button = Button(root, text="Add file", command=open_file).pack()

root.mainloop()