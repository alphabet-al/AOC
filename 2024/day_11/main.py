from functools import cache

@cache
def apply_rule(n, stone):
    # here we will check the stone value and apply a rule that is applicable, we will return the result
    if n == 0:
        return 1
    
    stone_string = str(stone)
    stone_len = len(stone_string)
    mid = stone_len // 2

    if stone == 0:
        return apply_rule(n - 1, 1)
    elif stone_len % 2 == 0:
        stone_left = stone_string[:mid]
        stone_right = stone_string[mid:]
        left_tree = apply_rule(n - 1, int(stone_left))
        right_tree = apply_rule(n - 1, int(stone_right))
        return(left_tree + right_tree)
    else:
        return apply_rule(n - 1, stone * 2024)
    

def blink(n, stones):
    # for each stone in stones, 'apply_rule' function and concatenate the answer with each stone and return to calling function
    count = 0

    for stone in stones:
        count += apply_rule(n, stone)   

    return count
   

if __name__ == "__main__":
    # path = r"C:\AOC\2024\day_11\test_data.txt" 
    path = r"C:\AOC\2024\day_11\data.txt" 

    with open(path, "r") as f:
        stones = [int(ch) for ch in f.read().split()]

    stone_count = blink(75, stones)
    print(f"Sum: {stone_count}")