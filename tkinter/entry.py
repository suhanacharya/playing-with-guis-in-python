from tkinter import *

root = Tk()

e = Entry(root)
e.pack()
e.insert(0, "Enter your name:")

def myClick():
    myLabel = Label(root, text="hello, " + e.get())
    myLabel.pack()

myButton = Button(root, text="Enter", command=myClick)
myButton.pack()

root.mainloop()