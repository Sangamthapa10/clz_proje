import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
class App(tk.Tk):

    def __init__(self,title,geo):
        super().__init__()
        self.title(title)
        self.geometry(f'{geo[0]}x{geo[1]}')
        self.home()
        self.mainloop()


    def home(self):
      




App('Taxi App',(1200,900))