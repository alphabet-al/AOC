from collections import defaultdict
import numpy as np


def combo(records):
    race_length = records['Time']
    race_distance = records['Distance']
    combinations = []

    for i in range(len(race_length)):
        t = race_length[i]
        d = race_distance[i]
        count = 0
        for j in range(1, t - 1):
            if j*(t - j) > d:
                count += 1
        if count > 0:
            combinations.append(count)

    return np.prod(combinations)

def combo2(records):
    t = records['Time']
    d = records['Distance']

    valid_p_values = [p for p in range(t + 1) if p * (t - p) > d]

    print(len(valid_p_values))

if __name__ == '__main__':
    # path =  r'C:\AOC\2023\Day_06\test_data.txt'
    path =  r'C:\AOC\2023\Day_06\data.txt'

    with open(path, 'r') as file:
        input = file.read().splitlines()
        records = defaultdict()
                
        for i in input:
            header , values = i.split(':')
            # part 1
            # values = [int(j) for j in values.split()]
            # part 2
            values = [j for j in values.split()]
            joined_string = ''.join(values)
            whole_number = int(joined_string)
            records[header] = whole_number

    # part 1
    # print(combo(records))

    # part 2
    combo2(records)