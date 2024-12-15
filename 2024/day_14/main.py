
def move_robots(time, robots, grid):
    for k,v in robots.items():
        robots[k][0] = [(v[0][0] + (v[1][0] * time)) % grid[0], (v[0][1] + (v[1][1] * time)) % grid[1]]

    return robots
    

def quadrant_count(m, grid):
    x,y = grid 
    mid_x, mid_y = x//2, y//2
    q1 = q2 = q3 = q4 = 0

    # q1 | q2
    # -------
    # q3 | q4
    
    for pos,vel in m.values():
        rx, ry = pos
        if rx < mid_x and ry < mid_y:
            q1 += 1
        elif rx > mid_x and ry < mid_y:
            q2 += 1
        elif rx < mid_x and ry > mid_y:
            q3 += 1
        elif rx > mid_x and ry > mid_y:
            q4 += 1

    return q1 * q2 * q3 * q4



def main(robots):
    # grid = (11, 7)  # test grid size
    grid = (101, 103) # puzzle input grid size
    t = 100
    moved_robots = move_robots(t, robots, grid)
    product = quadrant_count(moved_robots, grid)
    return product
    

if __name__ == "__main__":
    # path = r"C:\AOC\2024\day_14\test_data.txt" 
    path = r"C:\AOC\2024\day_14\data.txt" 

    with open(path, "r") as f:
        input = f.read().splitlines()
        robots = {}
        for i, row in enumerate(input):
            f,b = row.split(" ")
            p = list(map(int, f.split("=")[1].split(",") ))
            v = list(map(int, b.split("=")[1].split(",") ))
            robots[i] = [p,v]
    
    sf = main(robots)
    print(f"Safety Factor: {sf}")