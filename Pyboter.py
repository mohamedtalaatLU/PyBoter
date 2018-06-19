import tkinter as tk
import BotBase as b


def CreateBot():
    f = open("bot.py","w")
    f.write(b.s)

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        return
    

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Creat \n a \n Bot"
        self.hi_there["command"] = CreateBot()
        self.hi_there.pack(side="top")
        self.hi_there.size()
        self.quit = tk.Button(self, text="QUIT", fg="red", bg = "yellow", command=root.destroy)
        self.quit.pack(side="bottom")





root = tk.Tk()
app = App()
app = app.master
app.minsize(500,500)
app.title("PyBoter")
app.mainloop()
