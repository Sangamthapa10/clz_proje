import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ttkbootstrap impor ttk
root = ttk.Tk()
root.geometry('900x900')
root.title('hello')

# widgets
# lab1=ttk.Label(text='Label 1',background='green')
# lab2=ttk.Label(text='second',background='red')
# lab3=ttk.Label(text='third',background='blue')
# lab4=ttk.Label(text='fourth',background='blue')
#


# images

root.columnconfigure((1,2),weight=1,uniform='a')
root.rowconfigure(1,weight=1)


#image
fram=tk.Frame(root)
fram.grid(column=1,row=1,sticky='news')
image_tk = ImageTk.PhotoImage(Image.open('wp7709776-bmw-s1000rr-2021-wallpapers (1).jpg').resize((450,300)))
label = ttk.Label(fram, image=image_tk)
label.pack()


#login
ram=tk.Frame(root,background='red')
ram.grid(column=2,row=1,sticky='news')

tk.Label(text='Login').grid()
tk.Entry(ram).grid()
tk.Entry(ram).grid()

# pack
# lab1.pack(side='bottom',expand=True,fill='both')
# lab2.pack(side='top',expand=True,fill='both')


# grid
# root.columnconfigure(1,weight=1)
# root.columnconfigure(2,weight=1)
# root.columnconfigure(3,weight=2)
# root.rowconfigure((1,2),weight=1)
# lab1.grid(column=3,row=1,sticky='news')
# lab2.grid(column=1,row=1,rowspan=2,columnspan=2,sticky='news')
# lab3.grid(column=2,row=1,sticky='news')
# lab4.grid(column=3,row=2,sticky='news')


# place
# lab1.place(x=50,y=870)

# run
root.mainloop()
