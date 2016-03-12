import math


class Fraction(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "%d / %d = %f" % (self.a, self.b, self.a / self.b)


def simple_exp(x, n):
    """ Simple exponentiation, where n is a natural number """

    res = 1
    # exponentiation to n
    for i in range(n):
        res *= x

    return res


def bisection_exp(x, y, precision=4):

    exp = simple_exp(x, y.a)

    # y.b-th root will be between 1 and x^(y.a)
    bounds = [1, exp]

    steps = 0
    while True:
        guess = sum(bounds) / 2

        exp_guess = simple_exp(guess, y.b)

        # check if guess^(y.b) is close enough to exp
        if abs(exp_guess - exp) < 1 / (simple_exp(10, precision)):
            return (steps, guess)

        # change the bisection interval
        if exp_guess < exp:
            bounds[0] = guess
        else:
            bounds[1] = guess

        steps += 1


def newton_exp(x, y, precision=4):
    exp = simple_exp(x, y.a)

    # y.b-th root will be around x^(y.a) / y.b
    x_0 = exp / y.b

    steps = 0
    while True:
        x_1 = x_0 - (x_0 / y.b) + exp / (y.b * simple_exp(x_0, y.b - 1))

        # check if x_1^(y.b) is close enough to exp
        if abs(simple_exp(x_1, y.b) - exp) < 1 / (simple_exp(10, precision)):
            return (steps, x_1)

        x_0 = x_1
        steps += 1
