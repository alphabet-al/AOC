import numpy as np


def parse(input):
    """ Parse input from string input into nested list 
            each row of list is comprised of nested list which comprise list of strings (condition record)
            and tuple (group pattern)
            ex. [ [] , () ]
    """

    data = []
    for group in input:
        record, size = group

        # """ part 2 """
        # record = '?'.join([record]*5)
        # size = ','.join([size]*5)

        # record = [char for char in record]
        size = tuple(int(x) for x in size.split(','))
        data.append([record,size])  
    
    return data


def permute(data, index = 0):
    string, _ = data
     
    if index == len(string):
        return [string]

    if string[index] == '?':
    
        # replace '?' with '#'
        # string[index] = '#'
        string_hash = string[:index] + '#' + string[index + 1:]
        permutations_with_hash = permute((string_hash,_), index + 1)

        # replace '?' with '.'
        # string[index] = '.'
        string_period = string[:index] + '.' + string[index + 1:]
        permutations_with_period = permute((string_period,_), index + 1)

        return permutations_with_hash + permutations_with_period
    else: 
        return permute((string, _), index + 1)


def condition_check(permutations, check):
    valid_count = 0

    for each_permutation in permutations:
        # Split the string into groups separated by '.'
        groups = each_permutation.replace('.', ' ').split()

        # Apply constraints
        if len(groups) == len(check) and all(len(group) == check[i] for i, group in enumerate(groups)):
           
            valid_count += 1

    return valid_count


def main(input):
    valid = 0
    data = parse(input) 
    
    for i in data:
        permutations = permute(i)
        valid += condition_check(permutations, i[1])

    return valid        

if __name__ == '__main__':

    path = r'C:\AOC\2023\Day_12\test_data.txt'
    # path = r'C:\AOC\2023\Day_12\data.txt'

    with open(path, 'r') as file:
        input = [[row for row in line.split(' ')] for line in file.read().splitlines()]

    tots = main(input)
    print(tots)
