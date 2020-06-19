from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

root = Tk()
root.title("Radio button program")
root.iconbitmap('src/ninja_avatar.ico')


def popup():
	response = messagebox.askokcancel("Help me Obi-wan Kenobi!", "You're my only " 
														"hope")
	#response = messagebox.showinfo("Help me Obi-wan Kenobi!", "You're my
	# only " "hope")
	# Label(root, text=response).pack()
	# messagebox.showerror("Help me Obi-wan Kenobi!", "You're my only hope")
	# messagebox.showerror("Help me Obi-wan Kenobi!", "You're my only hope")
	# messagebox.askquestion("Help me Obi-wan Kenobi!", "You're my only hope")
	# messagebox.askokcancel("Help me Obi-wan Kenobi!", "You're my only hope")
	# messagebox.askyesno("Help me Obi-wan Kenobi!", "You're my only hope")
	# messagebox.showwarning("Get out", "Go!!")

	if response == 1:
		Label(root, text="You clicked Yes!").pack()
	else:
		Label(root, text="You clicked NO!").pack()




my_button = Button(root, text="Hope", command=popup)
my_button.pack()

mainloop()
