from decimal import Decimal


def formula():
    data = []

    with open("cv10/linreg.txt", "r") as f:
        for line in f:
            x, y = line.split()
            data.append((Decimal(x), Decimal(y)))

    n = len(data)
    x = [x for x, y in data]
    y = [y for x, y in data]
    xy = [x * y for x, y in data]
    xx = [x**2 for x, y in data]

    a = (sum(xx) * sum(y) - sum(x) * sum(xy) )/ (n * sum(xx) - sum(x)**2)
    b = (n * sum(xy) - sum(x) * sum(y)) / (n * sum(xx) - sum(x)**2)

    print(a, b)


def force():
    data = []

    with open("cv10/linreg.txt", "r") as f:
        for line in f:
            x, y = line.split()
            data.append((Decimal(x), Decimal(y)))

    min_squares = None

    for point1 in data:
        for point2 in data:
