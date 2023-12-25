import numpy as np
from itertools import combinations

def line_intersections(m, x1, y1, velocities):
    intersections = []
    for (i, j) in combinations(range(len(m)), 2):
    
        if m[i] == m[j]:  
            continue 

        # Calculate intersection
        x = (m[j] * x1[j] - m[i] * x1[i] + y1[i] - y1[j]) / (m[j] - m[i])
        y = m[i] * (x - x1[i]) + y1[i]

        # Calculate time of intersection
        t_i = (x - x1[i]) / velocities[i][0] if velocities[i][0] != 0 else (y - y1[i]) / velocities[i][1]
        t_j = (x - x1[j]) / velocities[j][0] if velocities[j][0] != 0 else (y - y1[j]) / velocities[j][1]

        # Check if the intersection occurs after time 0 for both lines
        if t_i >= 0 and t_j >= 0:
            intersections.append((x, y))


    return intersections


def parse(input):
    x = []
    y = []
    m = []
    v = []

    for i in input:
        point, vector = i
        x.append(point[0])
        y.append(point[1])
        m.append( vector[1]/ vector[0] )
        v.append(vector)

    x = np.array(x)
    y = np.array(y)
    m = np.array(m)

    return x,y,m,v

def boundary_check(intersections):
    count = 0
    # test case
    # min_x, max_x = 7,27
    # min_y, max_y = 7,27
    # part 1
    min_x, max_x = 200000000000000, 400000000000000
    min_y, max_y = 200000000000000, 400000000000000

    for i in intersections:
        x,y = i
        if min_x <= x <= max_x and min_y <= y <= max_y:
            count += 1
        
    return count


def main(input):
    x,y,m,v = parse(input)
    intersections = line_intersections(m, x, y, v)
    tot = boundary_check(intersections)

    return tot


if __name__ == '__main__':

    # path = r'C:\AOC\2023\Day_24\test_data.txt'
    path = r'C:\AOC\2023\Day_24\data.txt'
    
    with open(path, 'r') as file:
        input = [ [list(map(int, i.split(', ')))[:2] for i in row.strip().split('@')] for row in file.read().splitlines()]
        
        # include z dimension
        # input = [ [list(map(int, i.split(', '))) for i in row.strip().split('@')] for row in file.read().splitlines()]
    
    total = main(input)
    print(total)

  