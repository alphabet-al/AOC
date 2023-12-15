import re
from collections import deque, defaultdict


def string_value(group):
    curr_value = 0
    for i in group:
        curr_value = ( (curr_value + ord(i)) * 17) % 256
    
    return curr_value


def parse(data):
    split_input = []
    re_pattern = f'(?<=[=-])|(?=[=-])'

    for i in input:
        split_input.append(re.split( re_pattern, i))
    
    return split_input


def remove_by_label(label, dq):
    found = None
    ind = 0
    lens_number = 0
    for index, item in enumerate(dq):
        if item[0] == label:
            found = item
            lens_number = item[1]
            ind = index
    
    if found:
        dq.remove(found)
        return ind, lens_number
    else:
        return found
        
def check_label(label, dq):
    found = False

    for index, item in enumerate(dq):
        if item[0] == label:
            found = True
  
    return found

    
def hashmap(data):
    box = defaultdict(deque)

    # each group is broken into (label, operation, lens number)
    for grp in data:
        print()
        label, op, lens = grp
        # print(label, op, lens)
        # pass label(index 0) to hash function (string_value) to obtain box number
        box_num = string_value(label)
        # print(box_num)
        # each operation(index 1) specifies what to do with the box number we obtained above
        # '-' operation, we remove the lens with specifiec label from the box and move
        # all lenses forward to fill the gap left from us taking the lens out
        if op == '-' and check_label(label, box[box_num]) == False:
            print('{} not in box {}'.format(label, box_num))
            continue
        elif op == '-':
            lr_ind, lr_num = remove_by_label(label, box[box_num])
            print('{} removed from box:{} at index: {}'.format((label, lr_num), box_num, lr_ind))
    
        # '=' operation, we add lens with (label, lens number) to box 
            # if there is already a lens in the box with the same label (label, len number can be different)
            # replace old lens(ot, 9) with new lens (ot, 7), retaining order
            # if there isn't a lens in the box win the same label, add lens to box at the back of the last lens
            # currently in the box.

        if op == '=' and check_label(label, box[box_num]) == True:
            lr_ind, lr_num = remove_by_label(label, box[box_num])
            print("{} added to box".format((label, lens)))
            box[box_num].insert(lr_ind, (label, lens))
            print('{} removed at index: {}'.format((label, lr_num), lr_ind))

        elif op == '=':
            print("{} added to box {}".format((label, lens), box_num))
            box[box_num].append((label, lens))
    
    return box

def focus(box):
    # note : there are 256 boxes in total and all boxes are available, some may have 0 lenses in them

    # focusing power is calculated for each lens:
        # (1 + box number) * (index position of lens in box + 1) * (lens number)
        # sum all focusing power of all lenses 
    
    power = 0
    for k,v in box.items():
        for i in range(1, len(v) + 1):
            focal_length = v[i-1][1]
            power += (k + 1) * (i) * (int(focal_length))

    return power


def main(data,part=1):
    total = 0
    
    if part == 1:
        for grp in data:
            total += string_value(grp)
        return total    

    elif part == 2:
        data = parse(data)
        box_dict = hashmap(data)
        unlimited_power = focus(box_dict)

        return unlimited_power
    
    return "No part specified"

if __name__ == '__main__':

    # path = r'C:\AOC\2023\Day_15\test_data.txt'
    path = r'C:\AOC\2023\Day_15\data.txt'

    with open(path, 'r') as file:
        input = file.read().split(',')

    """ Part 1 """
    # total = main(input)
    # print(total)

    """ Part 2 """
    total = main(input,2)
    print(total)

    