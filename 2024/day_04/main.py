from collections import deque
import numpy as np

def find_M(r, c, dr, dc, grid, word):
    rNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
    cNbr = [-1, 0, 1, -1, 1, -1, 0, 1]

    letter = word.popleft()

    count = 0
    for k in range(8):
        newR = r + rNbr[k]
        newC = c + cNbr[k]
        if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]) and grid[newR][newC] == letter:

            count += dfs(newR, newC, rNbr[k], cNbr[k], grid, word.copy())
        
    return count


def dfs(r, c, rNbr, cNbr, grid, word):
    # depth first search in direction of travel
    
    if len(word) == 0:
        return 1
      
    letter = word.popleft()

    count = 0
    newR = r + rNbr
    newC = c + cNbr

    if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]) and grid[newR][newC] == letter:
        count += dfs(newR, newC, rNbr, cNbr, grid, word.copy())
        
    return count

def main(grid, pt2=False):
    word = deque(["M", "A", "S"])
    visited = set()
    count = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "X" and (y,x) not in visited:
                visited.add((y,x))
                dr = dc = None
                count += find_M(y, x, dr, dc, grid, word.copy())

    return count

def main_pt2(number_grid):
    count = 0
    # kernel's have to have the same shape....in this case 3x3
    kernel1 = np.array([ [2, 0, 2],
                         [0, 3, 0],
                         [4, 0, 4]
                        ])
    
    kernel2 = np.array([ [4, 0, 4],
                         [0, 3, 0],
                         [2, 0, 2]
                        ])
    
    kernel3 = np.array([ [4, 0, 2],
                         [0, 3, 0],
                         [4, 0, 2]
                        ])
    
    kernel4 = np.array([ [2, 0, 4],
                         [0, 3, 0],
                         [2, 0, 4]
                        ])
    
    kernels = [kernel1, kernel2, kernel3, kernel4]
    
    mask = np.array([    [1, 0, 1],
                         [0, 1, 0],
                         [1, 0, 1]
                        ])

    grid_rows, grid_cols = number_grid.shape
    k_rows, k_cols = kernel1.shape

    output_rows = grid_rows - k_rows + 1
    output_cols = grid_cols - k_cols + 1

    for i in range(output_rows):
        for j in range(output_cols):
            sub_grid = number_grid[i:i+k_rows, j:j+k_cols]
            for k in kernels:
                if np.array_equal(sub_grid[mask == 1], k[mask == 1]):
                    count += 1

    return count

if __name__ == "__main__":
    # path = r"C:\AOC\2024\day_04\test_data.txt"
    path = r"C:\AOC\2024\day_04\data.txt"

    with open(path, "r") as f:
        grid = f.read().splitlines()
        
    # how_many = main(grid, pt2 = False)
    # print(f"Number of 'XMAS' words: {how_many}")

    letter_to_number = {"X":1, "M":2, "A":3, "S":4}
    number_grid = np.array([[letter_to_number[letter] for letter in row]for row in grid])
    
    how_many2 = main_pt2(number_grid)
    print(f"Number of 'XMAS' words: {how_many2}")
    
