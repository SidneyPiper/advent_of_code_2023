from enum import IntEnum
from queue import PriorityQueue

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


def dijkstra(graph, start):
    nodes, edges = graph

    q = {start}
    visited = set()

    distances = {node: float("inf") for node in nodes}
    distances[start] = 0

    predecessors = {node: None for node in nodes}

    while q:
        print(len(q))
        u = next(iter(q))
        for key in q:
            if distances[key] < distances[u]:
                u = key
        q.remove(u)
        visited.add(u)
        for v in edges[u]:
            if v not in visited:
                q.add(v)
                alt = distances[u] + edges[u][v]
                if alt < distances[v]:
                    distances[v] = alt
                    predecessors[v] = u

    return distances, predecessors


def printTrack(graph, predecessors, start, end):
    predecessor = predecessors[end]

    while predecessor != start:
        graph[predecessor[0]][predecessor[1]] = "#"
        predecessor = predecessors[predecessor]

    graph[predecessor[0]][predecessor[1]] = "#"

    for r in graph:
        print("".join(r))


def starOne():
    # nodes = {(1), (2), (3), (4), (5)}
    # edges = {
    #    (1): {(2): 100, (3): 50},
    #    (2): {(4): 100, (5): 250},
    #    (3): {(2): 100, (5): 250},
    #    (4): {(5): 50},
    #    (5): {},
    # }

    graph = list(map(lambda x: list(x.strip()), lines))

    nodes = set()
    edges = {}

    for r in range(len(graph)):
        for c in range(len(graph[r])):
            nodes.add((r, c, 1, Direction.NORTH))
            nodes.add((r, c, 1, Direction.EAST))
            nodes.add((r, c, 1, Direction.SOUTH))
            nodes.add((r, c, 1, Direction.WEST))
            nodes.add((r, c, 2, Direction.NORTH))
            nodes.add((r, c, 2, Direction.EAST))
            nodes.add((r, c, 2, Direction.SOUTH))
            nodes.add((r, c, 2, Direction.WEST))
            nodes.add((r, c, 3, Direction.NORTH))
            nodes.add((r, c, 3, Direction.EAST))
            nodes.add((r, c, 3, Direction.SOUTH))
            nodes.add((r, c, 3, Direction.WEST))

    for node in nodes:
        edges[node] = {}

    for r in range(len(graph)):
        for c in range(len(graph[r])):
            # n1: n2,   e1,             w1
            # e1: n1,   e2,     s1,
            # s1:       e1,     s2,     w1
            # w1: n1,           s1,     w2
            # n2: n3,   e1,             w1
            # e2: n1,   e3,     s1
            # s2:       e1,     s3,     w1
            # w2: n1,           s1,     w3
            # n3:       e1,             w1
            # e3: n1,           s1
            # s3:       e1,             w1
            # w3: n1,           s1

            n, e, s, w = (r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)

            if 0 <= n[0] < len(graph):
                weight = int(graph[n[0]][n[1]])

                edges[(r, c, 1, Direction.NORTH)][
                    (n[0], n[1], 2, Direction.NORTH)
                ] = weight

                edges[(r, c, 1, Direction.EAST)][
                    (n[0], n[1], 1, Direction.NORTH)
                ] = weight

                edges[(r, c, 1, Direction.WEST)][
                    (n[0], n[1], 1, Direction.NORTH)
                ] = weight

                edges[(r, c, 2, Direction.NORTH)][
                    (n[0], n[1], 3, Direction.NORTH)
                ] = weight

                edges[(r, c, 2, Direction.EAST)][
                    (n[0], n[1], 1, Direction.NORTH)
                ] = weight

                edges[(r, c, 2, Direction.WEST)][
                    (n[0], n[1], 1, Direction.NORTH)
                ] = weight

                edges[(r, c, 3, Direction.EAST)][
                    (n[0], n[1], 1, Direction.NORTH)
                ] = weight

                edges[(r, c, 2, Direction.WEST)][
                    (n[0], n[1], 3, Direction.NORTH)
                ] = weight

            if 0 <= s[0] < len(graph):
                weight = int(graph[s[0]][s[1]])

                edges[(r, c, 1, Direction.EAST)][
                    (s[0], s[1], 1, Direction.SOUTH)
                ] = weight

                edges[(r, c, 1, Direction.SOUTH)][
                    (s[0], s[1], 2, Direction.SOUTH)
                ] = weight

                edges[(r, c, 1, Direction.WEST)][
                    (s[0], s[1], 1, Direction.SOUTH)
                ] = weight

                edges[(r, c, 2, Direction.EAST)][
                    (s[0], s[1], 1, Direction.SOUTH)
                ] = weight

                edges[(r, c, 2, Direction.SOUTH)][
                    (s[0], s[1], 3, Direction.SOUTH)
                ] = weight

                edges[(r, c, 2, Direction.WEST)][
                    (s[0], s[1], 1, Direction.SOUTH)
                ] = weight

                edges[(r, c, 3, Direction.EAST)][
                    (s[0], s[1], 1, Direction.SOUTH)
                ] = weight

                edges[(r, c, 3, Direction.WEST)][
                    (s[0], s[1], 1, Direction.SOUTH)
                ] = weight

            if 0 <= e[1] < len(graph[r]):
                weight = int(graph[e[0]][e[1]])

                edges[(r, c, 1, Direction.NORTH)][
                    (e[0], e[1], 1, Direction.EAST)
                ] = weight

                edges[(r, c, 1, Direction.EAST)][
                    (e[0], e[1], 2, Direction.EAST)
                ] = weight

                edges[(r, c, 1, Direction.SOUTH)][
                    (e[0], e[1], 1, Direction.EAST)
                ] = weight

                edges[(r, c, 2, Direction.NORTH)][
                    (e[0], e[1], 1, Direction.EAST)
                ] = weight

                edges[(r, c, 2, Direction.EAST)][
                    (e[0], e[1], 3, Direction.EAST)
                ] = weight

                edges[(r, c, 2, Direction.SOUTH)][
                    (e[0], e[1], 1, Direction.EAST)
                ] = weight

                edges[(r, c, 3, Direction.NORTH)][
                    (e[0], e[1], 1, Direction.EAST)
                ] = weight

                edges[(r, c, 3, Direction.SOUTH)][
                    (e[0], e[1], 1, Direction.EAST)
                ] = weight

            if 0 <= w[1] < len(graph[r]):
                weight = int(graph[w[0]][w[1]])

                edges[(r, c, 1, Direction.NORTH)][
                    (w[0], w[1], 1, Direction.WEST)
                ] = weight

                edges[(r, c, 1, Direction.SOUTH)][
                    (w[0], w[1], 1, Direction.WEST)
                ] = weight

                edges[(r, c, 1, Direction.WEST)][
                    (w[0], w[1], 2, Direction.WEST)
                ] = weight

                edges[(r, c, 2, Direction.NORTH)][
                    (w[0], w[1], 1, Direction.WEST)
                ] = weight

                edges[(r, c, 2, Direction.SOUTH)][
                    (w[0], w[1], 1, Direction.WEST)
                ] = weight

                edges[(r, c, 2, Direction.WEST)][
                    (w[0], w[1], 3, Direction.WEST)
                ] = weight

                edges[(r, c, 3, Direction.NORTH)][
                    (w[0], w[1], 1, Direction.WEST)
                ] = weight

                edges[(r, c, 3, Direction.SOUTH)][
                    (w[0], w[1], 1, Direction.WEST)
                ] = weight

    # for node in nodes:
    #     print(node, edges[node])

    distances, predecessors = dijkstra((nodes, edges), (0, 0, 1, Direction.EAST))

    # printTrack(
    #     graph, predecessors, (0, 0, 1, Direction.EAST), (12, 12, 1, Direction.EAST)
    # )

    end_index_r = len(graph) - 1
    end_index_c = len(graph[0]) - 1

    print(
        min(
            distances[(end_index_r, end_index_c, 1, Direction.NORTH)],
            distances[(end_index_r, end_index_c, 1, Direction.EAST)],
            distances[(end_index_r, end_index_c, 1, Direction.SOUTH)],
            distances[(end_index_r, end_index_c, 1, Direction.WEST)],
            distances[(end_index_r, end_index_c, 2, Direction.NORTH)],
            distances[(end_index_r, end_index_c, 2, Direction.EAST)],
            distances[(end_index_r, end_index_c, 2, Direction.SOUTH)],
            distances[(end_index_r, end_index_c, 2, Direction.WEST)],
            distances[(end_index_r, end_index_c, 3, Direction.NORTH)],
            distances[(end_index_r, end_index_c, 3, Direction.EAST)],
            distances[(end_index_r, end_index_c, 3, Direction.SOUTH)],
            distances[(end_index_r, end_index_c, 3, Direction.WEST)],
        )
    )


