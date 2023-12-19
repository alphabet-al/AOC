import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Polygon, JOIN_STYLE


def get_coordinates(plan, start):
    r, c = start
    vertices = [(r,c)]

    for ins, step in plan:

        if ins == 'U':
            r -= step
        elif ins == 'D':
            r += step
        elif ins == 'L':
            c -= step
        elif ins == 'R':
            c += step

        vertices.append((r,c))

    return vertices

def main(plan):
    start = (0,0)
    vertices = get_coordinates(plan, start)  # find vertices per instructions
    polygon = Polygon(vertices)
    buffered_polygon = polygon.buffer(.5, join_style=JOIN_STYLE.mitre)
    area = buffered_polygon.area
    
    # plot it
    x, y = polygon.exterior.xy
    bx, by = buffered_polygon.exterior.xy

    plt.plot(x, y, label="Original Polygon")
    plt.fill(x, y, alpha=0.3)
    plt.plot(bx, by, label="Buffered Polygon")
    plt.fill(bx, by, alpha=0.3, color='r')
    plt.legend()
    plt.show()

    return area

from functools import reduce

if __name__ == '__main__':

    # path = r'C:\AOC\2023\Day_18\test_data.txt'
    path = r'C:\AOC\2023\Day_18\data.txt'
    
    direction_mapping = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}
    
    with open(path, 'r') as file:
        input = [i for i in file.read().splitlines()]

        dig_plan = []
        dig_plan2 = []
        for i in input:
            dir, spaces, color = i.split()
            color = color.strip('()')
            hex, real_dir = reduce(lambda x, y: x*16 + y, [int(char, 16) for char in color[1:-1]]), direction_mapping[int(color[-1])]
            spaces = int(spaces)
            dig_plan.append((dir, spaces))
            dig_plan2.append((real_dir, hex))
    
    # total = main(dig_plan)
    # print(total)
        
    total = main(dig_plan2)
    print(total)
