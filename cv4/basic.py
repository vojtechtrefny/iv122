from lib import bitmap

import math
import numpy

colors = ["blue", "green", "red", "yellow"]

# circle
def circle(a, b, r, fill=False):

    img = bitmap.PNG()

    for angle in numpy.arange(0, 360, 0.1):
        rangle = math.radians(angle)
        x = r * math.cos(rangle) + a
        y = r * math.sin(rangle) + b
        img.draw_pixel(bitmap.Point(x, y))
        if fill:
            for i in numpy.arange(0, r, 0.1):
                x = i * math.cos(rangle) + a
                y = i * math.sin(rangle) + b
                img.draw_pixel(bitmap.Point(x, y))

    img.show()

# spiral
def spiral(centre_x, centre_y, size, color=False):

    img = bitmap.PNG()

    for angle in numpy.arange(0, 360*size, 0.1):
        rangle = math.radians(angle)

        r = 4 * rangle
        x = r * math.cos(rangle) + centre_x
        y = r * math.sin(rangle) + centre_y

        if color:
            img.draw_pixel(bitmap.Point(x, y), color=colors[int((angle + 45) / 90) % len(colors)])
        else:
            img.draw_pixel(bitmap.Point(x, y))

    img.show()
