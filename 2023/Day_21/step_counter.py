import numpy as np
from collections import deque

class Node:
    def __init__(self, coordinates, ch):
        self.coordinates = coordinates
        self.ch = ch
        self.children = []

    def __repr__(self):
        return f"{self.coordinates}"
        
    def set_children(self, grid):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        r, c = self.coordinates
        for dr, dc in directions:
            new_r, new_c = (r + dr) % len(grid), (c + dc) % len(grid[0])
            # if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):  # commented out for part 2

            child = grid[new_r][new_c]
            if child.ch == '.' or child.ch == 'S':
                self.children.append((child, (dr,dc)))    


def bfs(node, step_limit):
    visited = set()
    queue = deque([(node, 0, node.coordinates)])
    good_nodes = []
       
    while queue:
        node, steps, (virt_r, virt_c)= queue.popleft()

        if steps == step_limit + 1:
            break

        
        if (node.coordinates, (virt_r, virt_c)) not in visited:
            visited.add((node.coordinates, (virt_r, virt_c)))
            if steps % 2 == 0:
                good_nodes.append((virt_r, virt_c))
            steps += 1
            for child, delta in node.children:
                dr,dc = delta
                new_virt_r, new_virt_c = virt_r + dr, virt_c + dc
                # if child.coordinates[0] != new_virt_r:
                queue.append((child, steps, (new_virt_r, new_virt_c)))

                
                
                


    return good_nodes
    

# find coordinates for start position
def find_start(input):
    
    for i, row in enumerate(input):
        for j, char in enumerate(row):
            if char != 'S':
                continue
            else:
                return (i,j)


def init_nodes(grid):
    nodes = [[Node((i,j), grid[i][j]) for j in range(len(grid[0]))] for i in range(len(grid))]
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            nodes[i][j].set_children(nodes)
    
    return nodes


def draw_map(path, grid):
    for i in path:
        grid[i[0]][i[1]] = 'O'

    print(np.array(grid))


def main(data):
    start = find_start(data)
    node_grid = init_nodes(data)
    # print(np.array(node_grid).shape)
    # print(node_grid[0][0].children)
    start_node = node_grid[start[0]][start[1]]
    step_limit = 64

    garden_plots = bfs(start_node, step_limit)
    # draw_map(garden_plots, data)
    # print(garden_plots)

    return len(garden_plots)
 

if __name__ == '__main__':

    # path = r'C:\AOC\2023\Day_21\test_data.txt'
    path = r'C:\AOC\2023\Day_21\data.txt'
    
    with open(path, 'r') as file:
        input = [[ch for ch in i] for i in file.read().splitlines()]
      
    total = main(input)
    print(total)
