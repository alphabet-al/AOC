import numpy as np

path = r'C:\AOC\2022\Day14\test_data.txt'
coordinate_tuples = []

with open(path, 'r') as file:
    # Read each line and split into coordinate string pairs
    data = [line.split(' -> ') for line in file.read().splitlines()]
    
    # Now, for each line's data, split each coordinate pair and convert to integer tuples
    for line_data in data:
        for pair in line_data:
            # Handling potential spaces between pairs
            for p in pair.split(' '):
                if p:  # checking if p is not an empty string
                    coordinate_tuples.append(tuple(map(int, p.split(','))))

print(coordinate_tuples)
