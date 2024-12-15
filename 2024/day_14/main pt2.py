import numpy as np

def move_robots(time, robots, grid):
    locations = []
    for k,v in robots.items():
        locations.append([(v[0][0] + (v[1][0] * time)) % grid[0], (v[0][1] + (v[1][1] * time)) % grid[1]])
    
    
    return locations
    
def is_symmetric(data):
    points = set(map(tuple, data))

    for x,y in points:
        if (-x,y) not in points:
            return False

    return True

def main(robots):
    # grid = (11, 7)  # test grid size
    grid = (101, 103) # puzzle input grid size
    t = 0
        
    while True:
        t += 1
        
        robot_loc = move_robots(t, robots, grid)
        robot_loc = np.array(robot_loc)
        robot_loc[:,0] -= 5 
        
        print(robot_loc)
        
        if is_symmetric(robot_loc):
            break
        
        print(t)
    return t
    

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
    
    print(main(robots))