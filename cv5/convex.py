from lib import vector

import random


def orientation(p1, p2, p3):
    # http://en.wikipedia.org/wiki/Graham_scan
    # counter-clokwise if > 0
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)


def convex_hull():
    svg = vector.SVG(folder="cv5", name="convex")

    points = []

    for i in range(100):
        point = vector.Point(random.uniform(100, 500), random.uniform(100, 500))
        points.append(point)
        svg.objects.append(point)

    x_sorted = sorted(points, key=lambda point: point.x)

    bottom = []  # bottom half of the hull
    for point in x_sorted:
        while len(bottom) > 1 and orientation(bottom[-2], bottom[-1], point) <= 0:
            bottom.pop()
        bottom.append(point)

    top = []  # top half of the hull
    for point in reversed(x_sorted):
        while len(top) > 1 and orientation(top[-2], top[-1], point) <= 0:
            top.pop()
        top.append(point)

    convex = bottom + top
    for i in range(len(convex) - 1):
        svg.objects.append(vector.Line(convex[i], convex[i + 1]))

    svg.save()

convex_hull()
