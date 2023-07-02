from collections import defaultdict, deque

def canFinish(numCourses, prerequisites):
    # Build the adjacency list representation of the graph
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    for prerequisite in prerequisites:
        course, prereq = prerequisite
        graph[prereq].append(course)
        in_degree[course] += 1

    # Perform topological sort
    queue = deque()
    for course in range(numCourses):
        if in_degree[course] == 0:
            queue.append(course)

    while queue:
        course = queue.popleft()
        numCourses -= 1

        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return numCourses == 0

numCourses = 4
prerequisites = [[1, 0], [2, 1], [3, 2]]

if canFinish(numCourses, prerequisites):
    print("It is possible to schedule the courses without any prerequisites.")
else:
    print("It is not possible to schedule the courses without violating prerequisites.")
