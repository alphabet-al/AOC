# parse seeds from input, store as a list
# parse maps, store in dict....map['soil'] = [dest, source, length]

# convert function(number, map list)
# map list = [destination, source, range length]
# number = seed
# loop through list and check if (seed >= source < source + range length):
# if true, destination = seed - source + destination
# else continue
# return destination

# for each seed number, input seed number into convert function and store 
# as current destination number
# loop through all maps (soil, fertilizer, water, light, temperature, humidity and location)
# for k,v in map_dict.values():
# convert function (number, v)
# final number is location number 

# seed number -> soil number -> etc...
# source numbers not mapped are the same destination

from collections import defaultdict
import numpy as np

def convert(seed_num, mapp):
    y = seed_num

    for entry in mapp:
        dest, source, length = entry
        if (source <= seed_num < source + length):
            y = seed_num - source + dest

    if y == seed_num:
        return seed_num
    else:
        return y
    

def location(seeds, map_dict):
    loc = []

    master_seed_list = []

    for seed_range in seeds:
        seed_list = []
        for seed in range(seed_range[0], seed_range[0] + seed_range[1]):
            seed_list.append(seed)
        master_seed_list.append(np.array(seed_list))

    # print(master_seed_list)

    for seeds in master_seed_list:
        for seed in seeds:
            for k,v in map_dict.items():
                seed = convert(seed, v)
            loc.append(seed)
    
    return min(loc)


def convert2(seed_array, mapp):
    y = np.copy(seed_array)

    for i, entry in enumerate(mapp):
        dest, source, length = entry
        mask = (source <= seed_array) & (seed_array < source + length)
        y[mask] = seed_array[mask] - source + dest
    return y
    

def location2(seeds, map_dict):
    loc = []
    master_seed_list = []

    for seed_range in seeds:
        seed_list = []
        for seed in range(seed_range[0], seed_range[0] + seed_range[1]):
            seed_list.append(seed)
        master_seed_list.append(np.array(seed_list, dtype=np.int64))

    for seed in master_seed_list:
        for k,v in map_dict.items():
            seed = convert2(seed, v)
        loc.append(np.min(seed))

    return min(loc)

if __name__ == '__main__':
    path =  r'C:\AOC\2023\Day_05\test_data.txt'
    # path =  r'C:\AOC\2023\Day_05\data.txt'

    with open(path, 'r') as file:
        almanac = file.read().split('\n\n')

        _, seeds = almanac[0].split(': ')
        seeds = [int(i) for i in seeds.split()]
        seed_range = []
        for i in range(0, len(seeds), 2):
            seed_range.append((seeds[i],seeds[i+1])) 

        map_dict = defaultdict()

        for line in almanac[1:]:
            map_name = line.split('\n')[0].split(' ')[0].split('-')[-1]
            map_list = [list(map(int, i.split())) for i in line.split(':\n')[1].split('\n')]
            map_dict[map_name] = map_list
        
    # loc = location(seeds, map_dict)
    # print(loc)

    loc2 = location2(seed_range, map_dict)
    print(loc2)
