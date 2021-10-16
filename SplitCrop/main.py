from PIL import Image
import gui


work_image = Image.open(gui.file_browser.get())
print(work_image)
work_image.show()

width = work_image.size[0]
height = work_image.size[1]
print(width)
print(height)


def split_to_two(image):
    """Divides the photo into two equal parts"""
    # GET LEFT SIDE OF THE IMAGE ###
    left_side_crop = (0, 0, width/2, height)
    print(left_side_crop)
    image_left_side = image.crop(left_side_crop)
    image_left_side.save("left_side.jpg", quality=100)
    image_left_side.show()

    # GET RIGHT SIDE OF THE IMAGE ###
    right_side_crop = (width / 2, 0, width, height)
    print(right_side_crop)
    image_right_side = image.crop(right_side_crop)
    image_right_side.save("right_side.jpg", quality=100)
    image_right_side.show()


def split_to_three(image):
    """Divides the photo into three equal parts"""

    # GET THE LEFT PART OF THE IMAGE ###
    left_crop_image = (0, 0, round(width / 3), height)
    print(left_crop_image)
    image_left = image.crop(left_crop_image)
    image_left.save("cut1.jpg", quality=100)
    image_left.show()

    # GET THE MIDDLE PART OF THE IMAGE ###
    middle_crop_image = (round(width / 3), 0, round(width * 2 / 3), height)
    print(middle_crop_image)
    image_middle = image.crop(middle_crop_image)
    image_middle.save("cut2.jpg", quality=100)
    image_middle.show()

    # GET THE RIGHT PART OF THE IMAGE ###
    right_crop_image = (round(width * 2 / 3), 0, width, height)
    print(right_crop_image)
    image_right = image.crop(right_crop_image)
    image_right.save("cut3.jpg", quality=100)
    image_right.show()


def split_to_six(image):
    """Divides the photo into six equal parts"""

    # GET THE LEFT TOP PART OF THE IMAGE ###
    top_left_crop_image = (0, 0, width / 3, height/2)
    print(top_left_crop_image)
    top_left_image = image.crop(top_left_crop_image)
    top_left_image.save("cut4.jpg", quality=100)
    top_left_image.show()

    # GET THE MIDDLE TOP PART OF THE IMAGE ###
    top_middle_crop_image = (width / 3, 0, width * 2 / 3, height/2)
    print(top_middle_crop_image)
    top_middle_image = image.crop(top_middle_crop_image)
    top_middle_image.save("cut5.jpg", quality=100)
    top_middle_image.show()

    # GET THE RIGHT TOP PART OF THE IMAGE ###
    top_right_crop_image = (width * 2 / 3, 0, width, height/2)
    print(top_right_crop_image)
    top_right_image = image.crop(top_right_crop_image)
    top_right_image.save("cut6.jpg", quality=100)
    top_right_image.show()

    # GET THE LEFT TOP PART OF THE IMAGE ###
    top_left_crop_image = (0, height / 2, width / 3, height)
    print(top_left_crop_image)
    top_left_image = image.crop(top_left_crop_image)
    top_left_image.save("cut7.jpg", quality=100)
    top_left_image.show()

    # GET THE MIDDLE TOP PART OF THE IMAGE ###
    top_middle_crop_image = (round(width / 3), height / 2, round(width * 2 / 3), height)
    print(top_middle_crop_image)
    top_middle_image = image.crop(top_middle_crop_image)
    top_middle_image.save("cut8.jpg", quality=100)
    top_middle_image.show()

    # GET THE RIGHT TOP PART OF THE IMAGE ###
    top_right_crop_image = (round(width * 2 / 3), height / 2, width, height)
    print(top_right_crop_image)
    top_right_image = image.crop(top_right_crop_image)
    top_right_image.save("cut9.jpg", quality=100)
    top_right_image.show()


# split_to_three(work_image)
# split_to_six(work_image)
split_to_two(work_image)


# TODO: 1. Make a GUI(tkinter)
# TODO: 2. Make a database instead of dictionary.
# TODO: 3. Make cross section crops.
# TODO: 4. Kivy is a python mobile framework, kinda sucks tho..
# TODO: 5. Make an end window "after operation is done go to gallery or crop again".

