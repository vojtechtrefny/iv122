import math
import copy

from lib import vector


class _Position(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%d | %d)" % (self.x, self.y)

class Turtle(object):

    def __init__(self, name):

        self.position = _Position(500, 500)  # FIXME -- in vector fix negative coords
        self._write = True

        self.angle = 0
        self.stack = []

        self.svg = vector.SVG(folder="cv3", name=name)

    def forward(self, step, color="black"):
        start = copy.deepcopy(self.position)

        self.position.x += math.cos(math.radians(self.angle)) * step
        self.position.y += math.sin(math.radians(self.angle)) * step

        if self._write:
            self.svg.add_line(start.x, start.y, self.position.x, self.position.y, color)

    def push(self):
        self.stack.append((self.position.x, self.position.y, self.angle))

    def pop(self):
        self.position.x, self.position.y, self.angle = self.stack.pop()

    def back(self, step):
        self.forward(-step)

    def right(self, angle):
        self.angle += angle

    def left(self, angle):
        self.right(-angle)

    def pendown(self):
        self._write = True

    def penup(self):
        self._write = False

    def write_svg(self):
        self.svg.save()

    def reset(self):
        self.position = _Position(100, 100)
        self._write = True
        self.angle = 0
        self.svg.objects = []


def star(vertices):

    t = Turtle(name="star_" + str(vertices))

    for i in range(vertices):
        t.forward(100)
        t.right(180 - (180 / vertices))
        t.forward(100)

    t.write_svg()


def polygon(sides):

    t = Turtle(name="polygon_" + str(sides))

    for i in range(sides):
        t.forward(100)
        t.right(360 / sides)

    t.write_svg()
