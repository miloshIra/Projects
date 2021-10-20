from tkinter import *
import main
from models import User
from tkinter import filedialog
import time
from PIL import Image, ImageTk


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
    work_window.geometry("530x580")
    work_window.title("Work window")
    work_window.focus_force()
    time.sleep(0.5)
    log_window.withdraw()  # Hides logging window

    def file_browser():
        """Let's you select a file then it resizes and displays it on the canvas"""

        filename = filedialog.askopenfilename(initialdir="Desktop", title="Select photo",
                                              filetypes=(("jpg files", "*.jpg"),
                                                     ("png files", "*.png"),
                                                     ("all files", "*.*")))

        print(filename)
        work_image = Image.open(filename)
        work_image.show()

        image_width = work_image.size[0]
        image_height = work_image.size[1]

        if image_width >= image_height:
            print("Width is bigger")
            image_ratio = image_height/image_width
            while image_width > 500:
                image_width -= 10

            image_width_resize = image_width
            image_height_resize = image_width_resize * image_ratio
            print(image_width_resize, image_height_resize)
            display_image = work_image.resize((round(image_width_resize), round(image_height_resize)))
            background = ImageTk.PhotoImage(display_image)
            # photo_canvas = Canvas(photo_frame_widget)
            # photo_canvas.grid(column=0, row=0)
            photo_canvas.config(width=image_width_resize, height=image_height_resize)
            photo_canvas.create_image(0, 0, image=background, anchor=NW)
            # find_photo_button.grid_forget()
            work_window.geometry(str(round(image_width_resize + 30)) + 'x' + str(round(image_height_resize) + 80))
            find_photo_button.config(show=hide)

        else:
            print("Height is bigger")
            image_ratio = image_width/image_height #/image_width
            while image_height > 500:
                image_height -= 10

            image_height_resize = image_height
            image_width_resize = image_height_resize * image_ratio
            print(image_width_resize, image_height_resize)
            display_image = work_image.resize((round(image_width_resize), round(image_height_resize)))
            background = ImageTk.PhotoImage(display_image)
            # photo_canvas = Canvas(photo_frame_widget)
            # photo_canvas.grid(column=0, row=0)
            photo_canvas.config(width=image_width_resize, height=image_height_resize)
            photo_canvas.create_image(0, 0, image=background, anchor=NW)
            # find_photo_button.grid_forget()
            work_window.geometry(str(round(image_width_resize + 30)) + 'x' + str(round(image_height_resize) + 80))
            find_photo_button.config(show=hide)

        # def split_two():
        #     main.split_to_two(work_image)


    # find_photo_label = Label(work_window, text="Select photo")
    # find_photo_label.grid(column=0, row=0, padx=15, pady=10)

    split_button = Button(work_window, text="Split")
    split_button.grid(column=1, row=0)

    # find_photo_button = Button(work_window, text="Select photo", command=file_browser)
    # find_photo_button.grid(column=1, row=0, padx=15, pady=10)

    find_photo_button = Button(work_window, text="Select photo", command=file_browser)
    find_photo_button.grid(column=0, row=0, padx=15, pady=10)

    photo_frame_widget = LabelFrame(work_window, text="Splitting Image ")
    photo_frame_widget.grid(column=0, row=1, columnspan=3, rowspan=3, padx=10)

    # myCanvas = tkinter.Canvas(root, bg="white", height=300, width=300)
    photo_canvas = Canvas(photo_frame_widget, height=500, width=500)
    photo_canvas.grid(column=0, row=0, columnspan=3, rowspan=3)


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
