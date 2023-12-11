from collections import deque
import numpy as np


legal = {"|" : ("north", "south"), 
         "-" : ("east", "west"),
         "L" : ("north", "east"), 
         "J" : ("north", "west"),
         "7" : ("south", "west"),
         "F" : ("south", "east")
         }

dir = {"north" : (-1, 0),
       "south" : ( 1, 0),
       "east"  : ( 0, 1),
       "west"  : ( 0,-1)
       }

reversed_dir = {"north" : "south",
                "south" : "north",
                "east"  : "west",
                "west"  : "east"
                }

right_side = {"north" : "east",
              "east" : "south",
              "south" : "west",
              "west" : "north"
              }

left_side = {"north" : "west",
              "east" : "north",
              "south" : "east",
              "west" : "south"
              }


q = deque()
start_position_exits = []

def find_direction_by_value(value):
    for key, val in dir.items():
        if val == value:
            return key
    return None

# find coordinates for start position
def find_start(input):
    for i, row in enumerate(input):
        for j, char in enumerate(row):
            if char != 'S':
                continue
            else:
                return (i,j)
            
            
def moves(pos, input, visited):

    if input[pos[0]][pos[1]] == 'S':
        exits = start_position_exits
    else: 
        exits = legal[input[pos[0]][pos[1]]]

    for exit in exits:
        dy,dx = dir[exit]
        if 0 <= pos[0] + dy < len(input) and  0 <= pos[1] + dx < len(input[0]): # check which cardinal directions can be searched given current position on map
            (r,c) = (pos[0] + dy, pos[1] + dx)  # get coordinate for new position and cardinal direction to it. 
            char = input[r][c]
            
            if (r,c) in visited:
                continue
            elif char in legal and reversed_dir[exit] in legal[char]:  # check path is valid from current position to new position and add to queue
                q.append((r,c,))
                    
    return 0

# find exit headings for start position
def find_start_position_exits(pos, input):

    for k,v in dir.items():

        if 0 <= pos[0] + v[0] < len(input) and  0 <= pos[1] + v[1] < len(input[0]): # check which cardinal directions can be searched given current position on map
            (r,c), path_to = (pos[0] + v[0], pos[1] + v[1]), k  # get coordinate for new position and cardinal direction to it. 
            char = input[r][c]
            path_from = reversed_dir[path_to]   # reversed the path_to -> path_from to check if the pipe is valid

            if char in legal and path_from in legal[char]:  # check path is valid from current position to new position and add to queue
                start_position_exits.append(path_to)


def bfs(start, input):
    
    visited = []
    q.append(start)

    while True:
        current_pos = q.popleft()
        
        if current_pos in visited:
            break

        moves(current_pos, input, visited)

        visited.append(current_pos)


    return visited

def check_adj(x, y, grid):
    new_loc = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    coor = ()

    for loc in new_loc:
        new_row, new_col = x + loc[0], y + loc[1]
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            new_pt = grid[new_row][new_col]
            if new_pt != '.':
                is_symbol = True
                if new_pt == '*':
                    is_gear = True
                    coor = (new_row, new_col)

    return is_symbol, is_gear, coor
    

def steps(input):
    start = find_start(input)
    find_start_position_exits(start, input)
    answer = bfs(start, input)
    max_steps = len(answer) / 2
    
    return (int(max_steps), answer)

def find_area(path, grid):
    clockwise = []
    counter_clockwise = []
    count = 0
    
    for i in range(0, len(path), 2):
        clockwise.append(path[i])
    for i in range(1, len(path) + 1, 2):
        counter_clockwise.append(path[i])    

    # for i in range(0, len(path), 2):
    #     counter_clockwise.append(path[i])
    # for i in range(1, len(path) + 1, 2):
    #     clockwise.append(path[i])    

    # print(path)
    # print(clockwise)
    # print(counter_clockwise)

    for j in range(1):
        visited = []

        for i in range(len(clockwise) - 1):
            cr, cc = clockwise[i]
            nr, nc = clockwise[i+1]
            d_vector = (nr - cr, nc - cc)
            direction = find_direction_by_value(d_vector) # traverse direction
            right_direction = right_side[direction] # find right side perpendicular direction of travel
            offset = dir[right_direction]   # offset vector
            # print(offset)
            # take current position and add offset to inspect right side of path....if '.' then turn '.' to '1'
            # add coordinate to visited and count up by one

            dy, dx = (cr + offset[0], cc + offset[1])

            if 0 <= dy < len(grid) and 0 <= dx < len(grid[0]):
                if (dy,dx) not in path:
                    grid[dy][dx] = 'I'
                    path.append((dy,dx))
                    visited.append((dy,dx))
                    # print((dy,dx))
                    count += 1



        for i in range(len(counter_clockwise) - 1):
            cr, cc = counter_clockwise[i]
            nr, nc = counter_clockwise[i+1]
            d_vector = (nr - cr, nc - cc)
            direction = find_direction_by_value(d_vector) # traverse direction
            left_direction = left_side[direction] # find right side perpendicular direction of travel
            offset = dir[left_direction]   # offset vector
            # print(offset)
            # take current position and add offset to inspect right side of path....if '.' then turn '.' to '1'
            # add coordinate to visited and count up by one

            dy, dx = (cr + offset[0], cc + offset[1])
            if 0 <= dy < len(grid) and 0 <= dx < len(grid[0]):
                if (dy, dx) not in path:
                    grid[dy][dx] = 'I'
                    path.append((dy,dx))
                    visited.append((dy,dx))
                    count += 1

        # print(visited)

        new_loc = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        coor = ()

        visited2 = []
        for i in range(1):
            for x,y in visited:
                for loc in new_loc:
                    new_row, new_col = x + loc[0], y + loc[1]
                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                        new_pt = grid[new_row][new_col]
                        if (new_row, new_col) not in path and (new_row, new_col) not in visited2:
                            grid[new_row][new_col] = 'I'
                            path.append((dy,dx))
                            visited2.append((new_row, new_col))
                            count += 1
            visited = visited + visited2
        
        print(len(visited))
        print(len(visited2))
        # print(visited2)
        # for i in grid:
        #     print(i)

        # Join each list into a string
        lines = [''.join(lst) for lst in grid]

        # Join all lines into a single string separated by newlines
        result = '\n'.join(lines)

        print(result)

    # print(grid)
    print(count)



 

if __name__ == '__main__':

    # path = r'C:\AOC\2023\Day_10\test_data5.txt'
    path = r'C:\AOC\2023\Day_10\data.txt'

    with open(path, 'r') as file:
        input = [char for char in file.read().splitlines()]

        # for i in input:
            # print(i)
        
        input2 = [list(i) for i in input]

    answer, pipe_path = steps(input)
    # print( answer )
    
    # array = np.ones((len(input), len(input[0])))

    # for coord in pipe_path:
    #     # Check if the coordinates are within the bounds of the array
    #     if 0 <= coord[0] < array.shape[0] and 0 <= coord[1] < array.shape[1]:
    #         array[coord[0], coord[1]] = 0

    # print(array)
    

    find_area(pipe_path, input2)




