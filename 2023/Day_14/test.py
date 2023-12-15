import numpy as np
from functools import lru_cache

directions = {"north": (-1, 0), "west": (0, -1), "south": (1, 0), "east": (0, 1)}

@lru_cache(maxsize=None)
def swap(curr_xy, next_xy):
    curr_row, curr_col = curr_xy
    next_row, next_col = next_xy

    if curr_row == 0:
        return False

    return True

def coor_transform(grid, i, j, orientation):
    if orientation == 'north':  # y down, x right
        return i,j
    elif orientation == 'east':  # y left, x down
        return j, len(grid[0]) - i - 1
    elif orientation == 'south':  # y up, x left
        return len(grid) - i - 1, len(grid[0]) - j - 1
    elif orientation == 'west':  # y right, x up
        return len(grid) - j - 1, i
    else:
        raise ValueError("Invalid orientation")

def tilt(data, direction):
    for i in range(1, len(data)):   
        for j in range(len(data[0])):
            curr_xy = (i, j)
            dy, dx = directions[direction]
            next_xy = (i + dy, j + dx)

            # Check if next_xy is within the bounds of the array
            if 0 <= next_xy[0] < len(data) and 0 <= next_xy[1] < len(data[0]):
                t_curr_row, t_curr_col = coor_transform(data, *curr_xy, direction)
                t_next_row, t_next_col = coor_transform(data, *next_xy, direction)

                # Swap elements if conditions are met
                if data[t_curr_row][t_curr_col] == 'O' and data[t_next_row][t_next_col] == '.':
                    data[t_curr_row][t_curr_col], data[t_next_row][t_next_col] = data[t_next_row][t_next_col], data[t_curr_row][t_curr_col]



def main(data):
    cycles = 1000000

    for cyc in range(cycles):
        for k in directions.keys():
            tilt(data, k)
        
    counts = np.count_nonzero(data == 'O', axis=1)
    total = sum(counts[i] * (len(counts) - i) for i in range(len(counts)))
    
    print(total)

    # for i in data:
    #     print(i)


if __name__ == '__main__':

    path = r'C:\AOC\2023\Day_14\test_data.txt'
    # path = r'C:\AOC\2023\Day_14\data.txt'

    with open(path, 'r') as file:
        input = np.array( [[j for j in i] for i in file.read().splitlines()] )

    total = main(input)
    # print(total)
