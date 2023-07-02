from collections import deque, defaultdict

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
                if not self.bfs(vertex, color):
                    return False

        return True

    def bfs(self, start_vertex, color):
        queue = deque()
        queue.append(start_vertex)
        color[start_vertex] = 0  # Assign color 0 to the start vertex

        while queue:
            current_vertex = queue.popleft()

            for neighbor in self.graph[current_vertex]:
                if color[neighbor] == -1:  # Unvisited neighbor
                    color[neighbor] = 1 - color[current_vertex]  # Assign opposite color
                    queue.append(neighbor)
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
