from lib import vector

import random
import math


def get_intersection(line1, line2):
    # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line
    x1 = line1.start.x; y1 = line1.start.y
    x2 = line1.end.x; y2 = line1.end.y
    x3 = line2.start.x; y3 = line2.start.y
    x4 = line2.end.x; y4 = line2.end.y

    # no intersection
    if (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4) == 0:
        return None

    p1 = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    p2 = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

    p = vector.Point(p1, p2)

    # is our intersection on both edges?
    if line1.is_in(p) and line2.is_in(p):
        return p
    else:
        return None


def intersections():
    lines = []
    svg = vector.SVG(folder="cv5", name="intersections")
    lenght = 500

    for i in range(50):
        a = vector.Point(random.uniform(500, 1000), random.uniform(500, 1000))  # random start point
        rangle = math.radians(random.uniform(0, 360))  # random angle
        b = vector.Point(a.x + lenght * math.cos(rangle), a.y + lenght * math.sin(rangle))

        line = vector.Line(a, b)
        lines.append(line)
        svg.objects.append(line)

    for line1 in lines:

        for line2 in lines:
            if line1 == line2:
                continue

            intersection = get_intersection(line1, line2)
            if intersection is not None:
                svg.objects.append(intersection)

    svg.save()


intersections()
