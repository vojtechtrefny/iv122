from lib import bitmap

import math
import random


def chaos_game(n=3, p=1/2, iterations=100000, regular=True):

    img = bitmap.PNG(800, 800)

    # regular or random starting points?
    if regular:
        points = [bitmap.Point(400 + 300 * math.cos(2 * math.pi * i / n),  # + 400 is to be sure we don't have negative coordinates
                               400 + 300 * math.sin(2 * math.pi * i / n)) for i in range(1, n + 1)]
    else:
        points = [bitmap.Point(400 + 300 * math.cos(2 * math.pi * random.random()),
                               400 + 300 * math.sin(2 * math.pi * random.random())) for i in range(n)]

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
