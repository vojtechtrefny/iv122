import matplotlib.pyplot as pyplot

def collatz(num, rtype):
    i = 0
    m = 0
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3*num + 1

        i += 1
        if num > m:
            m = num

    if rtype == "step":
        return i

    if rtype == "max":
        return m

# ---------------------------------------------------------------------------- #
# pocet kroku

lst = []
for i in range(8000):
    lst.append((i+1, collatz(i+1, rtype="step")))

pyplot.plot([l[0] for l in lst], [l[1]for l in lst], "ko")

pyplot.show()

# ---------------------------------------------------------------------------- #
# maximalni cislo

lst = []
for i in range(8000):
    lst.append((i+1, collatz(i+1, rtype="max")))

pyplot.plot([l[0] for l in lst], [l[1]for l in lst], "ko")

pyplot.show()
