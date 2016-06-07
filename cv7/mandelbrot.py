import numpy
import colorsys

from lib import bitmap

znext = lambda z, c : z**2 + c

def mandelbrot(x_range=(-2, 1), y_range=(-1, 1), resolution=800, color=False):

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

    for real in numpy.arange(x_range[0], x_range[1], x_step):
        print(real)
        for imag in numpy.arange(y_range[0], y_range[1], y_step):

            c = complex(real, imag)
            z = complex(0, 0)

            i = 0
            while i < 30:
                z = znext(z, c)

                if abs(z) > 2:
                    break

                i += 1

            # pixel coordinates -- make sure to start with 0 and end with x/y-resoltion
            if x_range[0] <= 0:
                px = (real + abs(x_range[0])) * (x_resolution / x_length)
            else:
                px = (real - abs(x_range[0])) * (x_resolution / x_length)
            if y_range[0] <= 0:
                py = (imag + abs(y_range[0])) * (y_resolution / y_length)
            else:
                py = (imag - abs(y_range[0])) * (y_resolution / y_length)

            # color or greyscale
            if color:
                hsv_color = (1 - (i / 30), 0.75, 0.75)
                rgb_color = [int(255 * j) for j in colorsys.hsv_to_rgb(*hsv_color)]
            else:
                rgb_color = [255 - (i * 10), 255 - (i * 10), 255 - (i * 10)]
            img.draw_pixel(bitmap.Point(px, py), color=(rgb_color[0], rgb_color[1], rgb_color[2]))

    img.show()


mandelbrot()
mandelbrot(color=True)
mandelbrot(x_range=(0.25, 0.45), y_range=(0.45, 0.60), color=True)
