from collections import defaultdict

def find_trailheads(grid):
    starts = []
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == 0:  # Trailheads start at 0
                starts.append((i, j))
    return starts

def unique_trails(trailheads, grid):
    memo = {}  # Memoization dictionary
    t_hash = defaultdict(int)  # Dictionary for storing results
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Directions: up, down, left, right

    def dfs(pos):
        r, c = pos
        curr_value = grid[r][c]

        # Base case: Reached the end
        if curr_value == 9:
            return 1

        # Memoization key: position
        if pos in memo:
            return memo[pos]

        count = 0
        # Explore neighbors
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
                new_value = grid[new_r][new_c]
                if new_value == curr_value + 1:
                    count += dfs((new_r, new_c))

        memo[pos] = count  # Store in memoization table
        return count

    for trailhead in trailheads:
        t_hash[trailhead] = dfs(trailhead)

    return t_hash

def main(grid):
    trailheads = find_trailheads(grid)  # Find all trailheads (start points)
    t_hash = unique_trails(trailheads, grid)  # Count unique trails
    print(t_hash)
    return sum(t_hash.values())  # Total unique trails

if __name__ == "__main__":
    path = r"C:\AOC\2024\day_10\test_data.txt"  # Update with the correct file path

    with open(path, "r") as f:
        grid = [[int(i) for i in row] for row in f.read().strip().splitlines()]

    ans = main(grid)
    print(f"Sum: {ans}")
