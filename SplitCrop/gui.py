from tkinter import *




def print_user():
    print(user_var.get())


starting_window = Tk()
starting_window.title("Split|Crop")
starting_window.minsize(270, 200)
starting_window.iconbitmap(r"./static/iconDP.ico")

split_crop = Label(text="Split|Crop", font=("Ariel", 16))
split_crop.grid(column=1, row=0, pady=5)

info_label = Label(text="This is an info\n" + "label, tells you what\n" + "to do next.\n")
info_label.grid(column=1, row=5, pady=10)

user_label = Label(text="Username")
user_label.grid(column=0, row=1, padx=5)

password_label = Label(text="Password")
password_label.grid(column=0, row=2, padx=5)

user_var = StringVar()
user_entry = Entry(text="Username", textvariable=user_var,)
user_entry.grid(column=1, row=1)

password_var = StringVar()
password_entry = Entry(text="password", textvariable=password_var)
password_entry.grid(column=1, row=2, padx=10)

login_user_button = Button(text="Login",)
login_user_button.grid(column=1, row=3, pady=15)

register_user_button = Button(text="Register",)
register_user_button.grid(column=1, row=4)
starting_window.mainloop()
