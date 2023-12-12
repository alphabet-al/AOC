"""
--- Day 11: Cosmic Expansion ---
You continue following signs for "Hot Springs" and eventually come across an observatory. The Elf within turns out to 
be a researcher studying cosmic expansion using the giant telescope here.

He doesn't know anything about the missing machine parts; he's only visiting for this research project. However, he 
confirms that the hot springs are the next-closest area likely to have people; he'll even take you straight there once 
he's done with today's observation analysis.

Maybe you can help him with the analysis to speed things up?

The researcher has collected a bunch of data and compiled the data into a single giant image (your puzzle input). The 
image includes empty space (.) and galaxies (#). For example:

...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
The researcher is trying to figure out the sum of the lengths of the shortest path between every pair of galaxies. 
However, there's a catch: the universe expanded in the time it took the light from those galaxies to reach the 
observatory.

Due to something involving gravitational effects, only some space expands. In fact, the result is that any rows or 
columns that contain no galaxies should all actually be twice as big.

In the above example, three columns and two rows contain no galaxies:

   v  v  v
 ...#......
 .......#..
 #.........
>..........<
 ......#...
 .#........
 .........#
>..........<
 .......#..
 #...#.....
   ^  ^  ^
These rows and columns need to be twice as big; the result of cosmic expansion therefore looks like this:

....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#.......
Equipped with this expanded universe, the shortest path between every pair of galaxies can be found. It can help to 
assign every galaxy a unique number:

....1........
.........2...
3............
.............
.............
........4....
.5...........
............6
.............
.............
.........7...
8....9.......
In these 9 galaxies, there are 36 pairs. Only count each pair once; order within the pair doesn't matter. For each 
pair, find any shortest path between the two galaxies using only steps that move up, down, left, or right exactly 
one . or # at a time. (The shortest path between two galaxies is allowed to pass through another galaxy.)

For example, here is one of the shortest paths between galaxies 5 and 9:

....1........
.........2...
3............
.............
.............
........4....
.5...........
.##.........6
..##.........
...##........
....##...7...
8....9.......
This path has length 9 because it takes a minimum of nine steps to get from galaxy 5 to galaxy 9 (the eight locations 
marked # plus the step onto galaxy 9 itself). Here are some other example shortest path lengths:

Between galaxy 1 and galaxy 7: 15
Between galaxy 3 and galaxy 6: 17
Between galaxy 8 and galaxy 9: 5
In this example, after expanding the universe, the sum of the shortest path between all 36 pairs of galaxies is 374.

Expand the universe, then find the length of the shortest path between every pair of galaxies. What is the sum of 
these lengths?

Your puzzle answer was 9563821.

--- Part Two ---
The galaxies are much older (and thus much farther apart) than the researcher initially estimated.

Now, instead of the expansion you did before, make each empty row or column one million times larger. That is, each 
empty row should be replaced with 1000000 empty rows, and each empty column should be replaced with 1000000 empty 
columns.

(In the example above, if each empty row or column were merely 10 times larger, the sum of the shortest paths between 
every pair of galaxies would be 1030. If each empty row or column were merely 100 times larger, the sum of the shortest 
paths between every pair of galaxies would be 8410. However, your universe will need to expand far beyond these values.)

Starting with the same initial image, expand the universe according to these new rules, then find the length of the 
shortest path between every pair of galaxies. What is the sum of these lengths?

Your puzzle answer was 827009909817.
"""

import numpy as np
from itertools import combinations

def parse(input):
    input = [[char for char in i.strip()] for i in input]
    arr = np.array(input)
    
    return arr

def transform(data):
    row_index = []
    for i in reversed(range(data.shape[0])):
        row = data[i,:]
        if np.all(row == '.'):
            # data = np.insert(data, i+1, row, axis = 0)  # part 1
            row_index.append(i)

    col_index = []
    for i in reversed(range(data.shape[1])):
        col = data[:,i]
        if np.all(col == '.'):
            # data = np.insert(data, i+1, col, axis = 1)  # part 1
            col_index.append(i)
    
    num = 1
    galaxy = {}
    num_array = []

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if data[i,j] == '#':
                data[i,j] = num
                galaxy[num] = (i,j)
                num_array.append(num)
                num += 1
    
    # return data, num_array, galaxy  # part 1
    return data, num_array, galaxy, row_index, col_index  # part 2

def manhattan(pt1, pt2):
    return np.sum(np.abs(np.array(pt1) - np.array(pt2)))

def manhattan2(r1, c1, r2, c2):
    return sum((abs(r1 - r2), abs(c1 - c2)))

def find_min_sum(c_list, pt_info):
    total = 0
    
    for points in c_list:
        p1, p2 = points
        total += manhattan(pt_info[p1], pt_info[p2])

    return total

def find_min_sum2(c_list, pt_info, row_b, col_b):
    total = 0
    em = 1_000_000 # emptiness multiplier
        
    for points in c_list:
        p1, p2 = points
        
        r1, c1 = pt_info[p1]
        r2, c2 = pt_info[p2]
        lower_bound_row = min(r1, r2)
        lower_bound_col = min(c1, c2)
        upper_bound_row = max(r1, r2)
        upper_bound_col = max(c1, c2)
        row_multiplier = len([num for num in row_b if lower_bound_row < num < upper_bound_row])
        col_multiplier = len([num for num in col_b if lower_bound_col < num < upper_bound_col])
        if r2 > r1:
            r2 = r2 + (row_multiplier * (em - 1))
        else:
            r2 = r2 - (row_multiplier * (em - 1))

        if c2 > c1:
            c2 = c2 + (col_multiplier * (em - 1))
        else:
            c2 = c2 - (col_multiplier * (em - 1))

        total += manhattan2(r2, c2, r1, c1)

    return total

def main(input):
    data = parse(input)

    """ part 1 """
    # mod_data, galaxies, galaxy_info = transform(data)
    # combos = list(combinations(galaxies, 2))
    # min_sum = find_min_sum(combos, galaxy_info)

    """ part 2 """
    mod_data, galaxies, galaxy_info, row_bound, col_bound = transform(data)   # part 2
    combos = list(combinations(galaxies, 2))
    min_sum = find_min_sum2(combos, galaxy_info, row_bound, col_bound)

    return min_sum
    

if __name__ == '__main__':

    # path = r'C:\AOC\2023\Day_11\test_data.txt'
    path = r'C:\AOC\2023\Day_11\data.txt'

    with open(path, 'r') as file:
        input = file.read().splitlines()

        length = main(input)
        print(length)

