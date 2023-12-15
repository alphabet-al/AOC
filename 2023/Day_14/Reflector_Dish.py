import numpy as np
from functools import lru_cache

dir = {"north" : (-1, 0),
       "west"  : ( 0,-1),
       "south" : ( 1, 0),
       "east"  : ( 0, 1),
       }

def swap(curr_xy, direction, data):
    # recursive function that swaps current element, if a swappable element, with the next
    # element in the passed direction

    curr_row, curr_col = curr_xy
    next_row, next_col = (curr_row - 1), (curr_col)

    if curr_row == 0:
        return 0

    t_curr_row, t_curr_col = coor_transform(data, curr_row, curr_col, direction)
    t_next_row, t_next_col = coor_transform(data, next_row, next_col, direction)
    ele = data[t_curr_row][t_curr_col]
    next_ele = data[t_next_row][t_next_col]

    if ele != 'O' or next_ele != '.':
        return 0
    
    temp = next_ele
    data[t_next_row][t_next_col] = ele
    data[t_curr_row][t_curr_col] = temp
    swap((next_row, next_col), direction, data)

    return 0


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
    

def tilt(data, dir):
    # loop through each element and swap current element with element in next direction (dir)
    
    for i in range(1, len(data)):   
        for j in range(len(data[0])):
            coor = (i, j)
            swap(coor, dir, data)


def main(data):
    cycles = 1000


    for cyc in range(cycles):
        for k in dir.keys():
            tilt(data, k)

        
    counts = np.count_nonzero(data == 'O', axis=1)
    total = sum(counts[i] * (len(counts) - i) for i in range(len(counts)))
    
    print(total)

    # for i in data:
    #     print(i)


if __name__ == '__main__':

    # path = r'C:\AOC\2023\Day_14\test_data.txt'
    path = r'C:\AOC\2023\Day_14\data.txt'

    with open(path, 'r') as file:
        input = np.array( [[j for j in i] for i in file.read().splitlines()] )

    total = main(input)
    # print(total)