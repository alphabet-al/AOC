from collections import defaultdict
import copy 

def in_bounds(coor, grid):
    return 0 <= coor[0] < len(grid) and 0 <= coor[1] < len(grid[0])

def get_slope(a,b):
    ar, ac = a
    br, bc = b

    return br - ar, bc - ac


def parse(grid):
    ant = defaultdict(list)
    for i, row in enumerate(grid):
        for j, col in enumerate(grid[0]):
            if grid[i][j].isalnum():
                ant[grid[i][j]].append((i,j))
    return ant

def antinode(ant, grid):
    antinodes = set()
    for k,v in ant.items():
        for i in range(len(v) - 1):
            for j in range(i + 1, len(v)):
                rise, run = get_slope(v[i], v[j])
                antinode_1 = (v[i][0] - rise, v[i][1] - run)
                antinode_2 = (v[j][0] + rise, v[j][1] + run)
                antinodes.add(v[i])
                antinodes.add(v[j])


                while in_bounds(antinode_1, grid):
                    antinodes.add(antinode_1)
                    antinode_1 = (antinode_1[0] - rise, antinode_1[1] - run)

                while in_bounds(antinode_2, grid):
                    antinodes.add(antinode_2)
                    antinode_2 = (antinode_2[0] + rise, antinode_2[1] + run)

    return antinodes

def visualization(coor, grid):
    vis_grid = copy.deepcopy(grid)
    for r,c in coor:
        vis_grid[r][c] = '#'
    for row in vis_grid:
        print(row)
    return vis_grid

def main(grid):
    ant = parse(grid)
    antinode_coordinates = antinode(ant, grid)
    vis_grid = visualization(antinode_coordinates, grid)
   
    return len(antinode_coordinates)

if __name__ == "__main__":
    # path = r"C:\AOC\2024\day_08\test_data.txt" # 12 x 12 test grid
    # patht = r"C:\AOC\2024\day_08\test_grid.txt" # 12 x 12 test grid
    path = r"C:\AOC\2024\day_08\data.txt" # 50 x 50 grid

    with open(path, "r") as f:
        grid = [[ch for ch in row] for row in f.read().splitlines()]
    # with open(patht, 'r') as f:
    #     test_grid = [[ch for ch in row] for row in f.read().splitlines()]
        
    # grid = f.read()
    # cnt = Counter(grid)
    # print(cnt)

    # for row in grid:
    #     print(row)  

    
    ans = main(grid)
    print(f"Total Number of Unique Locations: {ans}")