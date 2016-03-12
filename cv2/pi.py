import math
import random

def archimedes(sides=96):
    angle = 2 * math.pi / sides
    inner = math.sin(angle / 2) * sides
    outer = math.tan(angle / 2) * sides

    return (inner + outer) / 2

def gregory_leibnitz(n=1000):
    pi = 0

    for i in range(n):
        pi += (-1)**i / (2*i + 1)

    pi *= 4

    return pi


def gauss_legendre(n=1000):
    pi = 0

    a_0 = 1
    b_0 = 1 / math.sqrt(2)
    t_0 = 1 / 4
    p_0 = 1

    for i in range(n):
        a_1 = (a_0 + b_0) / 2
        b_1 = math.sqrt(a_0 * b_0)
        t_1 = t_0 - p_0 * (a_0 - a_1)**2
        p_1 = 2*p_0

        a_0 = a_1
        b_0 = b_1
        t_0 = t_1
        p_0 = p_1

    pi = (a_0 + b_0)**2 / (4*t_0)

    return pi


def monte_carlo(n=1000):
    inside = 0

    for i in range(n):
        x,y = (random.random(), random.random())

        if math.sqrt(x**2 + y**2) <= 1:   # does the needle landed inside the circle?
            inside += 1

    return 4 * inside / n
