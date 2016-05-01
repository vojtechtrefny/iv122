from PIL import Image

from operator import xor


def hidden_1():
    image = Image.open("cv4/skryvacka1.png")

    for x in range(image.width ):
        for y in range(image.height):
            pixel = image.getpixel((x, y))
            new_pixel = (pixel[0], pixel[1], pixel[2] * 100)  # enhance blue part
            image.putpixel((x, y), new_pixel)

    image.show()


def hidden_2():
    image = Image.open("cv4/skryvacka2.png")
    new_image = Image.open("cv4/skryvacka2.png")

    for x in range(image.width - 1):
        for y in range(image.height):

            current_pixel = image.getpixel((x, y))
            next_pixel = image.getpixel((x + 1, y))

            # relative luminance from RGB -- https://en.wikipedia.org/wiki/Relative_luminance
            brightness_diff = abs(0.2126 * current_pixel[0] + 0.7152 * current_pixel[1] + 0.0722 * current_pixel[3] -
                                  0.2126 * next_pixel[0] - 0.7152 * next_pixel[1] - 0.0722 * next_pixel[3])

            # check if the brightness difference between current and next pixel
            # if the difference is too high, draw black pixel
            if brightness_diff > 0.5:
                new_pixel = (0, 0, 0)
                new_image.putpixel((x, y), new_pixel)

    new_image.show()


def hidden_3():
    image = Image.open("cv4/skryvacka3.png")

    black = 0
    white = 255

    for x in range(image.width - 1):
        for y in range(image.height):

            pixel = image.getpixel((x, y))

            # xor with 1px black/white grid
            if x % 2 == 0 and y % 2 == 0:
                new_pixel = (xor(pixel[0], black), xor(pixel[1], black),
                             xor(pixel[2], black))
            else:
                new_pixel = (xor(pixel[0], white), xor(pixel[1], white),
                             xor(pixel[2], white))
            image.putpixel((x, y), new_pixel)

    image.show()
