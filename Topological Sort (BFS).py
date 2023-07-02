from collections import defaultdict, deque

def topological_sort(graph):
    # Calculate the in-degree of each node
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Find all nodes with in-degree 0 and enqueue them
    queue = deque()
    for node in graph:
        if in_degree[node] == 0:
            queue.append(node)

    # Perform topological sort
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)

        # Decrement the in-degree of the neighbors and enqueue them if their in-degree becomes 0
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result

# Test the implementation
graph = defaultdict(list)
graph[5] = [0, 2]
graph[4] = [0, 1]
graph[2] = [3]
graph[3] = [1]
graph[0] = []

sorted_nodes = topological_sort(graph)
print("Topological Sort:", sorted_nodes)
