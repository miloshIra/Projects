from tkinter import *
from models import User
from tkinter import filedialog
import time


def login():
    registered_user = User(user_var.get(), password_var.get())
    report = registered_user.login()
    info_label.config(text=report)
    if report == True:
        go_to_work_window()


def register():
    new_user = User(user_var.get(), password_var.get())
    report = new_user.register()
    info_label.config(text=report)


def print_user():
    print(user_var.get())


def go_to_work_window():
    """Open working window after logging in"""
    work_window = Toplevel(log_window)
    work_window.geometry("400x350")
    work_window.title("Work window")
    work_window.focus_force()
    time.sleep(0.5)
    log_window.withdraw()  # Hides logging window

    def file_browser():
        filename = filedialog.askopenfilename(initialdir="Desktop", title="Select photo",
                                              filetypes=(("jpg files", "*.jpg"),
                                                     ("png files", "*.png"),
                                                     ("all files", "*.*")))

        print(filename)
        # return filename

    # find_photo_label = Label(work_window, text="Select photo")
    # find_photo_label.grid(column=0, row=0, padx=15, pady=10)

    find_photo_button = Button(work_window, text="Select photo", command=file_browser)
    find_photo_button.grid(column=0, row=0, padx=15, pady=10)

    photo_frame_widget = LabelFrame(work_window, text=" Editing Image ")
    photo_frame_widget.grid(column=0, row=1, padx=10)

    photo_canvas = Canvas(photo_frame_widget, bg='blue')
    photo_canvas.grid(column=0, row=0)


log_window = Tk()
log_window.title("Split|Crop")
log_window.minsize(270, 200)
log_window.iconbitmap(r"./static/iconDP.ico")
log_window.configure(background='#F5F5DC')

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
password_entry = Entry(text="password", textvariable=password_var, show="*")
password_entry.grid(column=1, row=2, padx=10)

login_user_button = Button(text="Login", command=login)
login_user_button.grid(column=1, row=3, pady=15)

register_user_button = Button(text="Register", command=register)
register_user_button.grid(column=1, row=4)
log_window.mainloop()
