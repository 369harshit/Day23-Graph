from collections import defaultdict, deque

def detect_cycle(graph):
    in_degree = defaultdict(int)

    # Calculate the in-degree of each node
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque()

    # Find all nodes with in-degree 0 and enqueue them
    for node in graph:
        if in_degree[node] == 0:
            queue.append(node)

    while queue:
        node = queue.popleft()

        # Remove the node from the graph and update in-degrees
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If any in-degree is non-zero, there is a cycle
    for node in in_degree:
        if in_degree[node] != 0:
            return True

    return False

# Test the implementation
graph = defaultdict(list)
graph[1] = [2]
graph[2] = [3]
graph[3] = [1]

has_cycle = detect_cycle(graph)
print("Has cycle:", has_cycle)
