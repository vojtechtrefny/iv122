from PIL import Image, ImageDraw

import math


def distance(a, b):
    # distance of two points

    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "[%f | %f]" % (self.x, self.y)


class Edge(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def length(self):
        return math.sqrt((self.a.y - self.a.x)**2 + (self.b.y - self.b.y)**2)

    @property
    def center(self):
        return Point((self.a.x + self.b.x) / 2, (self.a.y + self.b.y) / 2)

    def is_in(self, point):
        """ Does the point lies on the edge? """

        return abs(distance(point, self.a) + distance(point, self.b) - distance(self.a, self.b)) <= 0.0000001


class PNG(object):

    def __init__(self, width=400, height=400, img_color=(255, 255, 255, 255)):
        self.width = width
        self.height = height

        self.image = Image.new("RGBA", (self.width, self.height), img_color)

        self.draw = ImageDraw.Draw(self.image)

    def draw_line(self, start, end, color="black", width=1):
        self.draw.line(xy=(start.x, start.y, end.x, end.y), fill=color, width=width)

    def draw_pixel(self, point, color="black"):
        self.draw.point(xy=(point.x, point.y), fill=color)

    def draw_circle(self, center, radius, fill_color="black", outline_color="black"):
        bounds = (center.x - radius, center.y - radius,
                  center.x + radius, center.y + radius)
        self.draw.ellipse(bounds, fill=fill_color, outline=outline_color)

    def draw_rectangle(self, point, size, fill_color="black", outline_color="black"):
        bounds = (point.x, point.y,
                  point.x + size, point.y + size)
        self.draw.rectangle(bounds, fill=fill_color, outline=outline_color)

    def show(self):
        self.image.show()
