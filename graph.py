graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D', 'E'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C']
}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)


dfs(visited, graph, 'A')
