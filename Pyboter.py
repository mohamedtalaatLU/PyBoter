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
        self.widg["text"] = "Create \n a \n Bot"
        f = open("bot.py","w")
        self.widg["command"] = f.write(b.s)
        self.widg.pack(side="top")
        self.widg.size()
        self.butt = tk.Button(self, text= "Enable anti-spam", command= None)#the command is not implemented yet
        self.butt.pack(side="right")

        def show_box():
            mstr = tk.Tk()
            tk.Label(mstr, text = "SQL host or IP").grid(row = 3)
            e = tk.Entry(mstr)
            e.grid(row = 3 , column = 3)#thanks to noud02 the credits of creating this function goes to him

        self.butt1 = tk.Button(self, text="DB based bot", command=show_box)

        self.butt1.pack(side = "left")
        self.butt2 = tk.Button(self, text ="Change game the bot is playing")
        self.quit = tk.Button(self, text="QUIT", fg="red", bg = "yellow", command=root.destroy)
        self.quit.pack(side="bottom")





root = tk.Tk()
app = App()
app = app.master
app.minsize(500,500)
app.title("PyBoter")
app.mainloop()
