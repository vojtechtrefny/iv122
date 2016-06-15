import sys
import random

from lib import vector


test_maze = "..#.###.#.#.#.A#.###.####.#..#.#.#..#.B.#.#.##.#."

prizes = {"." : 1,
          "A" : 1,
          "B" : 1,
          "#" : 100}


def read_maze(maze_size, maze_str):
    """ Create a maze as dict of dicts (with neighbours and its 'prizes') from
        given string (see 'test_maze'). Also finds start and end point.
    """

    # create a list of lists (maze_size lenght) from the string
    maze_iter = iter(maze_str)
    maze_list = [[next(maze_iter) for i in range(maze_size)] for j in range(maze_size)]

    maze = {}
    for i in range(maze_size):
        for j in range(maze_size):
            maze[(i, j)] = {}

            # find start and end
            if maze_list[i][j] == "A":
                start = (i, j)
            elif maze_list[i][j] == "B":
                end = (i, j)

            # add neighbours
            if i + 1 < maze_size:
                maze[(i, j)][i + 1, j] = prizes[maze_list[i + 1][j]]
            if i - 1 >= 0:
                maze[(i, j)][i - 1, j] = prizes[maze_list[i -1][j]]
            if j + 1 < maze_size:
                maze[(i, j)][i, j + 1] = prizes[maze_list[i][j + 1]]
            if j - 1 >= 0:
                maze[(i, j)][i, j - 1] = prizes[maze_list[i][j - 1]]

    return maze, start, end


def dijkstra(maze, start):
    # https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

    q = []
    dist = {}
    prev = {}

    for vertex in maze.keys():
        dist[vertex] = sys.maxsize
        prev[vertex] = []
        q.append(vertex)

    dist[start] = 0

    while q:
        # vertex in Q with min dist[u]
        u = q[0]
        for vertex in q:
            if dist[vertex] < dist[u]:
                u = vertex

        q.remove(u)

        for neighbor in maze[u].keys():
            alt = dist[u] + maze[u][neighbor]
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = [u]
            elif alt == dist[neighbor]:
                prev[neighbor].append(u)

    return dist, prev


def shortest_path(maze, maze_size, start, end):
    """ Find the shortest path in the maze """

    dist, prev = dijkstra(maze, start)

    # start with end
    path = [end]

    # add previous steps
    while True:
        path.append(prev[path[-1]][0])

        if path[-1] == start:
            break

    path.reverse()

    return path


def random_maze(size=8):
    """ Generate random maze """

    maze = ""

    # place start and end to first/last row
    start = random.randint(0, size)
    end = random.randint(size*size - size - 1, size*size - 1)

    for i in range(size*size):
        if i == start:
            maze += "A"
        elif i == end:
            maze += "B"
        else:
            maze += random.choice(("#", "#", ".", ".", "."))

    return maze


def print_maze(index, maze_size, maze_str, positions, cell_size=50):
    # create a list of lists from give 'maze string'
    maze_iter = iter(maze_str)
    maze_list = [[next(maze_iter) for i in range(maze_size)] for j in range(maze_size)]

    svg = vector.SVG(folder="cv11", name="maze%d" % index)

    # add lines
    for i in range(maze_size + 1):
        svg.add_line(0 + cell_size*i, 0, 0 + cell_size*i, maze_size*cell_size)
        svg.add_line(0, 0 + cell_size*i, maze_size*cell_size, 0 + cell_size*i)

    # add start points and 'walls'
    for i in range(maze_size):
        for j in range(maze_size):
            if maze_list[i][j] == "#":
                rect = vector.Rectangle(x=i*cell_size, y=j*cell_size, size=cell_size, color="black")
                svg.objects.append(rect)
            elif maze_list[i][j] == "A":
                point = vector.Point(x=(i*cell_size + cell_size/2), y=(j*cell_size + cell_size/2), color="green")
                svg.objects.append(point)
            elif maze_list[i][j] == "B":
                point = vector.Point(x=(i*cell_size + cell_size/2), y=(j*cell_size + cell_size/2), color="red")
                svg.objects.append(point)

    # print moves
    for i in range(len(positions) - 1):
        start = vector.Point(x=(positions[i][0]*cell_size + cell_size/2), y=(positions[i][1]*cell_size + cell_size/2))
        end = vector.Point(x=(positions[i+1][0]*cell_size + cell_size/2), y=(positions[i+1][1]*cell_size + cell_size/2))
        line = vector.Line(start=start, end=end, color="blue")
        svg.objects.append(line)

    svg.save()


maze_str = random_maze(8)
maze, start, end = read_maze(8, maze_str)
path = shortest_path(maze, 8, start, end)

for i in range(len(path) - 1):
    print_maze(i, 8, maze_str, path[:i + 2])
