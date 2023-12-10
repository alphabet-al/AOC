def extrapolate(array):
    if all(x == 0 for x in array):
        return 0
    
    deltas = [y - x for x,y in zip(array, array[1:])]
    diff = extrapolate(deltas)
    # print(deltas, diff)
    return array[0] - diff



if __name__ == '__main__':
    # path = r'C:\AOC\2023\Day_09\test_data.txt'
    path = r'C:\AOC\2023\Day_09\data.txt'

    with open(path, 'r') as file:
        input = [[int(num) for num in row.split()] for row in file.read().splitlines()]
    
    total = 0

    for i in input:
        x = extrapolate(i)
        # print(i)
        # print(x)
        total += x

    print(total)
