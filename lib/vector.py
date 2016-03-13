import os


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '<circle cx="{}" cy="{}" r="2" stroke="black" stroke-width="3" ' \
               'fill="black" />\n'.format(self.x, self.y)


class Line(object):

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return '<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="black" ' \
               'stroke-width="1"/>\n'.format(self.start.x, self.start.y,
                                              self.end.x, self.end.y)


class SVG(object):

    def __init__(self, folder, name):
        self.name = name
        self.folder = folder
        self.objects = []

    def add_line(self, start_x, start_y, end_x, end_y):
        line = Line(Point(start_x, start_y),
                    Point(end_x, end_y))

        self.objects.append(line)

    def save(self):
        project_folder = os.path.dirname(os.path.realpath(__file__))

        with open(project_folder + '/../' + self.folder + '/' + self.name + '.svg', 'w+') as f:
            f.write('<svg xmlns="http://www.w3.org/2000/svg">\n')

            for obj in self.objects:
                f.write(str(obj))

            f.write('</svg>\n')

    def show(self):
        pass
