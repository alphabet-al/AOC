import copy
import heapq

from collections import deque



def _print(grid):
    for row in grid:
        print(*row, sep = "")


def generate_grid(n, input, grid):
    new_grid = copy.deepcopy(grid)
    for i in range(n):
        r,c = input[i]
        new_grid[r][c] = '#'
    
    return new_grid


def is_valid_move(r, c, grid):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != '#'


# use this as h(n)
def manhattan(n1, n2):
    return abs (n1[0] - n2[0]) + abs (n1[1] - n2[1])


def A_star(grid, start, end):
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]    # up, down, left, right
    # visited contains nodes we have popped off priority queue
    visited = set()
    # priority queue contains tuple of states to be expanded. tuple is in the form of (cost, path, node state).
    fringe = []
    # root_state comprised of start node, empty path list, g_cost, direction
    root_state = (start, [], 0)
    # root_cost is the h_cost of the start state, because the g_cost is 0 at the start...we are at the beginning
    root_cost = manhattan(start, end) + root_state[-1]
    # push root_cost(fcost of the start state) and root_state(start state) on to priority queue
    heapq.heappush(fringe, (root_cost, root_state))
    
    while fringe:      
        node_f_cost, node_state = heapq.heappop(fringe)
        node_coor, path, node_g_cost = node_state

        if node_coor == end:
            return True
            # return node_g_cost, path
       
        if node_coor not in visited:
            visited.add(node_coor)
            
       # evaluate the child nodes of current node and add to stack if isn't in visited
            for dr, dc in dir:
                nr = node_coor[0] + dr
                nc = node_coor[1] + dc

                if (nr, nc) not in visited and is_valid_move(nr, nc, grid):
                    child = (nr, nc)
                    new_path = path + [(nr, nc)]
                    g_cost = node_g_cost + 1
        
                    newState = (child, new_path, g_cost)

                    h_cost = manhattan(child, end)
                    f_cost = g_cost + h_cost
                    
                    # print(f_cost, child.coordinates)
                    heapq.heappush(fringe, (f_cost, newState))

    return False







def main(input):
    grid_shape = (71, 71)
    grid = [["." for _ in range(grid_shape[1])] for _ in range(grid_shape[0])]
    start = (0, 0)
    end = (len(grid[0]) - 1, len(grid[1]) - 1)
    low = 0
    high = len(input) - 1

    while low <= high:
        mid = low + (high - low) // 2
        
        new_grid = generate_grid(mid, input, grid)

        if A_star(new_grid, start, end):
            low = mid + 1
        else:
            high = mid - 1

    print(input[low - 1])
    
    

if __name__ == "__main__":
    # path = r"C:\AOC\2024\day_18\test_data.txt"
    path = r"C:\AOC\2024\day_18\data.txt"

    with open(path, "r") as f:
        input = [tuple(int(ch) for ch in row.split(",")) for row in f.read().splitlines()]
        

    main(input)
