from lib import bitmap

from matplotlib import path as mp
import numpy


def distance(a, b):
    # distance of two points

    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)


class Polygon(object):

    def __init__(self, vertices):

        self.vertices = vertices

        if len(self.vertices) < 3:
            raise ValueError("Need at least three vertices to create a polygon.")

        if not all([isinstance(vertice, bitmap.Point) for vertice in vertices]):
            raise AttributeError("Vertices has to be a list of bimpat.Point.")

        self._edges = None

    @property
    def edges(self):
        if self._edges is None:
            self._edges = []

            for i in range(len(self.vertices) - 1):
                self._edges.append(bitmap.Edge(self.vertices[i], self.vertices[i + 1]))

            self._edges.append(bitmap.Edge(self.vertices[-1], self.vertices[0]))

        return self._edges

    def is_in(self, point):
        # dirty hack to be sure start of the "ray" is always outside of the polygon
        ray = bitmap.Edge(bitmap.Point(-10000, -10000), point)

        intersections = set()  # set for intersections o we don't count polygon vertices as 2 intersections
        for edge in self.edges:
            x1 = ray.a.x; y1 = ray.a.y
            x2 = ray.b.x; y2 = ray.b.y
            x3 = edge.a.x; y3 = edge.a.y
            x4 = edge.b.x; y4 = edge.b.y

            # no intersection
            if (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4) == 0:
                continue

            # intersection -- https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line
            p1 = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
            p2 = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

            p = bitmap.Point(p1, p2)

            # is our intersection both on the edge and on the ray?
            if edge.is_in(p) and ray.is_in(p):
                intersections.add((p1, p2))

        # odd number of intersections --> point is in the polygon
        return not (len(intersections) % 2 == 0)

    def draw(self):
        x_0 = min([v.x for v in self.vertices])
        x_1 = max([v.x for v in self.vertices])

        y_0 = min([v.y for v in self.vertices])
        y_1 = max([v.y for v in self.vertices])

        img = bitmap.PNG()

        for i in numpy.arange(x_0, x_1, 1):
            for j in numpy.arange(y_0, y_1, 1):
                p = bitmap.Point(i, j)
                if self.is_in(p):
                    img.draw_pixel(p)

        img.show()


polygon = Polygon([bitmap.Point(10, 10), bitmap.Point(180, 20), bitmap.Point(160, 150),
                   bitmap.Point(100, 50), bitmap.Point(20, 180)])
polygon.draw()
