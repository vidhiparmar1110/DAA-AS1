def dfs(graph, start, visited):
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B', 'E'],
    'E': ['D']
}
visited = set()

dfs(graph, 'A', visited)
print("Visited nodes:", visited)
if len(visited) == len(graph):
    print("Graph is connected")
else:
    print("Graph is not connected")
