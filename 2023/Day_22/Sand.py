import numpy as np
from collections import defaultdict

class Block:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates

    def __repr__(self):
        return f'{self.name}'

    def cord_update(self):
        start, end = self.coordinates
        start[-1] -= 1
        end[-1] -= 1


def intersect(blk1, blk2):
    start, end = blk1
    start2, end2 = blk2
    if ( max(start[0], start2[0]) <= min( end[0], end2[0] ) ) \
        and ( max( start[1], start2[1] ) <= ( min( end[1], end2[1]) ) )  \
            and ( max( start[2], start2[2] ) <= ( min( end[2], end2[2]) ) ):
        return True
    else:
        return False                                 



def overlap(blk1, blk2):
    start, end = blk1
    start2, end2 = blk2
    if ( max(start[0], start2[0]) <= min( end[0], end2[0] ) ) \
        and ( max( start[1], start2[1] ) <= ( min( end[1], end2[1]) ) ):
        return True
    else:
        return False     


def settle(blks):
        for k,v in blks.items():
            if k == 1:
                continue
            else:                    
                for each_block in v:
                    for lower_block in blks[k - 1]:
                        if not overlap(each_block.coordinates, lower_block.coordinates):
                            print(each_block.coordinates)
                            each_block.cord_update
                            print(each_block.coordinates)
                            # settle(blks)
                            break

def move_block(gameboard, block, to_key, from_key):
    gameboard[to_key] + gameboard[from_key]

G = Block('G', [[1,1,5],[1,1,9]])
F = Block('F', [[0,1,6],[2,1,6]])
E = Block('E', [[2,0,5],[2,2,5]])
D = Block('D', [[0,0,4],[0,2,4]])
gameboard = defaultdict(list)
gameboard[8].append(G)
gameboard[6].append(F)
print(intersect(G.coordinates,F.coordinates))

move_block(gameboard, G, 6, 8)
print(gameboard)

def parse(data):
    block_dict = defaultdict(list)

    for i, row in enumerate(data):
        blocks = [list(map(int, j.split(','))) for j in row.split('~')]
        
        # for index in range(len(blocks[0])):
        #     if abs(blocks[0][index] - blocks[1][index]) > 0:
        #         dim = index
        #         blocks.append(dim)
        
        # dictionary holding block information (block start coor, block end coor,
        # varying dim such that we can iterate over the range)

        
                
        block_dict[blocks[0][-1]].append(Block(i,blocks))


    return block_dict    

def main(data):
    blks = parse(data)
    # for k,v in reversed(blks.items()):
    #     print(k,v)
    # blks = settle(blks)
    # print(intersect(blks[0], blks[2]))
    


if __name__ == '__main__':

    path = r'C:\AOC\2023\Day_22\test_data.txt'
    # path = r'C:\AOC\2023\Day_22\data.txt'
    
    with open(path, 'r') as file:
        input = file.read().splitlines()

        
    total = main(input)
    print(total)

