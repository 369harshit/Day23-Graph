from collections import defaultdict

class Graph:
    def __init__(self, num_vertices):
        self.graph = defaultdict(list)
        self.num_vertices = num_vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)

        stack.insert(0, v)

    def topological_sort(self):
        visited = [False] * self.num_vertices
        stack = []

        for vertex in range(self.num_vertices):
            if not visited[vertex]:
                self.topological_sort_util(vertex, visited, stack)

        return stack


# Example usage
g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Topological Sort:")
print(g.topological_sort())
