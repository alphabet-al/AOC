import numpy as np


def find_reflection_pt(arr, part_two):
    index = 0

    # horizontal reflection
    for i in range(1, arr.shape[0]):
        f_arr = arr[:i]
        arr1 = arr[i:]
        f_arr = np.flip(f_arr, 0)

        # truncate operation
        min_len = min(f_arr.shape[0], arr1.shape[0])
        f_arr = f_arr[:min_len]
        arr1 = arr1[:min_len]

        if not part_two:
            condition = np.all(arr1 == f_arr)
            if condition == True:
                index = i
                break
        else:
            truth = (arr1 == f_arr)
            almost_true = np.sum(truth == False) == 1
            if almost_true == 1:
                index = i
                break

    return index


def main(data, part_two = False):
    # find number of vertical columns before mirror line or number of row before mirror line for each array.
    # append (r,c) into a list.  iterate through list and calculate the sum of all arrays values, but v values stay the same
    # h values are multiplied by 100. ( r = r, c = 100*c )
    r_sum = 0
    c_sum = 0
    
    for array in data:

        r_sum += find_reflection_pt(array, part_two)
        c_sum += find_reflection_pt(array.T, part_two)
    
    return c_sum + (r_sum * 100)


if __name__ == '__main__':

    # path = r'C:\AOC\2023\Day_13\test_data.txt'
    path = r'C:\AOC\2023\Day_13\data.txt'

    with open(path, 'r') as file:
        input = [np.array([[k for k in j] for j in i.split()]) for i in file.read().split('\n\n')]
    
    total = main(input, part_two = True)
    print(total)
