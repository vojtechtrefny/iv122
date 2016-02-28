import matplotlib.pyplot as pyplot

def nsd(a, b):
    steps = 0
    while b > 0:
        c = a % b
        a = b
        b = c
        steps += 1

    return steps

# ---------------------------------------------------------------------------- #
# pocet kroku nsd

colors = ["b", "c", "g", "y", "m", "r", "k"]

def get_color(num, max_steps):
    # set color based on number of steps and maximum number of steps
    for i in range(6):  # 6 colours
        if num <= ((i + 1) * max_steps) // 6:
            return colors[i]

max_num = 100  # limit for nsd count
data = []

for i in range(max_num):
    for j in range(max_num):
        data.append(((i+1, j+1), nsd(i+1, j+1)))

max_steps = max([d[1] for d in data])  # maximum steps to count nsd

pyplot.axis("off")
pyplot.xlim([-1, max_num+1])
pyplot.ylim([-1, max_num+1])

for d in data:
    color = get_color(d[1], max_steps)
    pyplot.plot([d[0][0]], [d[0][1]], color + "o")

pyplot.show()
