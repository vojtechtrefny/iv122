from lib import bitmap

import math
import random


def chaos_game(n=3, p=1/2, iterations=100000):

    img = bitmap.PNG(800, 800)

    points = [bitmap.Point(400 + 300 * math.cos(2 * math.pi * i / n),
                           400 + 300 * math.sin(2 * math.pi * i / n)) for i in range(1, n + 1)]

    # draw the initial points
    for i in points:
        img.draw_pixel(i)

    x = bitmap.Point(random.uniform(0, 600), random.uniform(0, 600))

    for i in range(iterations):
        r = points[random.randint(0, len(points) - 1)]
        x = bitmap.Point((x.x + r.x) * p,  (x.y + r.y) * p)

        if i > 100:
            img.draw_pixel(x)

    img.show()
