import math
import numpy
import time

from lib import bitmap

roots = [complex(1, 0), complex(-0.5, math.sqrt(3) / 2), complex(-0.5, -math.sqrt(3) / 2)]
znext = lambda z : z - ((z**3 - 1) / (3 * z**2))


def newton(x_range=(-2, 2), y_range=(-2, 2), resolution=800, tolerance=0.0001, timing=False):

    # lengths of the intervals (ranges)
    x_length = x_range[1] - x_range[0]
    y_length = y_range[1] - y_range[0]

    # if the range is not 1:1 recalculate 'y-resolution'
    x_resolution = resolution
    y_resolution = int((y_length / x_length) * resolution)

    img = bitmap.PNG(x_resolution, y_resolution, img_color=(0, 0, 0))

    # steps for x and y axis so we produce 'enough pixels' to fill the image
    x_step = x_length / x_resolution
    y_step = y_length / y_resolution

    for x in numpy.arange(x_range[0], x_range[1], x_step):
        for y in numpy.arange(y_range[0], y_range[1], y_step):

            z = complex(x, y)
            if z == 0:
                continue

            i = 0
            while i < 100:
                # pixel coordinates -- make sure to start with 0 and end with x/y-resoltion
                if x_range[0] <= 0:
                    px = (x + abs(x_range[0])) * (x_resolution / x_length)
                else:
                    px = (x - abs(x_range[0])) * (x_resolution / x_length)
                if y_range[0] <= 0:
                    py = (y + abs(y_range[0])) * (y_resolution / y_length)
                else:
                    py = (y - abs(y_range[0])) * (y_resolution / y_length)

                if abs(z - roots[0]) < tolerance:
                    img.draw_pixel(bitmap.Point(px, py), color=(255 - i * 10, 0, 0))
                    break
                elif abs(z - roots[1]) < tolerance:
                    img.draw_pixel(bitmap.Point(px, py), color=(0, 255 - i * 10, 0))
                    break
                elif abs(z - roots[2]) < tolerance:
                    img.draw_pixel(bitmap.Point(px, py), color=(0, 0, 255 - i * 10))
                    break

                z = znext(z)
                i += 1

    # do not show image when measuring time
    if not timing:
        img.show()


start_time = time.time()
newton(resolution=800, timing=True)
end_time = time.time()
print("Time for not parallel function is %f [s]" % (end_time - start_time))

newton()
newton(x_range=(-0.5, 0.5), y_range=(-0.5, 0.5))
