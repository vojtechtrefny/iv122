import random
import math

from lib import vector


class Cell(object):

    def __init__(self, x, y, maze_size):
        self.x = x
        self.y = y
        self.maze_size = maze_size

        self.walls = {"top": True, "bottom": True, "right-upper": True, "right-lower": True,
                      "left-upper": True, "left-lower": True}

        self.visited = False

    def neighbours(self):
        """ neighbours of this cell (just coordinates) """

        cells = []

        # easy part -- top and bottom
        if self.y != 0:
            cells.append((self.x , self.y - 1))
        if self.y != self.maze_size - 1:
            cells.append((self.x, self.y + 1))

        # even cells
        if self.x % 2 == 0:
            if self.y != 0:
                if self.x != 0:
                    cells.append((self.x - 1, self.y - 1))  # left upper
                if self.x != self.maze_size - 1:
                    cells.append((self.x + 1, self.y - 1))  # right upper

            # add lower neighbours (if not on the side)
            if self.x != 0:
                cells.append((self.x - 1, self.y))  # left lower
            if self.x != self.maze_size - 1:
                cells.append((self.x + 1, self.y))  # right lower
        else:
            # add upper neighbours (if not on the side)
            if self.x != 0:
                cells.append((self.x - 1, self.y))  # left upper
            if self.x != self.maze_size - 1:
                cells.append((self.x + 1, self.y))  # right upper

            if self.y != self.maze_size - 1:
                if self.x != 0:
                    cells.append((self.x - 1, self.y))  # left lower
                if self.x != self.maze_size - 1:
                    cells.append((self.x + 1, self.y))  # right lower

        return cells


class Maze(object):

    seg_size = 50  # size of cell side in px

    def __init__(self, size=8):
        self.size = size

        self.maze = {}

        for i in range(size):
            for j in range(size):
                self.maze[(i, j)] = Cell(i, j, self.size)

        # select a random starting cell
        starting_cell = random.choice(list(self.maze.values()))
        self._random_dfs(starting_cell, [])

    def _reset_visited(self):
        """ Set all cells as unvisited """

        for cell in self.maze.values():
            cell.visited = False

    def _get_neighbours(self, cell):
        """ Get neighbour cells of cell """

        neighbours = cell.neighbours()
        return [self.maze[coord] for coord in neighbours]  # Cell.neighbours() returns coordinates not Cell

    def _break_wall(self, cell1, cell2):
        """ Break wall between 2 cells """

        # easy situation -- top-bottom neighbours
        if cell1.x == cell2.x and cell1.y == cell2.y - 1:
            cell1.walls["bottom"] = False
            cell2.walls["top"] = False
        elif cell1.x == cell2.x and cell1.y == cell2.y + 1:
            cell1.walls["top"] = False
            cell2.walls["bottom"] = False

        if cell1.x % 2 != 0:  # switch cells, so we have just one situation
            pom = cell1
            cell1 = cell2
            cell2 = pom

        # worst situation -- right-left neighbours
        if cell1.x + 1 == cell2.x and cell1.y == cell2.y:
            cell1.walls["right-lower"] = False
            cell2.walls["left-upper"] = False
        elif cell1.x + 1 == cell2.x and cell1.y - 1 == cell2.y:
             cell1.walls["right-upper"] = False
             cell2.walls["left-lower"] = False
        elif cell1.x -1 == cell2.x and cell1.y == cell2.y:
            cell1.walls["left-lower"] = False
            cell2.walls["right-upper"] = False
        elif cell1.x -1 == cell2.x and cell1.y - 1 == cell2.y:
            cell1.walls["left-upper"] = False
            cell2.walls["right-lower"] = False

    def _random_dfs(self, start, discovered):
        # https://en.wikipedia.org/wiki/Maze_generation_algorithm#Depth-first_search
        discovered.append(start)
        start.visited = True

        while discovered:
            start = discovered[-1]
            neighbours = self._get_neighbours(start)
            unvisited = [n for n in neighbours if not n.visited]

            if not unvisited:
                # no unvisited neighbours, get step back
                if not discovered:
                    return
                else:
                    discovered.pop()
                    continue

            next_cell = random.choice(unvisited)
            self._break_wall(start, next_cell)
            next_cell.visited = True
            discovered.append(next_cell)

    def save_svg(self):
        svg = vector.SVG(folder="cv12", name="maze_%d" % self.size)

        hex_height = self.seg_size * math.sin(math.radians(60))

        for cell in self.maze.values():
            points = []
            if cell.x % 2 == 0:
                for i in range(6):
                    points.append((self.seg_size * math.cos(2 * math.pi * i / 6) + self.seg_size + (1.5 * cell.x * self.seg_size),
                                   self.seg_size * math.sin(2 * math.pi * i / 6) + hex_height + 2 * hex_height * cell.y))
            else:
                for i in range(6):
                    points.append((self.seg_size * math.cos(2 * math.pi * i / 6) + self.seg_size + (1.5 * cell.x * self.seg_size),
                                   self.seg_size * math.sin(2 * math.pi * i / 6) + hex_height + hex_height + (2 * cell.y * hex_height)))

            if cell.walls["right-lower"]:
                svg.add_line(points[0][0], points[0][1], points[1][0], points[1][1])
            if cell.walls["bottom"]:
                svg.add_line(points[1][0], points[1][1], points[2][0], points[2][1])
            if cell.walls["left-lower"]:
                svg.add_line(points[2][0], points[2][1], points[3][0], points[3][1])
            if cell.walls["left-upper"]:
                svg.add_line(points[3][0], points[3][1], points[4][0], points[4][1])
            if cell.walls["top"]:
                svg.add_line(points[4][0], points[4][1], points[5][0], points[5][1])
            if cell.walls["right-upper"]:
                svg.add_line(points[5][0], points[5][1], points[0][0], points[0][1])

            if cell.x == 0 and cell.y == 0:
                svg.objects.append(vector.Point(points[0][0] - self.seg_size, points[0][1], color="green"))
            if cell.x == self.size - 1 and cell.y == self.size - 1:
                svg.objects.append(vector.Point(points[0][0] - self.seg_size, points[0][1], color="red"))


        svg.save()


maze = Maze(10)
maze.save_svg()
