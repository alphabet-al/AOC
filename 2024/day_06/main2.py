import numpy as np
import copy

def parse(grid):
    for i, row in enumerate(grid):
        for j, column in enumerate(row):
            if grid[i][j] == "^":
                return (i,j)

def in_bounds(curr_pos):
    return 0 <= curr_pos[0] < len(grid) and 0 <= curr_pos[1] < len(grid[0])

def pathfind(grid, start):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    curr_dir = 0
    curr_pos = start
    # path is a set so we don't duplicate coordinates we've traveled to 
    path = set()
    
    while in_bounds(curr_pos):
        # add current position to path
        path.add((curr_pos, curr_dir))
        
        # get coordinate of next position in direction of travel
        newR = curr_pos[0] + directions[curr_dir][0]
        newC = curr_pos[1] + directions[curr_dir][1]
        
        # if not in bounds, the guard has left the map
        if not in_bounds((newR, newC)):
            return 0

        # if not blocked, update current position to next position
        if grid[newR][newC] == "." or grid[newR][newC] == '^':
            curr_pos = (newR, newC)

        # check if next position is blocked or not
        # if blocked, change direction and continue loop
        else:
            curr_dir = (curr_dir + 1) % 4

        if (curr_pos, curr_dir) in path:
            return 1
    


def main(grid, pt2 = False):
    start = parse(grid)   
    count = 0

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if grid[i][j] == '.':
                grid[i][j] = '#'
                count += pathfind(grid, start)
                grid[i][j] = '.'

    return count
    
if __name__ == "__main__":
    # path = r"C:\AOC\2024\day_06\test_data.txt"
    path = r"C:\AOC\2024\day_06\data.txt"

    with open(path, "r") as f:
        grid = [[ch for ch in row] for row in f.read().splitlines()]
        
    ans = main(grid)
    print(f"Number of distinct positions: {ans}")