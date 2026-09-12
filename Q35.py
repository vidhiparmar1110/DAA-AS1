from collections import deque

def shortest_route(graph, start, destination):
    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {}
    parent[start] = None
    while queue:
        city = queue.popleft()
        if city == destination:
            break
        for neighbor in graph[city]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = city
                queue.append(neighbor)
    if destination not in parent:
        return None
    route = []
    current = destination
    while current is not None:
        route.append(current)
        current = parent[current]
    route.reverse()
    return route

cities = {
    "Ahmedabad": ["Vadodara", "Rajkot"],
    "Vadodara": ["Ahmedabad", "Surat"],
    "Rajkot": ["Ahmedabad", "Jamnagar"],
    "Surat": ["Vadodara", "Mumbai"],
    "Jamnagar": ["Rajkot"],
    "Mumbai": ["Surat"]
}

start = "Ahmedabad"
destination = "Mumbai"
route = shortest_route(cities,start,destination)

print("Shortest route:")
if route:
    print(" -> ".join(route))
    print("Number of roads:", len(route) - 1)
else:
    print("No route found")
