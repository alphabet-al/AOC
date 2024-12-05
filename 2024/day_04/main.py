"""
--- Day 4: Ceres Search ---
"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:


..X...
.SAMX.
.A..A.
XMAS.S
.X....
The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
Take a look at the little Elf's word search. How many times does XMAS appear?

Your puzzle answer was 2514.

--- Part Two ---
The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S
Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?

Your puzzle answer was 1888.
"""




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
    
