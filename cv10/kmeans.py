import matplotlib.pyplot as pyplot
import random
import sys
import math

from decimal import Decimal


def distance(a, b):
    # distance of two points

    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)


def get_center(points):
    # center of cluster

    x = sum(p[0] for p in points) / len(points)
    y = sum(p[1] for p in points) / len(points)

    return (x, y)


def normalize(points):
    # normalize data so both axes are between 0 and 1

    x_max = max(p[0] for p in points)
    y_max = max(p[1] for p in points)

    return [(p[0] / x_max, p[1] / y_max) for p in points]


def read_data(filename):
    data = []

    with open(filename, "r") as f:
        for line in f:
            x, y = line.split()
            data.append((Decimal(x), Decimal(y)))

    return data


def random_data(num_clusters):

    points = []

    # centers as vertices of regular polygon
    centers = [(math.cos(2 * math.pi * i / num_clusters), math.sin(2 * math.pi * i / num_clusters)) for i in range(num_clusters)]

    for center in centers:
        for i in range(20):
            rx = center[0] + random.gauss(0, 0.2)
            ry = center[1] + random.gauss(0, 0.2)
            points.append((rx, ry))

    random.shuffle(points)
    return points


def kmeans(points, num_clusters, iterations):

    # 'random' starting points
    centers = points[:num_clusters]

    for i in range(iterations):
        # create 'list' of clusters (actually a dict with centers as keys and points as values)
        clusters = {c : [] for c in centers}

        for point in points:
            min_center = None
            min_dist = sys.maxsize
            for center in centers:
                dist = distance(point, center)
                if dist < min_dist:
                    min_dist = dist
                    min_center = center

            clusters[min_center].append(point)

        centers = [get_center(cluster) for cluster in clusters.values()]

    colors = iter(["red", "blue", "yellow", "green", "orange", "grey", "teal", "purple"])
    for cluster in clusters.keys():
        pyplot.plot(cluster[0], cluster[1], "o", color="black")
        pyplot.plot([p[0] for p in clusters[cluster]], [p[1] for p in clusters[cluster]], ".", color=next(colors))

    pyplot.show()

# data from file
data = read_data("cv10/faithful.txt")
kmeans(normalize(data), 2, 10)

# random data
data = random_data(5)
kmeans(data, 5, 10)
