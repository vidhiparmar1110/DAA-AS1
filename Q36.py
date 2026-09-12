def dfs(graph, node, visited):
    print(node, end=" ")
    visited[node] = True

    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and not visited[neighbor]:
            dfs(graph, neighbor, visited)

graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0]
]

visited = [False] * len(graph)
print("DFS Traversal:")
dfs(graph, 0, visited)
