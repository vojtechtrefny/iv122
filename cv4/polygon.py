from lib import bitmap

from matplotlib import path as mp
import numpy


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
        path = mp.Path(numpy.array([(v.x, v.y) for v in self.vertices]))
        return path.contains_point((point.x, point.y))

    def draw(self):
        x_0 = min([v.x for v in self.vertices])
        x_1 = max([v.x for v in self.vertices])

        y_0 = min([v.y for v in self.vertices])
        y_1 = max([v.y for v in self.vertices])

        img = bitmap.PNG()

        for i in numpy.arange(x_0, x_1, 0.1):
            for j in numpy.arange(y_0, y_1, 0.1):
                p = bitmap.Point(i, j)
                if self.is_in(p):
                    img.draw_pixel(p)

        img.show()


polygon = Polygon([bitmap.Point(10, 10), bitmap.Point(180, 20), bitmap.Point(160, 150),
                   bitmap.Point(100, 50), bitmap.Point(20, 180)])
polygon.draw()
