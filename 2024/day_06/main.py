import numpy as np
import copy

def parse(grid):
    for i, row in enumerate(grid):
        for j, column in enumerate(row):
            if grid[i][j] == "^":
                return (i,j)

def in_bounds(curr_pos):
    return 0 <= curr_pos[0] < len(grid) and 0 <= curr_pos[1] < len(grid[0])

def pathfind(grid, start, dir):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    curr_dir = dir
    curr_pos = start
    # path is a set so we don't duplicate coordinates we've traveled to 
    path = set()
    
    while in_bounds(curr_pos):
        # add current position to path
        path.add(curr_pos)
        # get coordinate of next position in direction of travel
        newR = curr_pos[0] + directions[curr_dir][0]
        newC = curr_pos[1] + directions[curr_dir][1]
        # if not blocked, update current position to next position
        if not in_bounds((newR, newC)) or grid[newR][newC] == "." or grid[newR][newC] == '^':
            curr_pos = (newR, newC)
        # check if next position is blocked or not
        # if blocked, change direction and continue loop
        else:
            curr_dir = (curr_dir + 1) % 4
    
    return path


def visualize_path(path, grid):
    pathed_grid = copy.deepcopy(grid)

    for r,c in path:
        pathed_grid[r][c] = 'X'
    
    for row in pathed_grid:
        print(row)


def main(grid):
    start = parse(grid)   
    path = pathfind(grid, start, 0)
    # visualize_path(path, grid)
    
    return len(path)
    

if __name__ == "__main__":
    # path = r"C:\AOC\2024\day_06\test_data.txt"
    path = r"C:\AOC\2024\day_06\data.txt"

    with open(path, "r") as f:
        grid = [[ch for ch in row] for row in f.read().splitlines()]
        
    ans = main(grid)
    print(f"Number of distinct positions: {ans}")