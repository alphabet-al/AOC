from collections import defaultdict
from itertools import combinations
import sys

sys.setrecursionlimit(3000)

def parse_input(input_data):
    graph = defaultdict(set)
    for line in input_data:
        node, edges = line.split(':')
        for edge in edges.strip().split(' '):
            graph[node].add(edge)
            graph[edge].add(node)
    return graph

def dfs(graph, start, visited):
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def check_split(graph, edge1, edge2, edge3):
    # Remove the edges
    graph[edge1[0]].remove(edge1[1])
    graph[edge1[1]].remove(edge1[0])
    graph[edge2[0]].remove(edge2[1])
    graph[edge2[1]].remove(edge2[0])
    graph[edge3[0]].remove(edge3[1])
    graph[edge3[1]].remove(edge3[0])

    # Check the split
    visited = set()
    dfs(graph, next(iter(graph)), visited)

    # Add the edges back
    graph[edge1[0]].add(edge1[1])
    graph[edge1[1]].add(edge1[0])
    graph[edge2[0]].add(edge2[1])
    graph[edge2[1]].add(edge2[0])
    graph[edge3[0]].add(edge3[1])
    graph[edge3[1]].add(edge3[0])

    if len(visited) != len(graph):
        return len(visited), len(graph) - len(visited)
    return None


def find_solution(input_data):
    graph = parse_input(input_data)
    all_edges = [(node, neighbor) for node in graph for neighbor in graph[node] if node < neighbor]

    for edge1, edge2, edge3 in combinations(all_edges, 3):
        split = check_split(graph, edge1, edge2, edge3)
        if split:
            return split[0] * split[1]

    return None



if __name__ == '__main__':

    # path = r'C:\AOC\2023\Day_25\test_data.txt'
    path = r'C:\AOC\2023\Day_25\data.txt'
    
    with open(path, 'r') as file:
    #     input = [i for i in file.read().splitlines()]
        input = file.read().splitlines()
        
    # total = main(input)
    # print(total)


    result = find_solution(input)
    print(f"The product of the sizes of the two groups is: {result}")