import random

from lib import vector


class Cell(object):

    def __init__(self, x, y, maze_size):
        self.x = x
        self.y = y
        self.maze_size = maze_size

        # walls -- top, right, bottom, left
        self.walls = {"top": True, "right": True, "bottom": True, "left": True}

        self.visited = False

    def neighbours(self):
        """ neighbours of this cell (just coordinates) """

        cells = []

        if self.x != 0:
            cells.append((self.x - 1, self.y))
        if self.x != self.maze_size - 1:
            cells.append((self.x + 1, self.y))
        if self.y != 0:
            cells.append((self.x, self.y - 1))
        if self.y != self.maze_size - 1:
            cells.append((self.x, self.y + 1))

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
        """ Get neighbout cells of cell """

        neighbours = cell.neighbours()
        return [self.maze[coord] for coord in neighbours]  # Cell.neighbours() returns coordinates not Cell

    def _break_wall(self, cell1, cell2):
        """ Break wall between 2 cells """

        print("breaking wall between %d|%d and %d|%d" % (cell1.x, cell1.y, cell2.x, cell2.y))

        if cell1.x == cell2.x - 1:
            cell1.walls["right"] = False
            cell2.walls["left"] = False
        elif cell1.x == cell2.x + 1:
            cell1.walls["left"] = False
            cell2.walls["right"] = False
        elif cell1.y == cell2.y - 1:
            cell1.walls["bottom"] = False
            cell2.walls["top"] = False
        elif cell1.y == cell2.y + 1:
            cell1.walls["top"] = False
            cell2.walls["bottom"] = False

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


    def _get_reachable(self):
        """ Is finish still reachable?"""  # TODO: probably all cells should be reachable -- kontrolovat souvislost: https://cs.wikipedia.org/wiki/Souvisl%C3%BD_graf

        discovered = self._dfs(self.maze[(0, 0)])
        return self.maze[(size - 1, size - 1)] in discovered

    def save_svg(self):
        svg = vector.SVG(folder="cv12", name="maze_%d" % self.size)

        for cell in self.maze.values():
            if cell.walls["top"]:
                svg.add_line((cell.x * self.seg_size), (cell.y * self.seg_size),
                             (cell.x * self.seg_size) + self.seg_size, (cell.y * self.seg_size))
            if cell.walls["right"]:
                svg.add_line((cell.x * self.seg_size) + self.seg_size, (cell.y * self.seg_size),
                             (cell.x * self.seg_size) + self.seg_size, (cell.y * self.seg_size) + self.seg_size)
            if cell.walls["bottom"]:
                svg.add_line((cell.x * self.seg_size) + self.seg_size, (cell.y * self.seg_size) + self.seg_size,
                             (cell.x * self.seg_size), (cell.y * self.seg_size) + self.seg_size)
            if cell.walls["left"]:
                svg.add_line((cell.x * self.seg_size), (cell.y * self.seg_size) + self.seg_size,
                             (cell.x * self.seg_size), (cell.y * self.seg_size))

        svg.save()


maze = Maze()
maze.save_svg()
