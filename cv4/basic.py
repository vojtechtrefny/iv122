from lib import bitmap

import math
import numpy

colors = ["blue", "green", "red", "yellow"]

def circle(a, b, r, fill=False):
    """ Draw a circle using pixels

        :param a (int): x coordinate for circle center
        :param b (int): y coordinate for circle center
        :param r (int): radius of the circle
        :param fill (bool): should be the circle filled

    """

    img = bitmap.PNG()

    for angle in numpy.arange(0, 360, 0.1):
        rangle = math.radians(angle)
        x = r * math.cos(rangle)
        y = r * math.sin(rangle)
        img.draw_pixel(bitmap.Point(x + a, y + b))
        if fill:
            for i in numpy.arange(0, r, 0.1):
                x = i * math.cos(rangle)
                y = i * math.sin(rangle)
                img.draw_pixel(bitmap.Point(x + a, y + b))

    img.show()


def spiral(a, b, size, color=False):
    """ Draw a spiral using pixels

        :param a (int): x coordinate for spiral start
        :param b (int): y coordinate for spiral start
        :param size (int): size of the spiral
        :param color (bool): should be the spiral colored

    """

    img = bitmap.PNG()

    for angle in numpy.arange(0, 360*size, 0.1):
        rangle = math.radians(angle)

        r = 4 * rangle
        x = r * math.cos(rangle) + a
        y = r * math.sin(rangle) + b

        if color:
            img.draw_pixel(bitmap.Point(x, y), color=colors[int((angle + 45) / 90) % len(colors)])
        else:
            img.draw_pixel(bitmap.Point(x, y))

    img.show()


def ellipse(a, b, rotate=0, fade=False):
    """ Draw an ellipse using pixels

        :param a (int): major axis
        :param b (int): minor axis
        :param fade (bool): should the color of the ellipse fade

    """

    img = bitmap.PNG()

    for angle in numpy.arange(0, 360, 0.1):
        rangle = math.radians(angle)

        for i in numpy.arange(0, 255):
            # (0,0,0) -> (255,255,255) greyscale
            # => 255 ellipse rings each smaller with darker colour

            x = (a * i/255) * math.cos(rangle)
            y = (b * i/255) * math.sin(rangle)

            if rotate:
                rrotate = math.radians(rotate)
                x = x * math.cos(rrotate) - y * math.sin(rrotate)
                y = x * math.sin(rrotate) + y * math.cos(rrotate)

            if fade:
                img.draw_pixel(bitmap.Point(x + 200, y + 200), color=(i, i, i))  # + 200 for image center
            else:
                img.draw_pixel(bitmap.Point(x + 200, y + 200))

    img.show()
