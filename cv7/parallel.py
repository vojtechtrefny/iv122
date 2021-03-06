import time
import math
import numpy

from lib import bitmap

roots = [complex(1, 0), complex(-0.5, math.sqrt(3) / 2), complex(-0.5, -math.sqrt(3) / 2)]
znext = lambda z : z - ((z**3 - 1) / (3 * z**2))


def newton_worker(id, x_range, y_range, x_step, y_step, tolerance):
    res = []
    for x in numpy.arange(x_range[0], x_range[1], x_step):
        for y in numpy.arange(y_range[0], y_range[1], y_step):

            z = complex(x, y)
            if z == 0:
                continue

            i = 0
            while i < 100:
                if abs(z - roots[0]) < tolerance:
                    res.append((x, y, 255 - i * 10, 0, 0))
                    break
                elif abs(z - roots[1]) < tolerance:
                    res.append((x, y, 0, 255 - i * 10, 0))
                    break
                elif abs(z - roots[2]) < tolerance:
                    res.append((x, y, 0, 0, 255 - i * 10))
                    break

                i += 1
                z = znext(z)

    with open("res%d" % id, "w") as f:
        for point in res:
            f.write("%f;%f;%d;%d;%d\n" % point)


def newton_main(x_range=(-2, 2), y_range=(-2, 2), resolution=800, tolerance=0.0001, num_workers=4):
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

    workers = []
    files = []
    for i in range(num_workers):
        x_part_range = (x_range[0] + i * (x_length / num_workers), x_range[0] + (i + 1) * (x_length / num_workers))
        p = Process(target=newton_worker, args=(i, x_part_range, y_range, x_step, y_step, tolerance))
        files.append("res%d" % i)
        p.start()
        workers.append(p)

    for worker in workers:
        worker.join()

    for fname in files:
        with open(fname, "r") as f:
            for line in f:
                x, y, color1, color2, color3 = line.split(";")
                x = float(x)
                y = float(y)
                color = (int(color1), int(color2), int(color3))
                if x_range[0] <= 0:
                    px = (x + abs(x_range[0])) * (x_resolution / x_length)
                else:
                    px = (x - abs(x_range[0])) * (x_resolution / x_length)
                if y_range[0] <= 0:
                    py = (y + abs(y_range[0])) * (y_resolution / y_length)
                else:
                    py = (y - abs(y_range[0])) * (y_resolution / y_length)

                img.draw_pixel(bitmap.Point(px, py), color=color)

    img.show()


start_time = time.time()
newton_main(resolution=800, num_workers=2)
end_time = time.time()
print("Time for 2 workers is %f [s]" % (end_time - start_time))
