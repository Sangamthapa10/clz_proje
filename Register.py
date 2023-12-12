import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self, title, geo):
        super().__init__()
        self.title(title)
        self.geometry(f'{geo[0]}x{geo[1]}')
        self.register_page(geo)
        self.mainloop()

    def register_page(self, geo):
        self.columnconfigure((1, 2), weight=1, uniform='1')
        self.rowconfigure(1, weight=1)

        # left image screen
        left_screen = tk.Frame(self, bg='#ff416c')
        left_screen.grid(column=1, row=1, sticky='news')

        left_center = tk.Frame(left_screen, bg='#ff416c')
        left_center.grid(padx=(80, 0), pady=(190, 0))
        # img2 = 'register_taxi.jpeg'
        # self.image_tks = ImageTk.PhotoImage(Image.open(img2).resize((120, 120)))
        # label22 = tk.Label(left_center, image=self.image_tks, pady=160)
        # label22.grid()

        left_label_h = tk.Label(left_center,
                                text='Create a new account',
                                fg='#fff',
                                bg='#ff416c')
        left_label_h.config(font=("Motiva Sans", 22, 'bold'))
        left_label_h.grid()
        left_label_t = tk.Label(left_center,
                                text='It’s quick and easy',
                                fg='#fff',
                                bg='#ff416c')
        left_label_t.config(font=("Motiva Sans", 12, 'italic'))
        left_label_t.grid()
        left_label_t2 = tk.Label(left_center,
                                 text='Register with us and book your hotel right away',
                                 fg='#fff',
                                 bg='#ff416c')
        left_label_t2.config(font=("Motiva Sans", 12, 'italic'))
        left_label_t2.grid()

        def on_enter(e):
            register_btn['background'] = '#4CAF50'  # Change to a different color when hovered

        def on_leave(e):
            register_btn['background'] = '#388E3C'  # Change back to the original color when not hovered

        register_btn = tk.Button(left_center, width=30, bg='#fff', fg='black', font=('Arial', 12), text='Login')
        register_btn.bind("<Enter>", on_enter)
        register_btn.bind("<Leave>", on_leave)
        register_btn.grid(pady=20, padx=50)

        # right register screen
        right_screen = tk.Frame(self, background='#fff')
        right_screen.grid(column=2, row=1, sticky='news')
        login_frame = tk.Frame(right_screen, background='#fff')
        login_frame.grid(pady=(30, 0), padx=20)
        right_label_h = tk.Label(login_frame,
                                 text='Create a new account',
                                 fg='black',
                                 bg='#fff'
                                 )
        right_label_h.config(font=("Motiva Sans", 14, 'bold'))
        right_label_h.grid()
        username_frame = tk.Frame(
            login_frame,
            pady=10,
            bg='#fff',
        )
        username_frame.grid(pady=(10, 0))
        username_label = tk.Label(username_frame,
                                  fg='#1999ff',
                                  text='Enter Number',
                                  bg="#fff",
                                  )
        username_label.config(font=("Motiva Sans", 8, 'bold'))
        username_entry = ttk.Entry(username_frame, width=60)
        username_label.grid(sticky='w')
        username_entry.grid(pady=(0, 10),  ipady=5, ipadx=5)

        # first name and last name
        # label for it
        name_label = tk.Label(username_frame,
                              text='First and Last Name',
                              bg="#fff",
                              )
        name_label.grid(sticky='w')

        # frame and components
        name_frame = tk.Frame(login_frame, bg='#fff')
        name_frame.grid(sticky='w')
        first_name = ttk.Entry(name_frame,width=25)
        first_name.grid(column=1, row=1, ipady=5, ipadx=5)
        last_name = ttk.Entry(name_frame,width=25)
        last_name.grid(column=2, row=1,  padx=10, ipady=5, ipadx=5)

        # password label and entry
        password_frame = tk.Frame(login_frame,
                                  pady=10,
                                  bg='#fff')
        password_frame.grid()
        password_label = tk.Label(password_frame,
                                  text='Create Password',
                                  bg="#fff"
                                  )
        password_entry = ttk.Entry(password_frame, width=60)
        password_label.grid(sticky='w')
        password_entry.grid(ipady=5, ipadx=5)

        # again password label and entry
        password_frame2 = tk.Frame(login_frame, pady=10, bg='#fff')
        password_frame2.grid()
        password_label2 = tk.Label(password_frame2,
                                   text='Enter Password Again',
                                   bg="#fff"
                                   )
        password_entry2 = ttk.Entry(password_frame2, width=60)
        password_label2.grid(sticky='w')
        password_entry2.grid(ipady=5, ipadx=5)

        # Register button
        def on_enter(e):
            register_btn['background'] = '#4CAF50'  # Change to a different color when hovered

        def on_leave(e):
            register_btn['background'] = '#388E3C'  # Change back to the original color when not hovered

        register_btn = tk.Button(login_frame,
                                 bg='#00a400',
                                 fg='white',
                                 font=('Arial', 12),
                                 text='Create Account')
        register_btn.bind("<Enter>", on_enter)
        register_btn.bind("<Leave>", on_leave)
        register_btn.grid(pady=20, padx=50)


App('Register Page', (1000, 700))
