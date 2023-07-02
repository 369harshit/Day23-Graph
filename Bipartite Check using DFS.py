from collections import defaultdict

class Graph:
    def __init__(self, num_vertices):
        self.graph = defaultdict(list)
        self.num_vertices = num_vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_bipartite(self):
        color = [-1] * self.num_vertices  # Stores color for each vertex

        for vertex in range(self.num_vertices):
            if color[vertex] == -1:  # Unvisited vertex
                if not self.dfs(vertex, color, 0):
                    return False

        return True

    def dfs(self, current_vertex, color, current_color):
        color[current_vertex] = current_color

        for neighbor in self.graph[current_vertex]:
            if color[neighbor] == -1:  # Unvisited neighbor
                if not self.dfs(neighbor, color, 1 - current_color):
                    return False
            elif color[neighbor] == color[current_vertex]:  # Neighbor has the same color
                return False

        return True


# Example usage
g = Graph(8)
g.add_edge(1, 2)
g.add_edge(2, 6)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(6, 5)
g.add_edge(4, 7)
g.add_edge(7, 8)

print("Is Bipartite:", g.is_bipartite())
