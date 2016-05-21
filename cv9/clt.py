import random
import math
import matplotlib.pyplot as pyplot


ka = lambda: random.choice([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6])
kb = lambda: random.choice([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6])

def standard_deviation(data):
    mean = sum(data) / len(data)
    return math.sqrt((1 / len(data)) * sum([i**2 for i in data]) - mean**2)


def clt(sample_size=100, samples=10000, strategy="ka"):
    # strategy: [ka, random, random_saples]

    avg = []

    for i in range(samples):
        s = 0

        if strategy == "ka":
            dice = ka
        elif strategy == "random_samples":
            dice = random.choice([ka, kb])

        for j in range(sample_size):
            if strategy == "random":
                dice = random.choice([ka, kb])

            s += dice()

        avg.append(s / sample_size)

    return avg


# only ka dice
res = clt()
mean = sum(res) / 10000
dev = standard_deviation(res)
print("Only Ka dice:\nMean: %f, Standard deviation: %f" % (mean, dev))
pyplot.hist(res, 20)
pyplot.show()

# random dice
res = clt(strategy="random")
mean = sum(res) / 10000
dev = standard_deviation(res)
print("Random dice:\nMean: %f, Standard deviation: %f" % (mean, dev))
pyplot.hist(res, 20)
pyplot.show()

# random dice for sample
res = clt(strategy="random_samples")
mean = sum(res) / 10000
dev = standard_deviation(res)
print("Random dice for sample:\nMean: %f, Standard deviation: %f" % (mean, dev))
pyplot.hist(res, 20)
pyplot.show()
