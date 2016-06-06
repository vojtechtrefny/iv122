import matplotlib.pyplot as pyplot
import numpy

xnext = lambda x, r: r * x * (1 - x)

def feigenbaum(xstart=0.5, xrange=(0, 1), rrange=(2.4, 4.0)):
    x = xstart

    for i in numpy.arange(rrange[0], rrange[1], 0.005):
        for j in range(200):
            x = xnext(x, i)

            if j > 100 and x >= xrange[0] and x <= xrange[1]:
                pyplot.plot(i, x, ",", color="black")

    pyplot.xlabel("r")
    pyplot.ylabel("x")
    pyplot.show()


feigenbaum()
