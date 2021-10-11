from tkinter import *


def print_user():
    print(user_var.get())


starting_window = Tk()
starting_window.title("Split|Crop")
# starting_window.minsize(480, 640)
starting_window.iconbitmap(r"./static/iconDP.ico")

user_var = StringVar()
password_var = StringVar()


info_label = Label(text="This is an info\n" + "label, tells you what\n" + "to do next.\n")
info_label.grid(column=0, row=0)

user_label = Label(text="Username")
user_label.grid(column=0, row=1)

password_label = Label(text="Password")
password_label.grid(column=0, row=2)

user_entry = Entry(text="Username", textvariable=user_var,)
user_entry.grid(column=1, row=1)

password_entry = Entry(text="password", textvariable=password_var)
password_entry.grid(column=1, row=2, padx=50, pady=5)

print_user_button = Button(text="Print User", command=print_user)
print_user_button.grid(column=1, row=3, pady=10,)


starting_window.mainloop()
