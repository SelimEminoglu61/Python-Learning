import tkinter as tk
from PIL import Image,ImageTk


class ForTkinder():
    def __init__(self,window):
        window.geometry("700x300")
        window.title("Translate-Sel")

        self.loadP=Image.open("C:\\Users\\SELİM\\Desktop\\987-200.png")
        self.render=ImageTk.PhotoImage(self.loadP)
        self.img=Label(window,image=self.render)
        self.img.image=self.render
        self.img.place(x=275,y=65)
        self.img.configure(background="blue")



window = tk.Tk()
w=ForTkinder(window)
window.mainloop()
