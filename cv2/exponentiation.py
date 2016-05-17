import math
import random
import time
import decimal

from collections import namedtuple
import matplotlib.pyplot as pyplot

decimal.getcontext().prec = 100

class Fraction(object):

    def __init__(self, a, b):
        self.a = decimal.Decimal(a)
        self.b = decimal.Decimal(b)

    def __str__(self):
        return "%d / %d = %f" % (self.a, self.b, self.a / self.b)


def simple_exp(x, n):
    """ Simple exponentiation, where n is a natural number """

    res = 1
    # exponentiation to n
    for i in range(int(n)):
        res *= x

    return res


def bisection_exp(x, y, precision=0.00001):
    x = decimal.Decimal(x)
    exp = simple_exp(x, y.a)

    # y.b-th root will be between 1 and x^(y.a)
    bounds = [1, exp]

    steps = 0
    while True:
        guess = sum(bounds) / 2

        exp_guess = simple_exp(guess, y.b)

        # check if guess^(y.b) is close enough to exp
        if abs(exp_guess - exp) <= precision:
            return (steps, guess)

        # change the bisection interval
        if exp_guess < exp:
            bounds[0] = guess
        else:
            bounds[1] = guess

        steps += 1


def newton_exp(x, y, precision=decimal.Decimal(0.00001)):
    x = decimal.Decimal(x)

    exp = simple_exp(x, y.a)
    x_0 = x

    steps = 0
    while True:
        x_1 = x_0 - (simple_exp(x_0, y.b) - exp) / (y.b * simple_exp(x_0, y.b - 1))

        # check if x_1^(y.b) is close enough to exp, or if bounds are too close
        if abs(simple_exp(x_1, y.b) - exp) < precision:
            return (steps, x_1)

        x_0 = x_1
        steps += 1


Result = namedtuple("Result", ["base", "exp", "bisection", "newton"])


def steps_test():
    results = []

    for i in range(100):
        print(i)
        base = random.randint(1, 100)
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        exp = Fraction(a, b)

        res1 = bisection_exp(base, exp, 0.0000000001)
        res2 = newton_exp(base, exp, 0.0000000001)

        results.append(Result(base=base, exp=exp, bisection=res1[0], newton=res2[0]))

    exps = [str(r.base) + "^" + str(r.exp.a) + "/" + str(r.exp.b) for r in results]
    newton = [r.newton for r in results]
    bisection = [r.bisection for r in results]

    pyplot.xticks(range(len(exps)), exps, rotation="vertical")
    pyplot.plot(range(len(exps)), bisection, "r.")
    pyplot.plot(range(len(exps)), newton, "g.")
    pyplot.show()
