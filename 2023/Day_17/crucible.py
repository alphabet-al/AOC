import numpy as np
import heapq


class Node:
    def __init__(self, coordinates, cost):
        self.coordinates = coordinates
        self.cost = cost
        self.children = []

    def __lt__(self, other):
        return self.cost < other.cost

    def __repr__(self):
        return f"Node({self.coordinates})"
    
    def __sub__(self, other):
        return self.coordinates - other.coordinates
    
    def set_children(self, grid):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        for dx, dy in directions:
            x, y = self.coordinates
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                child = grid[new_x][new_y]
                self.children.append(child)

# use this as h(n)
def manhattan(n1, n2):
    return abs (n1[0] - n2[0]) + abs (n1[1] - n2[1])


def three_same_dir(path):
    if len(path) < 4:
        return False

    last_direction = None
    same_direction_count = 0

    for i in range(len(path) - 1):
        r, c = path[i]
        next_r, next_c = path[i + 1]
        direction = (next_r - r, next_c - c)

        if direction == last_direction:
            same_direction_count += 1
        else:
            same_direction_count = 1

        if same_direction_count >= 3:
            return True

        last_direction = direction

    return False


# use node values as g(n)
def A_star(grid, start, end):
    # visited contains nodes we have popped off priority queue
    visited = set()
    # priority queue contains tuple of states to be expanded. tuple is in the form of (cost, path, node state).
    fringe = []
    # root_state comprised of start node, empty path list, g_cost, direction, moves in direction
    root_state = (start, [], 0)
    # root_cost is the h_cost of the start state
    root_cost = manhattan(root_state[0].coordinates, end.coordinates) + root_state[-1]
    # push root_cost(fcost of the start state) and root_state(start state) on to priority queue
    heapq.heappush(fringe, (root_cost, root_state))
    
    while fringe:
        # print(fringe)        
        node_f_cost, node_state = heapq.heappop(fringe)
        node, path, node_g_cost = node_state

        if node.coordinates == end.coordinates:
            return node_g_cost, path
       
        if tuple(node.coordinates) not in visited:
            visited.add(tuple(node.coordinates))
            
       # evaluate the child nodes of current node and add to stack if isn't in visited
            for child in node.children:
                if tuple(child.coordinates) not in visited:
                    new_path = path + [child.coordinates]

                    if not three_same_dir(new_path):
                        g_cost = node_g_cost + child.cost
                        # print(g_cost, child.coordinates)
                        newState = (child, new_path, g_cost)
                        # h_cost = manhattan(child.coordinates, end.coordinates)
                        h_cost = 0
                        f_cost = g_cost + h_cost
                        
                        # print(f_cost, child.coordinates)
                        heapq.heappush(fringe, (f_cost, newState))

    return None


def main(data, part_two=False):
    root_node = data[0][0]
    end_node = data[-1][-1]

    heatloss, path = A_star(data, root_node, end_node)


    return heatloss, path

if __name__ == '__main__':

    path = r'C:\AOC\2023\Day_17\test_data.txt'
    # path = r'C:\AOC\2023\Day_17\data.txt'

    with open(path, 'r') as file:
        input = [[int(ch) for ch in i] for i in file.read().splitlines()]
        
        
            
        nodes = [[Node((i,j), input[i][j]) for j in range(len(input[0]))] for i in range(len(input))]

        for i in range(len(input)):
            for j in range(len(input[0])):
                nodes[i][j].set_children(nodes)
                
    total, path = main(nodes, part_two = False)
    print(total)
    
    mapp = np.array(input)
    test = np.zeros_like(mapp)
    print(path)
    for i, coor in enumerate(path):
        r,c = coor
        test[r][c] = i+1
    
    print(test)