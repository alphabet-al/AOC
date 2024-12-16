from collections import deque
import heapq
import copy


def bfs(start, end, grid):
    q = []
    visited = set()
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    heapq.heappush(q, (0, (start, [], 0)) ) 

    while q:
        cost, (pos, path, dir_index) = heapq.heappop(q)
        r, c = pos
        dr, dc = direction[dir_index]
        state = (r, c, dr, dc)
        
        if pos == end:
            return cost, path
        
        if state not in visited:
            visited.add(state)

        for i in range(-1, 2, 1):
            new_dir_index = (dir_index + i) % 4
            ndr, ndc = direction[new_dir_index]
            nr, nc = r + ndr, c + ndc

            if grid[nr][nc] != "#" and (nr, nc, ndr, ndc) not in visited:
                new_path = path + [(nr, nc)]

                if i != 0:
                    new_cost = cost + 1001
                else:
                    new_cost = cost + 1

                heapq.heappush(q, (new_cost, ((nr, nc), new_path, new_dir_index)))
    
    return None


def visualize(path, grid):
    new_grid = copy.deepcopy(grid)

    for coor in path:
        x, y = coor
        new_grid[x][y] = "O"
    
    for row in new_grid:
        print(*row, sep="")


def main(start, end, grid):
    score, path = bfs(start,end, grid)
    visualize(path, grid)
    
    return score, path

if __name__ == "__main__":
    path = r"C:\AOC\2024\day_16\test_data.txt"
    # path = r"C:\AOC\2024\day_16\data.txt"

    with open(path, "r") as f:
        grid = [[ch for ch in row] for row in f.read().splitlines()]

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == "S":
                start = (i, j)
            elif col == "E":
                end = (i, j)
    
    score, path = main(start, end, grid)
    print(score)
    print(len(set(path)))
    print(path)
