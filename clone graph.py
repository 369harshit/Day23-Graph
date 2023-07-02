class Node:
    def __init__(self, val=None, neighbors=None):
        self.val = val
        if neighbors is not None:
            self.neighbors = neighbors
        else:
            self.neighbors = []


def cloneGraph(node):
    if node is None:
        return None

    visited = {}
    return cloneNode(node, visited)

def cloneNode(node, visited):
    if node.val in visited:
        return visited[node.val]

    cloned_node = Node(node.val)
    visited[node.val] = cloned_node

    for neighbor in node.neighbors:
        cloned_neighbor = cloneNode(neighbor, visited)
        cloned_node.neighbors.append(cloned_neighbor)

    return cloned_node

# Create an example undirected graph
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

# Clone the graph
cloned_node = cloneGraph(node1)

# Test the cloned graph
print(cloned_node.val)  # Output: 1
print(cloned_node.neighbors[0].val)  # Output: 2
print(cloned_node.neighbors[1].val)  # Output: 4

cloned_node = cloneGraph(node2)
print(cloned_node.val)  
print(cloned_node.neighbors[0].val)  
print(cloned_node.neighbors[1].val)

cloned_node = cloneGraph(node3)
print(cloned_node.val)  
print(cloned_node.neighbors[0].val)  
print(cloned_node.neighbors[1].val)

cloned_node = cloneGraph(node4)
print(cloned_node.val)  
print(cloned_node.neighbors[0].val)  
print(cloned_node.neighbors[1].val)
