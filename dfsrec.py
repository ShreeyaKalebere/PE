def dfs_recursive(graph, node, visited):
    if node not in visited:
        print(node, end=" ")  # Process the node (e.g., print it)
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

# Example Usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
visited_nodes = set()
print("Recursive DFS Traversal:")
dfs_recursive(graph, 'A', visited_nodes)
print()