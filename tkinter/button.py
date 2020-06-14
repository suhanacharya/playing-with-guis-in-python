from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button")
    myLabel.pack()


# myButton = Button(root, text="Click Me!", state=DISABLED)
# myButton = Button(root, text="Click Me!", padx=50, pady=50)
myButton = Button(root, text="Click Me!", command=myClick, fg="blue", bg="#000000")
# myButton

myButton.pack()

root.mainloop()