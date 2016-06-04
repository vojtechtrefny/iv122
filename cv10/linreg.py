import matplotlib.pyplot as pyplot
import numpy
import random
import operator

from decimal import Decimal


def read_data(filename):
    data = []

    with open(filename, "r") as f:
        for line in f:
            x, y = line.split()
            data.append((Decimal(x), Decimal(y)))

    return data


def random_data(a, b, mu=0, sigma=0.5):
    data = []

    for x in numpy.arange(0, 10, 0.1):
        y = a * x + b

        rx = x + random.gauss(mu, sigma)
        ry = y + random.gauss(mu, sigma)

        data.append((rx, ry))

    return data


def lin_reg(data, orig=None):
    n = len(data)
    x = [x for x, y in data]
    y = [y for x, y in data]
    xy = [x * y for x, y in data]
    xx = [x**2 for x, y in data]

    a = (n * sum(xy) - sum(x) * sum(y)) / (n * sum(xx) - sum(x)**2)
    b = (sum(xx) * sum(y) - sum(x) * sum(xy) )/ (n * sum(xx) - sum(x)**2)

    # plot the points
    pyplot.plot(x, y, ".")

    # "points" for the line
    x1 = min(x)
    y1 = a * x1 + b
    x2 = max(x)
    y2 = a * x2 + b
    pyplot.plot([x1, x2], [y1, y2], color="red")

    # add "original" line with known a, b
    if orig is not None:
        x1 = min(x)
        y1 = orig[0] * x1 + orig[1]
        x2 = max(x)
        y2 = orig[0] * x2 + orig[1]
        pyplot.plot([x1, x2], [y1, y2], color="green")

    pyplot.show()

    return (a, b)


# data from file
data = read_data("cv10/linreg.txt")
a, b = lin_reg(data)
print("given data (linreg.txt): a: %s, b: %s" % (a, b))

# random data
data = random_data(2, 3)
a, b = lin_reg(data, orig=(2, 3))
print("random data: a: %s, b: %s" % (a, b))
