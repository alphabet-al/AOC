

def dfs(value, numbers, node_value, index):
    if index + 1 >= len(numbers):
        if node_value == value:
            return True
        else:
            return False
   
    if index + 1 < len(numbers):
        key_s = node_value + numbers[index + 1]
        key_p = node_value * numbers[index + 1]
        # part 2 additional code
        key_c = int(f"{node_value}{numbers[index + 1]}")
         
        s = dfs(value, numbers, key_s, index + 1)
        p = dfs(value, numbers, key_p, index + 1)
        # part 2 additional code
        c = dfs(value, numbers, key_c, index + 1)
        
        # added 'or c' 
        if s or p or c:
            return True
        else:
            return False
  

def test_input(eq):
    index = 0
    target = eq[0] 
    numbers = eq[1]
    initial_node = eq[1][0]
    return dfs(target, numbers, initial_node, index)


def main(input):
    count = 0
    
    for eq in input:
        if test_input(eq):
            count += eq[0]

    return count


if __name__ == "__main__":
    # path = r"C:\AOC\2024\day_07\test_data.txt"
    path = r"C:\AOC\2024\day_07\data.txt"

    with open(path, "r") as f:
        data = f.read().splitlines()
        input = []
        for row in data:
            value, numbers = row.split(":")
            value = int(value)
            numbers = list(map(int, numbers.strip().split(" ")))
            input.append([value, numbers])


    ans = main(input)
    print(f"Total Calibration Result: {ans}")