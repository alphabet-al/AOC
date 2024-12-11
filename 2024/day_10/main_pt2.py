from collections import defaultdict
from functools import lru_cache

def find_trailheads(grid):
    starts = []
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == 0:
                starts.append((i, j))  # Find all trailheads
    return starts

def unique_trails(trailheads, grid, pt2):
    t_hash = defaultdict(int)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    @lru_cache(None)
    def dfs(pos, visited):
        count = 0
        r, c = pos
        curr_value = grid[r][c]

        # Base case: If we reach 9
        if curr_value == 9:
            visited = visited | {pos}  # Mark the position as visited (union with the new position)
            return 1 if pt2 else 0  # Return 1 for part 2 (count all paths), 0 for part 1

        # Explore the neighbors
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
                new_value = grid[new_r][new_c]
                if new_value == curr_value + 1 and (new_r, new_c) not in visited:
                    count += dfs((new_r, new_c), visited)  # Recursively explore neighbors

        return count

    for trailhead in trailheads:
        visited = frozenset()  # Use frozenset instead of set
        t_hash[trailhead] = dfs(trailhead, visited)

    return t_hash

def main(grid, pt2=False):
    trailheads = find_trailheads(grid)  # List of all trailheads
    t_hash = unique_trails(trailheads, grid, pt2)  # Map of trailheads with count of unique trails
    print(t_hash)  # Debugging step to visualize trailhead counts
    return sum(t_hash.values())  # Return the sum of all trail counts

if __name__ == "__main__":
    path = r"C:\AOC\2024\day_10\test_data.txt"  # Change to your correct file path

    with open(path, "r") as f:
        grid = [[int(i) for i in row] for row in f.read().strip().splitlines()]  # Convert input grid into integer values

    ans = main(grid, pt2=False)  # Set pt2=True to count all valid trails (for part 2)
    print(f"Sum: {ans}")  # Print the final result
