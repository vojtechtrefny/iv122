import math

from lib import vector
from cv3.turtle import Turtle

def pentagram_turtle():

    t = Turtle(name="pentagram1")

    for i in range(5):
        t.forward(100)
        t.right(72)

    diagonal = 2 * math.cos(math.radians(36)) * 100

    t.right(36)
    t.forward(diagonal)

    for i in range(4):
        t.left(36)
        t.left(180)
        t.forward(diagonal)

    t.write_svg()


def pentagram_lines():
    svg = vector.SVG(folder="cv3", name="pentagram2")

    points = []

    # calculate point coordinates, +100 is padding to make sure there are no
    # negative coordinates because these doesn't work with svg
    for i in range(5):
        points.append((100 * math.cos(2 * math.pi * i / 5) + 100,
                       100 * math.sin(2 * math.pi * i / 5) + 100))

    # connect all points
    for i in points:
        for j in points:
            svg.add_line(i[0], i[1], j[0], j[1])

    svg.save()


def rectangles_turtle():

    t = Turtle(name="rectangles")

    a = 300  # square side
    angle = 15  # inner angle
    rangle = math.radians(angle)

    for j in range(15):
        for i in range(4):
            t.forward(a)
            t.right(90)

        # move to the start point of the next square
        x = a * math.tan(rangle) / (1 + math.tan(rangle))
        t.penup()
        t.forward(x)
        t.pendown()
        t.right(angle)

        # side lenght of the new square
        a = (a - x) / math.cos(rangle)

    t.write_svg()


def circle_lines():
    svg = vector.SVG(folder="cv3", name="circle")

    d = 200

    # "center" lines
    svg.add_line(100, 0, 100, 200)
    svg.add_line(0, 100, 200, 100)

    for i in range(5, 100, 5):
        lenght = math.sqrt(d**2 / 4 - i**2)  # lenght of the line to draw
        svg.add_line(100 - i, d / 2 - lenght, 100 - i, d / 2 + lenght)  # left part
        svg.add_line(100 + i, d / 2 - lenght, 100 + i, d / 2 + lenght)  # right part
        svg.add_line(d / 2 - lenght, 100 - i, d / 2 + lenght, 100 - i)  # top part
        svg.add_line(d / 2 - lenght, 100 + i, d / 2 + lenght, 100 + i)  # bottom part

    svg.save()

circle_lines()


def triangles_turtle():

    t = Turtle(name="triangles")

    # first (outer) tringle
    for i in range(3):
        t.forward(100)
        t.left(120)

    for i in range(5):
        # stop drawing and move "up and right"
        t.penup()
        t.forward(10)
        t.left(90)
        t.forward(5)
        t.right(90)
        t.pendown()

        # draw "smaller" triangles
        for j in range(3):
            t.forward(100 - (i + 1) * 20)
            t.left(120)

    t.write_svg()
