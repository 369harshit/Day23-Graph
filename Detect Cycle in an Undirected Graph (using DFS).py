from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, v):
                    return True
            elif parent != neighbor:
                return True

        return False

    def is_cyclic(self):
        visited = defaultdict(bool)

        for vertex in self.graph:
            if not visited[vertex]:
                if self.is_cyclic_util(vertex, visited, -1):
                    return True

        return False


# Example usage:
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 5)
g.add_edge(5, 7)
g.add_edge(7, 6)
g.add_edge(6, 3)
g.add_edge(3, 4)


if g.is_cyclic():
    print("Graph contains a cycle")
else:
    print("Graph doesn't contain a cycle")
