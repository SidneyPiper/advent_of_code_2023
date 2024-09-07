from enum import IntEnum

TEST_MODE = False
STAR = 2

if TEST_MODE:
    with open("test_input.txt") as f:
        lines = f.readlines()
else:
    with open("input.txt") as f:
        lines = f.readlines()


class Direction(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


def find_possible_p1(r, c, direction, maze):
    possible = set()
    if (
        0 <= r - 1 < len(maze)
        and 0 <= c < len(maze)
        and not direction == Direction.SOUTH
    ):
        if maze[r - 1][c] in ".^":
            possible.add((r - 1, c, Direction.NORTH))

    if (
        0 <= r + 1 < len(maze)
        and 0 <= c < len(maze)
        and not direction == Direction.NORTH
    ):
        if maze[r + 1][c] in ".v":
            possible.add((r + 1, c, Direction.SOUTH))

    if (
        0 <= r < len(maze)
        and 0 <= c - 1 < len(maze)
        and not direction == Direction.EAST
    ):
        if maze[r][c - 1] in ".<":
            possible.add((r, c - 1, Direction.WEST))

    if (
        0 <= r < len(maze)
        and 0 <= c + 1 < len(maze)
        and not direction == Direction.WEST
    ):
        if maze[r][c + 1] in ".>":
            possible.add((r, c + 1, Direction.EAST))

    return possible


def move_p1(position, maze, result=0):
    r, c, direction = position
    possible = find_possible_p1(r, c, direction, maze)

    while len(possible) == 1:
        result += 1
        r, c, direction = possible.pop()
        possible = find_possible_p1(r, c, direction, maze)

    if len(possible) == 2:
        result += 1 + max(
            move_p1(possible.pop(), maze),
            move_p1(possible.pop(), maze),
        )

    if len(possible) == 3:
        result += 1 + max(
            move_p1(possible.pop(), maze),
            move_p1(possible.pop(), maze),
            move_p1(possible.pop(), maze),
        )

    return result


def starOne():
    maze = list(map(lambda x: list(x.strip()), lines))
    print(move_p1((0, 1, Direction.SOUTH), maze))


def find_possible_p2(position, maze):
    r, c, direction = position
    possible = set(
        filter(
            lambda x: 0 <= x[0] < len(maze)
            and 0 <= x[1] < len(maze)
            and maze[x[0]][x[1]] == ".",
            {
                (r - 1, c, Direction.NORTH),
                (r + 1, c, Direction.SOUTH),
                (r, c - 1, Direction.WEST),
                (r, c + 1, Direction.EAST),
            },
        )
    )

    match direction:
        case Direction.NORTH:
            possible.discard((r + 1, c, Direction.SOUTH))
        case Direction.SOUTH:
            possible.discard((r - 1, c, Direction.NORTH))
        case Direction.EAST:
            possible.discard((r, c - 1, Direction.WEST))
        case Direction.WEST:
            possible.discard((r, c + 1, Direction.EAST))

    return possible


def move_p2(position, maze, visited, result=0):
    possible = find_possible_p2(position, maze)

    while len(possible) == 1:
        result += 1
        position = possible.pop()

        if position == (len(maze) - 1, len(maze) - 2, Direction.SOUTH):
            return result

        if (position[0], position[1]) in visited:
            return 0

        possible = find_possible_p2(position, maze)

    if len(possible) == 2:
        p1, p2 = possible.pop(), possible.pop()
        visited.add((position[0], position[1]))
        return (
            1
            + result
            + max(
                move_p2(p1, maze, visited.copy()),
                move_p2(p2, maze, visited.copy()),
            )
        )

    if len(possible) == 3:
        p1, p2, p3 = possible.pop(), possible.pop(), possible.pop()
        visited.add((position[0], position[1]))
        return (
            1
            + result
            + max(
                move_p2(p1, maze, visited.copy()),
                move_p2(p2, maze, visited.copy()),
                move_p2(p3, maze, visited.copy()),
            )
        )

    return 0


def findNodes(maze):
    nodes = [(1, 0), (len(maze[0]) - 2, len(maze) - 1)]

    for y in range(1, len(maze) - 1):
        for x in range(1, len(maze[0]) - 1):
            if maze[y][x] == ".":
                N = [maze[y - 1][x], maze[y + 1][x], maze[y][x - 1], maze[y][x + 1]]
                if N.count(".") > 2:
                    nodes.append((x, y))
    return nodes


def walk_till_node(current, visited, n, maze, nodes):
    x, y = current

    if current in nodes:
        return current, n

    visited.append(current)

    if (x - 1, y) not in visited and maze[y][x - 1] == ".":
        return walk_till_node((x - 1, y), visited, n + 1, maze, nodes)

    if (x + 1, y) not in visited and maze[y][x + 1] == ".":
        return walk_till_node((x + 1, y), visited, n + 1, maze, nodes)

    if (x, y - 1) not in visited and maze[y - 1][x] == ".":
        return walk_till_node((x, y - 1), visited, n + 1, maze, nodes)

    if (x, y + 1) not in visited and maze[y + 1][x] == ".":
        return walk_till_node((x, y + 1), visited, n + 1, maze, nodes)


def generateEdges(maze, nodes):
    edges = []
    for x, y in nodes:
        if x > 0 and maze[y][x - 1] == ".":
            dest, n = walk_till_node((x - 1, y), [(x, y)], 1, maze, nodes)
            edges.append(((x, y), dest, n))
        if x < len(maze[0]) - 1 and maze[y][x + 1] == ".":
            dest, n = walk_till_node((x + 1, y), [(x, y)], 1, maze, nodes)
            edges.append(((x, y), dest, n))
        if y > 0 and maze[y - 1][x] == ".":
            dest, n = walk_till_node((x, y - 1), [(x, y)], 1, maze, nodes)
            edges.append(((x, y), dest, n))
        if y < len(maze) - 1 and maze[y + 1][x] == ".":
            dest, n = walk_till_node((x, y + 1), [(x, y)], 1, maze, nodes)
            edges.append(((x, y), dest, n))

    return edges


def find_longest_path(graph, start, end, visited=set(), total_length=0):
    if start == end:
        return total_length
    
    visited.add(start)
    max_length = 0

    for neighbor, length in graph[start]:
        if neighbor not in visited:
            max_length = max(max_length, find_longest_path(graph, neighbor, end, visited.copy(), total_length + length))

    return max_length



def starTwo():
    maze = list(
        map(
            lambda x: list(
                x.replace("^", ".")
                .replace("v", ".")
                .replace("<", ".")
                .replace(">", ".")
                .strip()
            ),
            lines,
        )
    )

    nodes = findNodes(maze)
    edges = generateEdges(maze, nodes)

    graph = {}

    for node in nodes:
        graph[node] = []

    for x, y, l in edges:
        graph[x].append((y, l))

    start_node = (1, 0)
    end_node = (len(maze) - 2, len(maze) - 1)
    longest_path_length = find_longest_path(graph, start_node, end_node)

    print(f"Länge des längsten Pfades: {longest_path_length}")


if STAR == 1:
    starOne()
elif STAR == 2:
    starTwo()
