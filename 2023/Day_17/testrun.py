# %%
import numpy as np
import heapq

# %%
path = r'C:\AOC\2023\Day_17\test_data.txt'
# path = r'C:\AOC\2023\Day_17\data.txt'

# %%
with open(path, 'r') as file:
    input = [[int(ch) for ch in i] for i in file.read().splitlines()]

# %%
class Node:
    def __init__(self, coordinates, cost):
        self.coordinates = coordinates
        self.cost = cost
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self):
        return f"Node({self.coordinates}, Cost: {self.cost})"
    
    def __str__(self):
        return f'{self.cost}'
    
    def __lt__(self, other):
        return self.cost < other.cost
    

class Grid:
    def __init__(self, ascii_map):
        self.grid = self.create_grid(ascii_map)
        self.link_nodes()

    def create_grid(self, ascii_map):
        # Assumes ASCII map is a list of strings, where each string is a row
        node_grid = []
        for x, row in enumerate(ascii_map):
            node_row = []
            for y, char in enumerate(row):
                cost = char  # Assign a default cost or based on specific characters
                node_row.append(Node((x, y), cost))
            node_grid.append(node_row)
        return node_grid

    def link_nodes(self):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                node = self.grid[x][y]
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < len(self.grid) and 0 <= new_y < len(self.grid[0]):
                        child_node = self.grid[new_x][new_y]
                        node.add_child(child_node)

    def get_node(self, position):
        x, y = position
        return self.grid[x][y]

    def __getitem__(self, index):
        return self.grid[index]  

    def __repr__(self):
        return "\n".join([" ".join([repr(cell) for cell in row]) for row in self.grid])
    
    def __str__(self):
        return "\n".join([" ".join([str(cell) for cell in row]) for row in self.grid])




# %%
grid = Grid(input)

print(grid)

# %%
def check_four_consecutive_moves(path):
    if len(path) < 5:
        return False  # Not enough moves to have four consecutive in the same direction

    # Reverse the path and take the last 5 elements from it
    rev_path = path[::-1][:5]

    # Calculate directions for the last four segments of the original path
    directions = [(rev_path[i][0] - rev_path[i+1][0], rev_path[i][1] - rev_path[i+1][1]) for i in range(4)]

    # Check if all four moves are in the same direction
    if all(direction == directions[0] for direction in directions):
        return True  # Invalid path as it contains four consecutive moves in the same direction
    
    return False
    

# use node values as g(n)
def ucs(grid, start, end):
    # visited contains nodes we have popped off priority queue
    # visited = set()
    # priority queue contains tuple of states to be expanded. tuple is in the form of (g_cost, node state -> (node, path))
    fringe = []
    # dictionary to store min g_cost to node. we use it to check if we need to push node back to priority queue if this new
    # path has a lower cost than when we had visited it in the past
    min_costs = {start.coordinates:0}
    # initizalize empty list to store path for each particular node state
    path = [start.coordinates]
    # root_cost is the g_cost of the start state, in this case there is no cost at the start node
    root_cost = 0
    # root_state
    root_state = (start, path)
    # push root_cost(g_cost of the start state) and root_state(start state) on to priority queue
    heapq.heappush(fringe, (root_cost, root_state))
    
    while fringe:
        
        g_cost, node_state = heapq.heappop(fringe)
        node, path = node_state
        
        
        if node.coordinates == end.coordinates:
            return g_cost, path
       
          
       # evaluate the child nodes of current node and add to stack if isn't in visited
        for child in node.children:
            new_path = path + [child.coordinates]
            new_g_cost = g_cost + child.cost

            if not check_four_consecutive_moves(new_path):
                if tuple(child.coordinates) not in min_costs or new_g_cost < min_costs[tuple(child.coordinates)]:
                    min_costs[tuple(child.coordinates)] = new_g_cost
                    heapq.heappush(fringe, (new_g_cost, (child, new_path)))

    return None

# %%
def main(data, part_two=False):
    root_node = data[0][0]
    end_node = data[-1][-1]

    heatloss, path = ucs(data, root_node, end_node)
    
    return heatloss, path

# %%
total, path = main(grid, part_two = False)

# %%
print(total)

# %%
# print(path)


