from collections import Counter, defaultdict

def in_bounds(r,c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
    
def dfs(r, c, curr_region, visited):
    dir = [(-1,0), (1,0), (0,-1), (0,1)]
    path = [(r, c)]
        
    if grid[r][c] != curr_region:
        return []

    if (r, c) not in visited:
        visited.add((r,c))
  
    for dr, dc in dir:
        nr = r + dr
        nc = c + dc

        if in_bounds(nr,nc) and (nr,nc) not in visited:
            dfs_area = dfs(nr, nc, curr_region, visited)
            path.extend(dfs_area)
                
    return path


def calculate_price(grid):
    visited = set()

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if (r,c) not in visited:
                path = dfs(r, c, ch, visited)
                print(path)
    return



def main(grid):

    return calculate_price(grid)

    

if __name__ == "__main__":
    path = r"C:\AOC\2024\day_12\test_data.txt" 
    # path = r"C:\AOC\2024\day_12\data.txt" 

    with open(path, "r") as f:
        data = f.read()
        # regions = Counter(data)
        grid = [[ch for ch in row] for row in data.splitlines()]
        
    
    total = main(grid)
    print(f"Price: {total}")