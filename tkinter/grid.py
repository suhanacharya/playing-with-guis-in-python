from tkinter import *

root = Tk()

# Creating a label Widget
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="My name is Suhan")
# myLabel3 = Label(root, text="                 ")

#Show Label into the screen
myLabel1.grid(row=1, column="1")
myLabel2.grid(row=2, column="3")
# myLabel3.grid(row=1, column="2")

root.mainloop()