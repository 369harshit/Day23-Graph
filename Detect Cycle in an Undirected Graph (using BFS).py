from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def has_cycle(self):
        visited = set()
        queue = deque()

        for vertex in self.graph:
            if vertex not in visited:
                queue.append((vertex, None))  # (vertex, parent)
                visited.add(vertex)

                while queue:
                    curr_vertex, parent = queue.popleft()

                    for neighbor in self.graph[curr_vertex]:
                        if neighbor not in visited:
                            queue.append((neighbor, curr_vertex))
                            visited.add(neighbor)
                        elif neighbor != parent:
                            return True

        return False


# Create a graph
g = Graph()
g.add_edge(4, 5)
g.add_edge(4, 6)
g.add_edge(5, 6)

print("Graph has a cycle:", g.has_cycle())
