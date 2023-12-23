import numpy as np
import sys, time
from collections import deque

sys.setrecursionlimit(3000)

class Maze:
    def __init__(self, grid):
        self.grid = grid
        self.width = len(grid[0])
        self.height = len(grid)
        self.start = (0, 1)
        self.end = (len(grid) - 1, len(grid[-1]) - 2)

    def __repr__(self):
        grid_str = ''
        for row in self.grid:
            grid_str += ' '.join(str(cell) for cell in row) + '\n'
        return grid_str
        
        
    def get_neighbors(self, pos):
        neighbors = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        r, c = pos
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < self.height and 0 <= new_c < self.width:
                neighbor = self.grid[new_r][new_c]
                """ part 1 """
                # if neighbor == '.' or (neighbor == 'v' and (dr,dc) == (1, 0)) or \
                #     (neighbor == '>' and (dr,dc) == (0, 1)): # change this depending on map characteristics
                #     neighbors.append((new_r, new_c))   
                """ part 2 """
                if neighbor == '.' or neighbor == 'v' or neighbor == '>':
                    neighbors.append((new_r, new_c)) 

        return neighbors 



def parse(data):
    pass


def dfs_r(grid, pos, path, all_paths):
    # recursion dfs
    if pos == grid.end:
        all_paths.append(path)
    else:
        for neighbor in grid.get_neighbors(pos):
            if neighbor not in path:
                dfs_r(grid, neighbor, path + [neighbor], all_paths)

def dfs(grid, pos):
    # iterative dfs
    stack = [(pos, [])]
    all_paths = []

    while stack:
        pos, path = stack.pop()

        if pos == grid.end:
            all_paths.append(path)
            continue
        
        for neighbor in grid.get_neighbors(pos):
            if neighbor not in path:
                new_path = path + [neighbor]
                stack.append((neighbor, new_path))

    return all_paths



def bfs(grid, pos):
    queue = deque([ ( pos, [] ) ])
    all_paths = []

    while queue:
        pos, path = queue.popleft()

        if pos == grid.end:
            all_paths.append(path)
            continue
        
        for neighbor in grid.get_neighbors(pos):
            if neighbor not in path:
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))

    return all_paths



def find_max_hike(allp):
    return max(len(i) for i in allp)
   
    

def main(data):
    start = (0,1)
    grid = Maze(data)
    # print(grid.get_neighbors((3,11)))
    
    # recursion solution need to set recursion limit to 3000 to work
    all_paths = []
    # dfs_r(grid, start, [], all_paths)


    # iterative solution
    all_paths = dfs(grid, start) 


    " part 2 "    
    # all_paths = bfs(grid, start) 

    hike = find_max_hike(all_paths)

    return hike

if __name__ == '__main__':

    path = r'C:\AOC\2023\Day_23\test_data.txt'
    # path = r'C:\AOC\2023\Day_23\data.txt'
    
    with open(path, 'r') as file:
        input = [[ch for ch in i] for i in file.read().splitlines()]

        
    start_time = time.time()
    total = main(input)
    print(total)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"The code took {elapsed_time} seconds to run")
