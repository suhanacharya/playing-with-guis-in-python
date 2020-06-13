import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self, bg="blue", fg="white")
        self.hi_there["text"] = "Hello World\n(click me)"
        self.konichiwa = tk.Button(self, bg="red")
        self.konichiwa["text"] = "Konichiwa\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.konichiwa["command"] = self.say_konichiwa
        self.hi_there.pack(side="top")
        self.konichiwa.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
    
    def say_konichiwa(self):
        print("konichiwa, mina san!")

root = tk.Tk()
app = Application(master=root)
app.master.title("The Hello App")
app.master.maxsize(1000, 400)

app.mainloop()
