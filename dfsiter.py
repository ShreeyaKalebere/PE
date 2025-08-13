def dfs_iterative(graph, start_node):
    visited = set()
    stack = [start_node]

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            print(current_node, end=" ")  # Process the node
            visited.add(current_node)
            # Add unvisited neighbors to the stack.
            # Reverse the order to ensure correct traversal for some graph types.
            for neighbor in reversed(graph.get(current_node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

# Example Usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print("Iterative DFS Traversal:")
dfs_iterative(graph, 'A')
print()