memo = {}

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
        record = '?'.join([record]*5)
        size = ','.join([size]*5)

        # record = [char for char in record]
        size = tuple(int(x) for x in size.split(','))
        data.append([record,size])  
    
    return data


def count(cfg, nums):
    if cfg == '':
        return 1 if nums == () else 0
    
    if nums == ():
        return 0 if '#' in cfg else 1
    
    key = (cfg, nums)

    if key in memo:
        return memo[key]

    results = 0
    
    if cfg[0] in '.?':
        results += count(cfg[1:], nums)
    
    if cfg[0] in '#?':
        if nums[0] <= len(cfg) and '.' not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != '#'):
            results += count(cfg[nums[0] + 1:], nums[1:])

    memo[key] = results

    return results


def main(input):
    valid = 0
    data = parse(input) 
    
    for cfg, nums in data:
        valid += count(cfg, nums)

    return valid        

if __name__ == '__main__':

    # path = r'C:\AOC\2023\Day_12\test_data.txt'
    path = r'C:\AOC\2023\Day_12\data.txt'

    with open(path, 'r') as file:
        input = [[row for row in line.split(' ')] for line in file.read().splitlines()]

    total = main(input)
    print(total)