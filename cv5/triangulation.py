import random

from lib import vector


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
        # two ends touchig --> no intersection in this case
        if (p == line1.start or p == line1.end) and (p == line2.start or p == line2.end):
            return None
        else:
            return p
    else:
        return None


def triangulation():

    svg = vector.SVG(folder="cv5", name="triangulation")

    # random points
    points = []
    for i in range(50):
        point = vector.Point(random.uniform(100, 500), random.uniform(100, 500))
        points.append(point)
        svg.objects.append(point)

    # all lines
    lines = []
    for point1 in points:
        for point2 in points:
            if point1 == point2:
                continue
            lines.append(vector.Line(point1, point2))

    # sort lines by lenght
    lines = sorted(lines, key=lambda line: line.length)

    triang_lines = []
    for candidate in lines:
        add = True
        for line in triang_lines:
            if get_intersection(line, candidate):
                add = False  # intersection with some line in triangulation --> do not add
                break
        if add:
            triang_lines.append(candidate)

    for line in triang_lines:
        svg.objects.append(line)

    svg.save()
