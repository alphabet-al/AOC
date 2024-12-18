from collections import Counter, defaultdict

def in_bounds(r,c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
    
def dfs(r, c, curr_region, visited):
    dir = [(-1,0), (1,0), (0,-1), (0,1)]
    perimeter = 0
    area = 1
    
    if not in_bounds(r,c) or grid[r][c] != curr_region:
        return 0,1
    
    if (r, c) in visited:
        return 0,0
    
    visited.add((r,c))
    
    for dr, dc in dir:
        nr = r + dr
        nc = c + dc
    
        dfs_area, dfs_perimeter = dfs(nr, nc, curr_region, visited)
        area += dfs_area
        perimeter += dfs_perimeter
        
        
    return area, perimeter
  


def calculate_price(grid):
    price = 0
    visited = set()

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            area, perimeter= dfs(r, c, ch, visited)
            price += (area * perimeter)
    return price



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