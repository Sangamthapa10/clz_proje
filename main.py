import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk


# import ttkbootstrap as bootstrap


class App(tk.Tk):
    def __init__(self, title, geo):
        super().__init__()
        self.image_tk = None
        self.title(title)
        self.geometry(f'{geo[0]}x{geo[1]}')
        self.login_page(geo)
        self.mainloop()

    def login_page(self, geo):

        # image frame
        left_frame = tk.Frame(self)
        left_frame.grid(column=1, row=1, sticky='news')
        img1 = 'login.png'
        self.image_tk = ImageTk.PhotoImage(Image.open(img1).resize((int(geo[0] / 2), geo[1])))
        label1 = tk.Label(left_frame, image=self.image_tk)
        label1.grid(sticky='news')

        # login frame
        right_frame = tk.Frame(self, background='#fff', pady=40)
        right_frame.grid(column=2, row=1, sticky='news', ipady=40)
        # grid for right frame
        # right_frame.columnconfigure(1, weight=1)
        # right_frame.columnconfigure(2, weight=30)
        # right_frame.columnconfigure(3, weight=1)
        login_frame = tk.Frame(right_frame, background='#fff')
        login_frame.grid()
        # login profile img
        img2 = 'ltop.png'
        self.image_tks = ImageTk.PhotoImage(Image.open(img2).resize((120, 120)))
        label22 = tk.Label(login_frame, image=self.image_tks, pady=160)
        label22.grid()
        # username label and entry
        username_frame = tk.Frame(
            login_frame,
            bg='#fff',
        )
        username_frame.grid(pady=(10, 0)
                            )
        username_label = tk.Label(username_frame,
                                  fg='#1999ff',
                                  text='SIGN IN WITH ACCOUNT NAME',
                                  bg="#fff",
                                  )
        username_label.config(font=("Motiva Sans", 8, 'bold'))
        username_entry = ttk.Entry(username_frame, width=60)
        username_label.grid(sticky='w')
        username_entry.grid(pady=(0, 10), padx=10, ipady=5, ipadx=5)
        # password label and entry
        password_frame = tk.Frame(login_frame, pady=10, bg='#fff')
        password_frame.grid()
        password_label = tk.Label(password_frame,
                                  text='Enter Password',
                                  bg="#fff"
                                  )
        password_entry = ttk.Entry(password_frame, width=60)
        password_label.grid(sticky='w')
        password_entry.grid(ipady=5, ipadx=5)
        # checkbox login
        check_frame = tk.Frame(login_frame, bg='#fff')
        check_frame.grid(sticky='w')
        checkbox_ = tk.Checkbutton(check_frame,
                                   bg='#fff',
                                   text='Keep me logged in',
                                   onvalue='agree',
                                   offvalue='disagree', )
        checkbox_.grid()

        # login button
        def on_enter(e):
            login_btn['background'] = '#4CAF50'  # Change to a different color when hovered

        def on_leave(e):
            login_btn['background'] = '#388E3C'  # Change back to the original color when not hovered

        login_btn = tk.Button(login_frame, width=40, bg='#388E3C', fg='white', font=('Arial', 12), text='Login')
        login_btn.bind("<Enter>", on_enter)
        login_btn.bind("<Leave>", on_leave)
        login_btn.grid(pady=20, padx=50)


App('Login Page', (1000, 700))
