from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Frames')

root.iconbitmap('src/ninja_avatar.ico')

frame = LabelFrame(root, padx=50, pady=50)
frame.grid(row=0, column=0)

frame2 = LabelFrame(root, padx=50, pady=50)
frame2.grid(row=0, column=1)

frame3 = LabelFrame(root, padx=50, pady=50)
frame3.grid(row=1, column=0)

frame4 = LabelFrame(root, padx=50, pady=50)
frame4.grid(row=1, column=1)

b = Button(frame, text="Click here 1")
b.grid(row=0, column=0)

b2 = Button(frame, text="Click here 2")
b2.grid(row=1, column=1)

b3 = Button(frame2, text="Click here 3")
b3.grid(row=0, column=0)

b4 = Button(frame2, text="Click here 4")
b4.grid(row=1, column=1)

b5 = Button(frame3, text="Click here 5")
b5.grid(row=0, column=0)

b6 = Button(frame3, text="Click here 6")
b6.grid(row=1, column=1)

b7 = Button(frame4, text="Click here 7")
b7.grid(row=0, column=0)

b8 = Button(frame4, text="Click here 8")
b8.grid(row=1, column=1)

root.mainloop()