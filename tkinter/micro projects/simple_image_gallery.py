from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Simple Image Gallery')
root.iconbitmap('../src/ninja_avatar.ico')

# my_image1 = ImageTk.PhotoImage(Image.open('../src/ninja.png'))
# my_image2 = ImageTk.PhotoImage(Image.open('../src/whale.png'))
# my_image3 = ImageTk.PhotoImage(Image.open('../src/tiger.png'))
# my_image4 = ImageTk.PhotoImage(Image.open('../src/wild.png'))
# my_image5 = ImageTk.PhotoImage(Image.open('../src/squirrel.png'))

my_image1 = ImageTk.PhotoImage(Image.open('../src/bird.jpg'))
my_image2 = ImageTk.PhotoImage(Image.open('../src/dragonfly.jpg'))
my_image3 = ImageTk.PhotoImage(Image.open('../src/flower.jpg'))
my_image4 = ImageTk.PhotoImage(Image.open('../src/ladybug.jpg'))
my_image5 = ImageTk.PhotoImage(Image.open('../src/petal.jpg'))

image_list = [my_image1, my_image2, my_image3, my_image4, my_image5]
image_num = 0

my_label = Label(image=image_list[0])
status_bar = Label(root, text="Image " + str(image_num + 1) + " / " + str(
		len(image_list)), bd=1, relief=SUNKEN, anchor=E)
status_bar.grid(row=2, column=0, columnspan=3, sticky=W+E)


def go_back():
	global image_num
	global my_label
	global button_forward
	global button_back
	global image_list
	global status_bar

	if 0 < image_num:
		image_num -= 1
		my_label.grid_forget()
		my_label = Label(image=image_list[image_num])
		my_label.grid(row=0, column=0, columnspan=3)

		button_forward = Button(root, text=">>", command=go_forward)
		button_forward.grid(row=1, column=2)

	if image_num == 0:
		button_back = Button(root, text="<<", state=DISABLED)
		button_forward = Button(root, text=">>", command=go_forward)
		button_forward.grid(row=1, column=2)
		button_back.grid(row=1, column=0)
	else:
		button_back = Button(root, text="<<", command=go_back)
		button_back.grid(row=1, column=0)

	status_bar = Label(root, text="Image " + str(image_num + 1) + " / " + str(
		len(image_list)), bd=1, relief=SUNKEN, anchor=E)
	status_bar.grid(row=2, column=0, columnspan=3, sticky=W+E)


def go_forward():
	global image_num
	global my_label
	global button_forward
	global button_back
	global image_list
	global status_bar

	if image_num + 1 < len(image_list):
		image_num += 1
		my_label.grid_forget()
		my_label = Label(image=image_list[image_num])
		my_label.grid(row=0, column=0, columnspan=3)

		button_back = Button(root, text="<<", command=go_back)
		button_back.grid(row=1, column=0)

	if image_num == len(image_list)-1:
		button_forward = Button(root, text=">>", state=DISABLED)
		button_forward.grid(row=1, column=2)

	status_bar = Label(root, text="Image " + str(image_num + 1) + " / " + str(
		len(image_list)), bd=1, relief=SUNKEN, anchor=E)
	status_bar.grid(row=2, column=0, columnspan=3, sticky=W+E, )


my_label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text="<<", command=go_back, state=DISABLED)
exit_button = Button(text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=go_forward)

button_back.grid(row=1, column=0)
exit_button.grid(row=1, column=1, pady=10)
button_forward.grid(row=1, column=2)

root.mainloop()
