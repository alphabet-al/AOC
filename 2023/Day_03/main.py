from collections import deque

def check_adj(x, y, grid):
    new_loc = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    is_symbol = False
    is_gear = False
    coor = ()

    for loc in new_loc:
        new_row, new_col = x + loc[0], y + loc[1]
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            new_pt = grid[new_row][new_col]
            if new_pt != '.' and (new_pt.isdigit() is False):
                is_symbol = True
                if new_pt == '*':
                    is_gear = True
                    coor = (new_row, new_col)

    return is_symbol, is_gear, coor
                
    
def combine_digits(dq):
    combined_str = ''
    while dq:
        combined_str += dq.popleft()
    return int(combined_str)


def add_all_parts(schematic):
    sum_pns = 0
    queue = deque()
    gear_dict = {}
    part_number = False
    sum_gear = 0

    # Check each element in grid
    for i in range(len(schematic)):
        for j in range(len(schematic[i])):
            # If the element is a digit, we store in queue and check adjacency to symbol
            if schematic[i][j].isdigit():
                queue.append(schematic[i][j])
                if part_number is False:
                    part_number, is_gear, coor = check_adj(i, j, schematic)
            
            # If the element is not a digit, we check if the number in the queue is a part number
            # If it is then we add to running total
            else:
                if len(queue) != 0 and (part_number is True):
                    num = combine_digits(queue)
                    sum_pns += num
                    
                    if is_gear:
                        if coor in gear_dict.keys():
                            gear_dict[coor].extend([num])
                        else:
                            gear_dict[coor] = [num]

                    queue.clear()
                    part_number = False

                    # special case where number in queue wasn't adjacent to a symbol, meaning
                    # the number is not a part number
                elif len(queue) != 0 and (part_number is False):
                    queue.clear()
                    part_number = False

                    # case where the element is a '.', so we do nothing...
                else:
                    continue

    for k,v in gear_dict.items():
        if len(v) == 2:
            sum_gear += v[0] * v[1]

    return sum_pns, sum_gear


if __name__ == '__main__':
    # path =  r'C:\AOC\2023\Day_03\test_data.txt'
    path =  r'C:\AOC\2023\Day_03\data.txt'

    with open(path, 'r') as file:
        input = file.read().splitlines()
        
    sum_parts, sum_gears = add_all_parts(input)
    print(sum_parts, sum_gears)

    