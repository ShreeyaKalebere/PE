from collections import deque

def bfs(graph, start_node):
    """
    Performs a Breadth-First Search (BFS) on a graph.

    Args:
        graph (dict): An adjacency list representation of the graph,
                      where keys are nodes and values are lists/sets of neighbors.
        start_node: The node from which to start the BFS.

    Returns:
        list: A list of nodes in the order they were visited during the BFS.
    """
    visited = set()  # To keep track of visited nodes
    queue = deque([start_node])  # Initialize the queue with the starting node
    bfs_traversal_order = []

    visited.add(start_node)

    while queue:
        current_node = queue.popleft()  # Dequeue the front node
        bfs_traversal_order.append(current_node)

        # Explore neighbors
        for neighbor in graph.get(current_node, []):  # Handle nodes with no neighbors
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return bfs_traversal_order

# Example Usage:
if __name__ == "__main__":
    # Representing the graph using an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start_node = 'A'
    traversal_result = bfs(graph, start_node)
    print(f"BFS traversal starting from {start_node}: {traversal_result}")

    graph2 = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1, 5],
        5: [2, 4]
    }
    start_node2 = 0
    traversal_result2 = bfs(graph2, start_node2)
    print(f"BFS traversal starting from {start_node2}: {traversal_result2}")