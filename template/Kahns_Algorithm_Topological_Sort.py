from collections import deque

def FindTopologicalOrdering(g):

    n = len(g)

    # Step 1: Initialize in-degree dictionary with all nodes set to 0
    in_degree = {node: 0 for node in g}
    
    # Step 2: Populate in-degree by iterating over edges
    for node, neighbors in g.items():
        for neighbor in neighbors:
            in_degree[neighbor] += 1

    # Print the in-degree dictionary
    print(in_degree)

    # 'q' always contains the set nodes with no incoming edges.
    q = deque()
    for node in in_degree:
        if in_degree[node] == 0:
            q.append(node)

    index = 0
    order = [0] * n
    while q:
        at = q.popleft()
        order[index] = at
        index += 1
        neighbors = g[at]
        for neighbor in neighbors:
            in_degree[neighbor] = in_degree[neighbor] - 1
            if in_degree[neighbor] == 0:
                q.append(neighbor)
    if index != n:
        return False

    return order

# 'g' is a directed acyclic graph represented as a adjacency list
g = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['C']}


ordering = FindTopologicalOrdering(g)
print(ordering)
        