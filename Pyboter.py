import tkinter as tk
import BotBase as b


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        return
    

    def create_widgets(self):
        self.widg = tk.Button(self)
        self.widg["text"] = "Creat \n a \n Bot"
        f = open("bot.py","w")
        self.widg["command"] = f.write(b.s)
        self.widg.pack(side="top")
        self.widg.size()
        self.quit = tk.Button(self, text="QUIT", fg="red", bg = "yellow", command=root.destroy)
        self.quit.pack(side="bottom")





root = tk.Tk()
app = App()
app = app.master
app.minsize(500,500)
app.title("PyBoter")
app.mainloop()
