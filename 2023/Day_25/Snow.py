from collections import defaultdict
import random


def parse(input):
    graph = defaultdict()

    for i in input:
        key, value = i.split(':')
        value = [v for v in value.strip().split(' ')]
        graph[key] = value
    
    return graph

def karger_min_cut(graph):
    while len(graph) > 2:
        node1, connected_nodes = random.choice(list(graph.items()))
        if connected_nodes:
            node2 = random.choice(connected_nodes)
            graph[node1].extend(graph[node2])
        for key, nodes in graph.items():
            if node2 in nodes:
                graph[key].remove(node2)
                graph[key].append(node1)
        del graph[node2]
    return len(list(graph.values())[0])

def find_min_cut(graph, iterations):
    min_cut = float('inf')
    for _ in range(iterations):
        new_graph = defaultdict(list, {k: v[:] for k, v in graph.items()})
        cut = karger_min_cut(new_graph)
        min_cut = min(min_cut, cut)

    return min_cut, new_graph



def main(input):
    graph = parse(input)
    # for i, node in enumerate(graph.values()):
    #     print(node, i)
    min_cut, new_graph = find_min_cut(graph, 1000)
    # print(new_graph)
    for i in new_graph:
        print(i)
    print(f"The minimum cut is: {min_cut}")
    


    
if __name__ == '__main__':

    path = r'C:\AOC\2023\Day_25\test_data.txt'
    # path = r'C:\AOC\2023\Day_25\data.txt'
    
    with open(path, 'r') as file:
        input = [i for i in file.read().splitlines()]
        
    total = main(input)
    print(total)
