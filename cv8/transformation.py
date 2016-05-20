from lib import vector

import copy

import numpy
import math


def combine(transformations):
    matrix = transformations[0]

    for i in transformations[1:]:
        matrix = i * matrix

    return matrix


def rotate(angle):
    rangle = math.radians(angle)
    matrix = numpy.matrix([[math.cos(rangle), -math.sin(rangle), 0.0],
                           [math.sin(rangle), math.cos(rangle), 0.0],
                           [0.0, 0.0, 1.0]])

    return matrix


def translate(x=0, y=0):
    matrix = numpy.matrix([[1.0, 0.0, x],
                           [0.0, 1.0, y],
                           [0.0, 0.0, 1.0]])

    return matrix


def scale(x=1.0, y=1.0):
    matrix = numpy.matrix([[x, 0.0, 0.0],
                           [0.0, y, 0.0],
                           [0.0, 0.0, 1.0]])

    return matrix


def shear(k=1.0):
    matrix = numpy.matrix([[1.0, k, 0.0],
                           [0.0, 1.0, 0.0],
                           [0.0, 0.0, 1.0]])

    return matrix


def do_it(matrix, lines):
    new_lines = []

    for line in lines:
        start_matrix = numpy.matrix([[line.start.x], [line.start.y], [1]])
        start_res = matrix.dot(start_matrix)

        end_matrix = numpy.matrix([[line.end.x], [line.end.y], [1]])
        end_res = matrix.dot(end_matrix)

        new_lines.append(vector.Line(vector.Point(float(start_res[0]), float(start_res[1])), vector.Point(float(end_res[0]), float(end_res[1]))))

    return new_lines


def square(size=100):
    lines = [vector.Line(vector.Point(0, 0), vector.Point(size, 0)),
             vector.Line(vector.Point(size, 0), vector.Point(size, size)),
             vector.Line(vector.Point(size, size), vector.Point(0, size)),
             vector.Line(vector.Point(0, size), vector.Point(0, 0))]
    return lines


def example1():
    svg = vector.SVG("cv8", "example1")
    matrix = combine([rotate(20), scale(1.1, 1.1), translate(5, 10)])

    obj = square()
    svg.objects.extend(obj)

    for i in range(10):
        obj = do_it(matrix, obj)
        svg.objects.extend(obj)

    svg.save()


def example2():
    svg = vector.SVG("cv8", "example2")
    matrix = combine([rotate(10), scale(1.1, 0.8)])

    obj = square()
    svg.objects.extend(obj)

    for i in range(15):
        obj = do_it(matrix, obj)
        svg.objects.extend(obj)

    svg.save()


def example3():
    svg = vector.SVG("cv8", "example3")
    matrix = combine([shear(1.3), rotate(10), scale(0.9, 0.9), translate(50, 50)])

    obj = square()
    svg.objects.extend(obj)

    for i in range(5):
        obj = do_it(matrix, obj)
        svg.objects.extend(obj)

    svg.save()

example1()
example2()
example3()
