import sys

def dijkstra(graph, start):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    distances = [sys.maxsize] * num_nodes
    distances[start] = 0

    for _ in range(num_nodes):
        min_distance = sys.maxsize
        min_index = -1

        for i in range(num_nodes):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                min_index = i

        if min_index == -1:
            break

        visited[min_index] = True

        for i in range(num_nodes):
            if not visited[i] and graph[min_index][i] > 0:
                new_distance = distances[min_index] + graph[min_index][i]
                if new_distance < distances[i]:
                    distances[i] = new_distance

    return distances

# Example adjacency matrix representation of a graph
graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

start_node = 0
shortest_distances = dijkstra(graph, start_node)
print("Shortest distances from node", start_node)
for i, distance in enumerate(shortest_distances):
    print("Node", i, ":", distance)
