import matplotlib.pyplot as pyplot

def eratos(lim):
    lim += 1
    res = [True for i in range(lim)]

    for i in range(2, lim):
        if res[i]:
            for j in range(i*2, lim, i):
                res[j] = False

    primes = []
    for i in range(2, lim):
        if res[i]:
            primes.append(i)

    return primes


def ulam(width):
    coordinates = []

    n = 1
    x = 0
    y = 0
    i = 1

    while i <= width**2:
        if n % 2 == 1:
            # step right
            coordinates.append((i, (x, y)))
            x += 1
            i += 1

            # n steps down
            for j in range(n):
                coordinates.append((i, (x, y)))
                y -= 1
                i += 1

            # n steps left
            for j in range(n):
                coordinates.append((i, (x, y)))
                x -= 1
                i += 1

        else:
            # step left
            coordinates.append((i, (x, y)))
            x -= 1
            i += 1

            # n steps up
            for j in range(n):
                coordinates.append((i, (x, y)))
                y += 1
                i += 1

            # n steps right
            for j in range(n):
                coordinates.append((i, (x, y)))
                x += 1
                i += 1

        n += 1

    return coordinates

# ---------------------------------------------------------------------------- #
# cisla delitelna 4 v posloupnosti

nums = ulam(300)
to_print = [num[1] for num in nums if num[0] % 4 == 0]

pyplot.axis("off")
pyplot.plot([l[0] for l in to_print], [l[1]for l in to_print], "k,")

pyplot.show()


# ---------------------------------------------------------------------------- #
# prvocisla v posloupnosti

nums = ulam(300)
primes = eratos(100000)
print(primes)
print(nums[-1][0])
to_print = [num[1] for num in nums if num[0] in primes]

pyplot.axis("off")
pyplot.plot([l[0] for l in to_print], [l[1]for l in to_print], "k.")

pyplot.show()
