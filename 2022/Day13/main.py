import numpy as np
import json

path = r'C:\AOC\2022\Day13\data.csv'
data = []

# Load JSON data from a file
with open(path, 'r') as file:
    input = file.readlines()

    for i in range(0, len(input), 3):
        data.append([json.loads(input[i]), json.loads(input[i+1])])

def compare(var1, var2):
    if isinstance(var1, int) and isinstance(var2, int):
        if var1 < var2:
            return True
        elif var1 > var2:
            return False
        return None
    elif isinstance(var1, list) and isinstance(var2, list):
        for i in range(len(var1)):
            if i == len(var2):
                return False
            truth = compare(var1[i], var2[i])
            if truth != None:
                return truth
        if len(var1) == len(var2):
            return None
        return True
        
    if isinstance(var2, int):
        return compare(var1, [var2])
    elif isinstance(var1, int):
        return compare([var1], var2)

total = 0            
for i in range(len(data)):
    x = compare(data[i][0], data[i][1])
    if x == True or x == None:
        total += i+1 
        print("index: {} Value: {}".format(i+1, total))

print(total)
