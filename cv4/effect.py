from lib import bitmap

import math

def grid():
    img = bitmap.PNG()

    pixels = []

    grid_size = 20
    img_size = 220

    # grid
    for i in range(img_size):
        for j in range(img_size):
            if (i // grid_size) % 2 == (j // grid_size) % 2:
                pixels.append([i, j, False])  # False for black
            else:
                pixels.append([i, j, True])  # True for white

    center = (img_size // 2, img_size // 2)

    # create circles and invert grid color inside them
    for radius in (45, 85, 125):
        for pixel in pixels:
            # if pixel is in the circle, change its color
            if math.sqrt((pixel[0] - center[0])**2 + (pixel[1] - center[1])**2) <= radius:
                pixel[2] = not pixel[2]

    # draw the pisels
    for pixel in pixels:
        if pixel[2]:
            color = "white"
        else:
            color = "black"
        img.draw_pixel(bitmap.Point(pixel[0], pixel[1]), color=color)

    img.show()
