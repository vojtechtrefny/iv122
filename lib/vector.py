import os
import math


def distance(a, b):
    # distance of two points

    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)


class Point(object):

    type = "point"

    def __init__(self, x, y, color="black"):
        self.x = x
        self.y = y
        self.color = color

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return abs(self.x - other.x) < 0.00001 and abs(self.y - other.y) < 0.00001

    def __str__(self):
        return '<circle cx="{}" cy="{}" r="2" stroke="{}" stroke-width="3" ' \
               'fill="black" />\n'.format(self.x, self.y, self.color)


class Line(object):

    type = "line"

    def __init__(self, start, end, color="black"):
        self.start = start
        self.end = end
        self.color = color

    def is_in(self, point):
        """ Does the point lies on the line? """

        return abs(distance(point, self.start) + distance(point, self.end) - distance(self.start, self.end)) <= 0.0000001

    @property
    def length(self):
        return abs(distance(self.start, self.end))

    def __str__(self):
        return '<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="{}" ' \
               'stroke-width="1"/>\n'.format(self.start.x, self.start.y,
                                              self.end.x, self.end.y, self.color)


class SVG(object):

    def __init__(self, folder, name):
        self.name = name
        self.folder = folder
        self.objects = []

    def add_line(self, start_x, start_y, end_x, end_y, color="black"):
        line = Line(Point(start_x, start_y),
                    Point(end_x, end_y), color)

        self.objects.append(line)

    def normalize(self):
        """ Make sure we don't have negative coordinates in our svg
        """
        min_x = 0
        min_y = 0

        for obj in self.objects:
            if obj.type == "point":
                points = [obj]
            if obj.type == "line":
                points = [obj.start, obj.end]

            for point in points:
                if point.x < min_x:
                    min_x = point.x
                if point.y < min_y:
                    min_y = point.y

        if min_x < 0 or min_y < 0:
            for obj in self.objects:
                if obj.type == "point":
                    obj.x += abs(min_x)
                    obj.y += abs(min_y)
                if obj.type == "line":
                    obj.start.x += abs(min_x)
                    obj.start.y += abs(min_y)
                    obj.end.x += abs(min_x)
                    obj.end.y += abs(min_y)

    def save(self):
        self.normalize()
        project_folder = os.path.dirname(os.path.realpath(__file__))

        with open(project_folder + '/../' + self.folder + '/' + self.name + '.svg', 'w+') as f:
            f.write('<svg xmlns="http://www.w3.org/2000/svg">\n')

            for obj in self.objects:
                f.write(str(obj))

            f.write('</svg>\n')

    def show(self):
        pass
