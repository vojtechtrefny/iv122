import numpy
import colorsys

from lib import bitmap

znext = lambda z, c : z**2 + c

def julia(x_range=(-1.5, 1.5), y_range=(-1.5, 1.5), resolution=800, color=False):

    # lengths of the intervals (ranges)
    x_length = x_range[1] - x_range[0]
    y_length = y_range[1] - y_range[0]

    # if the range is not 1:1 recalculate 'y-resolution'
    x_resolution = resolution
    y_resolution = int((y_length / x_length) * resolution)

    img = bitmap.PNG(x_resolution, y_resolution)

    # steps for x and y axis so we produce 'enough pixels' to fill the image
    x_step = x_length / x_resolution
    y_step = y_length / y_resolution

    for x in numpy.arange(x_range[0], x_range[1], x_step):
        print(x)
        for y in numpy.arange(y_range[0], y_range[1], y_step):

            c = complex(-0.13, 0.75)
            z = complex(x, y)

            i = 0
            while i < 30:
                z = znext(z, c)

                if abs(z) > 2:
                    break

                i += 1

            # pixel coordinates -- make sure to start with 0 and end with x/y-resoltion
            if x_range[0] <= 0:
                px = (x + abs(x_range[0])) * (x_resolution / x_length)
            else:
                px = (x - abs(x_range[0])) * (x_resolution / x_length)
            if y_range[0] <= 0:
                py = (y + abs(y_range[0])) * (y_resolution / y_length)
            else:
                py = (y - abs(y_range[0])) * (y_resolution / y_length)

            # color or greyscale
            if color:
                hsv_color = (1 - (i / 30), 0.75, 0.75)
                rgb_color = [int(255 * j) for j in colorsys.hsv_to_rgb(*hsv_color)]
            else:
                rgb_color = [255 - i * 10, 255 - i * 10, 255 - i * 10]
            img.draw_pixel(bitmap.Point(px, py), color=(rgb_color[0], rgb_color[1], rgb_color[2]))

    img.show()


julia()
julia(color=True)
julia(x_range=(0.32, 0.34), y_range=(0.33, 0.35))
