from collections import defaultdict

def detect_cycle(graph):
    # Calculate the in-degree of each node
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Initialize a stack to track the topological order
    stack = []

    def dfs(node):
        # Mark the current node as visited
        visited.add(node)

        # Explore the neighbors of the current node
        for neighbor in graph[node]:
            # If the neighbor is already visited, a cycle is detected
            if neighbor in visited:
                return True

            # If the neighbor is not visited, perform DFS recursively
            if neighbor not in stack and dfs(neighbor):
                return True

        # Push the current node onto the stack
        stack.append(node)

        return False

    # Track the visited nodes during DFS traversal
    visited = set()

    # Perform DFS on each node in the graph
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False

# Test the implementation
graph = defaultdict(list)
graph[1] = [2]
graph[2] = [3]
graph[3] = [1]

has_cycle = detect_cycle(graph)
print("Has cycle:", has_cycle)