def starTwo():
    graph = list(map(lambda x: list(x.strip()), lines))

    nodes = set()
    edges = {}

    for r in range(len(graph)):
        for c in range(len(graph[r])):
            for i in range(10):
                nodes.add((r, c, i + 1, Direction.NORTH))
                nodes.add((r, c, i + 1, Direction.EAST))
                nodes.add((r, c, i + 1, Direction.SOUTH))
                nodes.add((r, c, i + 1, Direction.WEST))

    for node in nodes:
        edges[node] = {}

    for r in range(len(graph)):
        for c in range(len(graph[r])):
            # n1: n2,   e1,             w1
            # e1: n1,   e2,     s1,
            # s1:       e1,     s2,     w1
            # w1: n1,           s1,     w2
            # n2: n3,   e1,             w1
            # e2: n1,   e3,     s1
            # s2:       e1,     s3,     w1
            # w2: n1,           s1,     w3
            # n3:       e1,             w1
            # e3: n1,           s1
            # s3:       e1,             w1
            # w3: n1,           s1

            n, e, s, w = (r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)

            if 0 <= n[0] < len(graph):
                weight = int(graph[n[0]][n[1]])

                for i in range(1, 10):
                    edges[(r, c, i, Direction.NORTH)][
                        (n[0], n[1], i + 1, Direction.NORTH)
                    ] = weight

                for i in range(4, 11):
                    edges[(r, c, i, Direction.EAST)][
                        (n[0], n[1], 1, Direction.NORTH)
                    ] = weight

                    edges[(r, c, i, Direction.WEST)][
                        (n[0], n[1], 1, Direction.NORTH)
                    ] = weight

            if 0 <= s[0] < len(graph):
                weight = int(graph[s[0]][s[1]])

                for i in range(1, 10):
                    edges[(r, c, i, Direction.SOUTH)][
                        (s[0], s[1], i + 1, Direction.SOUTH)
                    ] = weight

                for i in range(4, 11):
                    edges[(r, c, i, Direction.EAST)][
                        (s[0], s[1], 1, Direction.SOUTH)
                    ] = weight

                    edges[(r, c, i, Direction.WEST)][
                        (s[0], s[1], 1, Direction.SOUTH)
                    ] = weight

            if 0 <= e[1] < len(graph[r]):
                weight = int(graph[e[0]][e[1]])

                for i in range(1, 10):
                    edges[(r, c, i, Direction.EAST)][
                        (e[0], e[1], i + 1, Direction.EAST)
                    ] = weight

                for i in range(4, 11):
                    edges[(r, c, i, Direction.SOUTH)][
                        (e[0], e[1], 1, Direction.EAST)
                    ] = weight

                    edges[(r, c, i, Direction.NORTH)][
                        (e[0], e[1], 1, Direction.EAST)
                    ] = weight

            if 0 <= w[1] < len(graph[r]):
                weight = int(graph[w[0]][w[1]])

                for i in range(1, 10):
                    edges[(r, c, i, Direction.WEST)][
                        (w[0], w[1], i + 1, Direction.WEST)
                    ] = weight

                for i in range(4, 11):
                    edges[(r, c, i, Direction.NORTH)][
                        (w[0], w[1], 1, Direction.WEST)
                    ] = weight

                    edges[(r, c, i, Direction.SOUTH)][
                        (w[0], w[1], 1, Direction.WEST)
                    ] = weight

    # for node in nodes:
    #     print(node, edges[node])

    distances, predecessors = dijkstra((nodes, edges), (0, 0, 1, Direction.EAST))

    # printTrack(
    #     graph, predecessors, (0, 0, 1, Direction.EAST), (12, 12, 1, Direction.SOUTH)
    # )

    end_index_r = len(graph) - 1
    end_index_c = len(graph[0]) - 1

    end_distances = []

    for i in range(3, 10):
        end_distances.append(
            distances[(end_index_r, end_index_c, i + 1, Direction.NORTH)]
        )
        end_distances.append(
            distances[(end_index_r, end_index_c, i + 1, Direction.EAST)]
        )
        end_distances.append(
            distances[(end_index_r, end_index_c, i + 1, Direction.SOUTH)]
        )
        end_distances.append(
            distances[(end_index_r, end_index_c, i + 1, Direction.WEST)]
        )

    print(min(end_distances))


if STAR == 1:
    starOne()
elif STAR == 2:
    starTwo()
