from collections import deque, defaultdict

def FindTopologicalOrdering(g):

    n = len(g)

    # Step 1: Initialize in-degree dictionary with all nodes set to 0
    in_degree = {node: 0 for node in g}
    
    # Step 2: Populate in-degree by iterating over edges
    for node, neighbors in g.items():
        for neighbor in neighbors:
            in_degree[neighbor] += 1

    # Print the in-degree dictionary
    # print(in_degree)

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

def create_adj_list(g):
    adj_list = {}

    for k in g:
        adj_list[k] = []

    for k,v in g.items():
        for input_node, qty in v['inputs'].items():
            if input_node not in adj_list:
                adj_list[input_node] = []
            adj_list[input_node].append(k)

    return adj_list

def how_much_ore(top_order, g):
    needed = defaultdict(int)
    needed['FUEL'] = 1
    print(needed)
    for node in reversed(top_order):
        if node == 'ORE':
            continue

        output_qty = g[node]['outputs']
        multiplier = -(-needed[node] // output_qty)

        for input_node, input_qty in g[node]['inputs'].items():
            needed[input_node] += input_qty * multiplier

    return needed['ORE']

if __name__ == "__main__":
    # path = "./test_data.txt"
    path = "./data.txt"
    g = {}  # rules-based graph representation

    with open(path, 'r') as f:
        data = f.read().splitlines()
        for row in data:
            ins, outs = row.split(' => ')
            o_qty, o_res = outs.split(" ")
            inputs = ins.split(", ")
            g[o_res] = {"outputs" : int(o_qty), "inputs" : {i_res : int(i_qty) for i_qty, i_res in (ea.split(" ") for ea in inputs)}}

    g_adj_list = create_adj_list(g) # adj list graph representation
    top_order = FindTopologicalOrdering(g_adj_list)
    # print(top_order)
    ore_needed = how_much_ore(top_order, g)
    print(f"Ore Needed: {ore_needed}")

    ORE_ON_HAND = 1000000000000
