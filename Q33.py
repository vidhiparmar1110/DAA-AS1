from collections import deque

def shortest_path(graph, start, target):
    queue = deque([start])

    visited = set()
    visited.add(start)

    parent = {}
    parent[start] = None

    while queue:
        node = queue.popleft()
        if node == target:
            break
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

    if target not in parent:
        return None
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start = 'A'
target = 'F'
path = shortest_path(graph, start, target)
print("Shortest path:", path)
print("Number of edges:", len(path) - 1)
