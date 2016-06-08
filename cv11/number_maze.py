import sys


mazes = [(4, "2 2 2 1 2 3 3 3 3 3 1 3 3 1 1 0"),
         (5, "3 1 1 2 3 2 2 1 2 3 2 1 4 4 1 3 1 4 2 4 3 1 2 3 0"),
         (5, "1 2 3 1 1 1 3 4 1 1 1 1 3 1 4 1 3 4 2 2 3 1 3 1 0"),
         (10, "9 7 9 4 1 3 4 2 8 8 2 5 8 8 1 2 5 1 2 2 3 8 2 6 8 \
               9 5 9 1 2 4 1 4 9 9 7 5 9 5 3 6 9 3 5 1 3 6 7 2 8 \
               1 2 9 9 2 8 9 9 5 9 3 9 5 6 4 9 7 9 1 4 7 9 6 1 7 \
               6 2 5 4 7 1 4 1 2 2 5 1 5 2 6 2 4 6 3 3 3 2 2 9 0")]



def read_maze(maze_size, maze_str):
    maze_str = (int(n) for n in maze_str.split())
    maze_list = [[next(maze_str) for i in range(maze_size)] for j in range(maze_size)]

    maze = {}
    for i in range(maze_size):
        for j in range(maze_size):
            maze[(i, j)] = {}

            if maze_list[i][j] == 0:
                continue

            if i + maze_list[i][j] < maze_size:
                maze[(i, j)][i + maze_list[i][j], j] = maze_list[i][j]
            if i - maze_list[i][j] >= 0:
                maze[(i, j)][i - maze_list[i][j], j] = maze_list[i][j]
            if j + maze_list[i][j] < maze_size:
                maze[(i, j)][i, j + maze_list[i][j]] = maze_list[i][j]
            if j - maze_list[i][j] >= 0:
                maze[(i, j)][i, j - maze_list[i][j]] = maze_list[i][j]

    return maze


def dijkstra(maze):
    # https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

    q = []
    dist = {}
    prev = {}

    for vertex in maze.keys():
        dist[vertex] = sys.maxsize
        prev[vertex] = []
        q.append(vertex)

    dist[(0, 0)] = 0

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


def paths(graph, start):
    global num_paths

    if start == (0, 0):
        num_paths += 1

    for neighbor in graph[start]:
        if neighbor:
            paths(graph, neighbor)


def shortest_path(maze, maze_size):
    dist, prev = dijkstra(maze)

    #print(prev)

    path = [(maze_size - 1, maze_size - 1)]

    while True:
        path.append(prev[path[-1]][0])

        if path[-1] == (0, 0):
            break

    path.reverse()

    return prev, path, dist[(maze_size - 1, maze_size - 1)]


for idx, maze in enumerate(mazes):
    graph, path, length = shortest_path(read_maze(mazes[idx][0], mazes[idx][1]), mazes[idx][0])

    num_paths = 0
    paths(graph, (mazes[idx][0] - 1, mazes[idx][0] - 1))

    print("Maze number %d:\nShortest path: %s (length %d)\nNumber of paths with same lenght: %d" % (idx + 1, str(path), length, num_paths))
    print("-----------------")
