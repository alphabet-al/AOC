import numpy as np

# coor_sys = {"north" : np.array([[1, 0],[0, 1]]),
#             "south" : np.array([[-1, 0],[0, -1]]),
#             "east"  : np.array([[0, 1],[-1, 0]]),
#             "west"  : np.array([[0, -1],[1, 0]])
#            }


dir = {"north" : (-1, 0),
       "south" : ( 1, 0),
       "east"  : ( 0, 1),
       "west"  : ( 0,-1)
       }

def swap(curr_xy, direction, data):
    # recursive function that swaps current element, if a swappable element, with the next
    # element in the passed direction

    curr_row, curr_col = curr_xy
    
    # dy, dx = dir[direction]
    # next_row, next_col = (curr_row + dy), (curr_col + dx)
    ele = data[curr_row][curr_col]
    next_ele = data[curr_row][curr_col - 1]

    # print((curr_row,curr_col), ele, (next_row, next_col), next_ele)

    if curr_col == 0:
        return 0
    elif ele != 'O' or next_ele != '.':
        return 0
    else:
        temp = next_ele
        data[curr_row][curr_col - 1] = ele
        data[curr_row][curr_col] = temp
        swap((curr_row, curr_col - 1), direction, data)
    
    return 0


def tilt(data, dir):
    # loop through each element and swap current element with element in next direction (dir)
    # 
    # print(id(data))

    if dir == 'north':
        data = np.transpose(data)
                
        for i in range(len(data)):   
            for j in range(1, len(data[0])):
                coor = (i, j)
                swap(coor, dir, data)
  
    elif dir == 'cycle':
        # cycles = 1_000_000_000
        cycles = 100000

        for cycle in range(cycles):
            for k in range(4):
                if k == 0:
                    data = np.transpose(data)
                elif k == 2:
                    data = np.flipud(data)
                    data = np.transpose(data)
                elif k == 3:
                    data == np.fliplr(data)                                                           

                for i in range(len(data)):   
                    for j in range(1, len(data[0])):
                        coor = (i, j)
                        swap(coor, dir, data)

                if k == 0:
                    data = np.transpose(data)
                elif k == 2:
                    data = np.transpose(data)
                    data = np.flipud(data)
                elif k == 3:
                    data == np.fliplr(data) 




    # data = np.transpose(data)
    counts = np.count_nonzero(data == 'O', axis=1)
    total = sum(counts[i] * (len(counts) - i) for i in range(len(counts)))
    
    return total



def main(data):
    # print(id(data))
    return tilt(data, 'north')

if __name__ == '__main__':

    path = r'C:\AOC\2023\Day_14\test_data.txt'
    # path = r'C:\AOC\2023\Day_14\data.txt'

    with open(path, 'r') as file:
        input = np.array( [[j for j in i] for i in file.read().splitlines()] )
    # print(id(input))
    total = main(input)
    print(total)