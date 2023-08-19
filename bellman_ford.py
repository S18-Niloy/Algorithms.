import sys

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def bellman_ford(self, source):
        distances = [sys.maxsize] * self.num_vertices
        distances[source] = 0

        for _ in range(self.num_vertices - 1):
            for u, v, weight in self.edges:
                if distances[u] != sys.maxsize and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

        for u, v, weight in self.edges:
            if distances[u] != sys.maxsize and distances[u] + weight < distances[v]:
                print("Graph contains negative-weight cycle")
                return

        return distances

# Example graph representation
num_vertices = 5
graph = Graph(num_vertices)
graph.add_edge(0, 1, -1)
graph.add_edge(0, 2, 4)
graph.add_edge(1, 2, 3)
graph.add_edge(1, 3, 2)
graph.add_edge(1, 4, 2)
graph.add_edge(3, 2, 5)
graph.add_edge(3, 1, 1)
graph.add_edge(4, 3, -3)

source_vertex = 0
shortest_distances = graph.bellman_ford(source_vertex)
print("Shortest distances from vertex", source_vertex)
for i, distance in enumerate(shortest_distances):
    print("Vertex", i, ":", distance)
