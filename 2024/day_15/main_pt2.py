path = r"C:\AOC\2024\day_15\test_data.txt" 
# path = r"C:\AOC\2024\day_15\data.txt" 

with open(path, "r") as f:
    grid, moves = f.read().split("\n\n")
    grid = [[ch for ch in row] for row in grid.splitlines()]
    moves = [move for move in moves if move != '\n']
    

tile_mapping = {
    "#": "##",
    ".": "..",
    "O": "[]",
    "@": "@."
}    

new_grid = [[char for ch in row for char in tile_mapping[ch]] for row in grid]

movements = {
            "^": (-1, 0),
            "v": (1, 0),
            "<": (0, -1),
            ">": (0, 1)
            }

pos = [(i,j) for i, row in enumerate(new_grid) for j, col in enumerate(row) if col == "@" ]
pos_r, pos_c = pos[0]


def swap(r, c, nr, nc):
    temp = grid[r][c] 
    grid[r][c] = grid[nr][nc]   
    grid[nr][nc] = temp


def move(r, c, dr, dc):
    nr = r + dr
    nc = c + dc

    if new_grid[r][c] == "#":
        return 0

    if new_grid[r][c] == ".":
        return 1

    if new_grid[r][c] == "O":

        if move(nr, nc, dr, dc):
            swap(r, c, nr, nc)
            return 1
        else:
            return 0
        

for dir in moves:
    dr, dc = movements[dir]
    is_path_valid = move(pos_r + dr, pos_c + dc, dr, dc)
    
    if is_path_valid:
        swap(pos_r, pos_c, pos_r + dr, pos_c + dc)
        pos_r, pos_c = (pos_r + dr, pos_c + dc)
        
for row in new_grid:
    print(row)

GPS = [i*100 + j for i, row in enumerate(grid) for j, col in enumerate(grid[0]) if grid[i][j] == "O"]

print(sum(GPS))




    
# check if cell in direction of movement is clear
# if it is then we swap values of new postion with current position
# if it isn't, we check type of obstruction:
    # if it's a wall, we return 0
    # if it's an 'O' then we need to propogate the check forward untill we reach a "." (return 1) or an "#"
        # at which case we do like above, if it's a "." we return 1 or we return 0 if it's a "#", we check if 1 or 0 and swap if 1 and return 0 if 0.
        # once we return back to our current position we move again.

