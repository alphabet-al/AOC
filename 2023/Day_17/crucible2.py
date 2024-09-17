import numpy as np

def main(data, part_two=False):
    pass

if __name__ == '__main__':

    path = r'C:\AOC\2023\Day_17\test_data.txt'
    # path = r'C:\AOC\2023\Day_17\data.txt'

    with open(path, 'r') as file:
        input = [[int(ch) for ch in i] for i in file.read().splitlines()]
        print(input)
        # nodes = [[Node((i,j), input[i][j]) for j in range(len(input[0]))] for i in range(len(input))]

        # for i in range(len(input)):
            # for j in range(len(input[0])):
                # nodes[i][j].set_children(nodes)
                
    # total, path = main(nodes, part_two = False)
