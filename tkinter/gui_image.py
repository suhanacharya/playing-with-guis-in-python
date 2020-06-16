from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('')

root.iconbitmap('src/ninja_avatar.ico')

my_image = ImageTk.PhotoImage(Image.open('src/ninja.png'))
my_label = Label(image=my_image)

my_label.pack()


exit_button = Button(text="Exit Program", command=root.quit)
exit_button.pack

root.mainloop()