from collections import defaultdict

def find_trailheads(grid):
    starts = []
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            coor = (i, j)
            value = col
            if value == 0:
                starts.append(coor)
    
    return starts

def unique_trails(trailheads, grid, pt2):
    memo = {}
    t_hash = defaultdict(int)
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]    # up, down, left, right


    def dfs(memo, visited, pos, grid):
        count = 0
        r, c = pos
        curr_value = grid[r][c]

       
        if curr_value == 9:
            if not pt2:
                if pos not in visited:  # part 1 only wants to know if there is a valid path to 9, so we only count if we can reach 9 at least once.
                    visited.add(pos)
                    return 1
            else:
                visited.add(pos)    # part 2 condition for valid trail from trailhead counts all paths from trailhead to 9, so we don't need to check if 9 was ever visited, we just count all occurances
                return 1
        
        for direction in dir:
            new_r = r + direction[0]
            new_c = c + direction[1]
            if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
                new_value = grid[new_r][new_c]
                if new_value == curr_value + 1:
                    count += dfs(memo, visited, (new_r, new_c), grid)
        
        return count
                
    for trailhead in trailheads:
        visited = set()
        t_hash[trailhead] = dfs(memo, visited, trailhead, grid)



    return t_hash



def main(grid, pt2 = False):
    trailheads = find_trailheads(grid)   # list of trailheads
    t_hash = unique_trails(trailheads, grid, pt2) # return a hashmap of trailheads with count of hiking trails branching off of each trailhead
    print(t_hash)
    return sum(t_hash.values())

    

if __name__ == "__main__":
    path = r"C:\AOC\2024\day_10\test_data.txt" 
    # path = r"C:\AOC\2024\day_10\data.txt" 

    with open(path, "r") as f:
        grid = [[int(i) for i in row] for row in f.read().strip().splitlines()]

    ans = main(grid, pt2 = True)
    print(f"Sum: {ans}")