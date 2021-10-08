from PIL import Image

work_image = Image.open("crop6.jpg")
# work_image.show()
#
#
width = work_image.size[0]
height = work_image.size[1]
print(width)
print(height)


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


split_to_three(work_image)
split_to_six(work_image)
