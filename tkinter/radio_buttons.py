from tkinter import *

root = Tk()
root.title("Radio button program")
root.iconbitmap('src/ninja_avatar.ico')

basket = StringVar()
basket.set("Juice")


def clicked(value):
	my_label = Label(root, text=basket.get())
	my_label.pack()


groceries = [
	("Apples", "Apples"),
	("Shampoo", "Shampoo"),
	("Chocolate", "Chocolate"),
	("Juice", "Juice")
]

for text, item in groceries:
	Radiobutton(root, text=text, variable=basket, value=item).pack(anchor=W)

my_label = Label(root, text=basket.get())
my_label.pack()

my_button = Button(root, text="order!", command=lambda: clicked(basket.get()))
my_button.pack()

mainloop()
