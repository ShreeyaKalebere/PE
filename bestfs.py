import heapq

def best_first_search(graph, start, goal, heuristic):
    """
    Implements the Best-First Search algorithm.

    Args:
        graph (dict): A dictionary representing the graph where keys are nodes
                      and values are lists of their neighbors.
        start: The starting node.
        goal: The target node.
        heuristic (dict): A dictionary mapping each node to its heuristic value.

    Returns:
        dict: A dictionary storing the path from start to goal, where keys are
              nodes and values are their parent nodes in the path. Returns None
              if no path is found.
    """
    # Priority queue stores tuples of (priority, node)
    # The priority is determined by the heuristic value of the node.
    frontier = [(heuristic[start], start)]
    came_from = {start: None}  # Stores the path

    while frontier:
        _, current = heapq.heappop(frontier)  # Get node with lowest heuristic

        if current == goal:
            return came_from

        for neighbor in graph[current]:
            if neighbor not in came_from:
                priority = heuristic[neighbor]
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current

    return None  # No path found

def reconstruct_path(came_from, start, goal):
    """
    Reconstructs the path from the 'came_from' dictionary.

    Args:
        came_from (dict): The dictionary returned by best_first_search.
        start: The starting node.
        goal: The target node.

    Returns:
        list: A list representing the path from start to goal, or an empty list
              if no path was found or came_from is None.
    """
    if came_from is None:
        return []

    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

if __name__ == "__main__":
    # Example Usage:
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': ['G', 'I'],
        'E': ['H'],
        'F': [],
        'G': [],
        'H': [],
        'I': []
    }

    heuristic = {
        'A': 10, 'B': 8, 'C': 7,
        'D': 6, 'E': 4, 'F': 5,
        'G': 3, 'H': 2, 'I': 0
    }

    start_node = 'A'
    goal_node = 'I'

    came_from_result = best_first_search(graph, start_node, goal_node, heuristic)

    if came_from_result:
        path = reconstruct_path(came_from_result, start_node, goal_node)
        print(f"Path from {start_node} to {goal_node}: {path}")
    else:
        print(f"No path found from {start_node} to {goal_node}.")