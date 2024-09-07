import random
from collections import deque, defaultdict, OrderedDict

TEST_MODE = False
STAR = 1

if TEST_MODE:
    with open("test_input.txt") as f:
        lines = f.readlines()
else:
    with open("input.txt") as f:
        lines = f.readlines()


def starOne():
    graph = {}

    for line in lines:
        line = line.replace(":", "").replace("\n", "").split(" ")
        key, values = line[0], line[1:]

        for value in values:
            if key not in graph.keys():
                graph[key] = []
            if value not in graph.keys():
                graph[value] = []

            graph[key].append(value)
            graph[value].append(key)

    edge_usage = find_shortest_paths_and_track_edges(graph)

    sorted_edge_usage = OrderedDict(
        sorted(edge_usage.items(), key=lambda item: item[1], reverse=True)
    )

    top_3_edges = list(sorted_edge_usage.items())[:3]

    top_3_edges = list(map(lambda x: x[0], top_3_edges))

    remove_edges(graph, top_3_edges)

    print(
        count_reachable_nodes_bfs(graph, top_3_edges[0][0])
        * count_reachable_nodes_bfs(graph, top_3_edges[0][1])
    )


def bfs_shortest_path(graph, start, end):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node in visited:
            continue

        visited.add(node)

        if node == end:
            return path

        for neighbor in graph[node]:
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)

    return None


def update_edge_usage(edge_usage, path):
    for i in range(len(path) - 1):
        edge = tuple(sorted((path[i], path[i + 1])))
        edge_usage[edge] += 1


def find_shortest_paths_and_track_edges(graph, num_iterations=500):
    edge_usage = defaultdict(int)
    nodes = list(graph.keys())

    for _ in range(num_iterations):
        start, end = random.sample(nodes, 2)
        shortest_path = bfs_shortest_path(graph, start, end)

        if shortest_path:
            update_edge_usage(edge_usage, shortest_path)

    return edge_usage


def remove_edges(graph, edges_to_remove):
    for edge in edges_to_remove:
        node1, node2 = edge
        if node2 in graph[node1]:
            graph[node1].remove(node2)
        if node1 in graph[node2]:
            graph[node2].remove(node1)


def count_reachable_nodes_bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return len(visited)


def starTwo():
    pass


if STAR == 1:
    starOne()
elif STAR == 2:
    starTwo()
