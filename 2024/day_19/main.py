def howManyConstruct(target, wordbank, memo = None):
    how_many = 0

    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if len(target) == 0:
        return 1
    
    for word in wordbank:
        w = len(word)
        front = target[:w]
        
        if word == front:
            new_target = target[w:]
            how_many += howManyConstruct(new_target, wordbank, memo)
           
    memo[target] = how_many

    return how_many

def canConstruct(target, wordbank, memo = None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if len(target) == 0:
        return True
    
    for word in wordbank:
        w = len(word)
        front = target[:w]
        back = target[-w:]
        
        if word == front:
            new_target = target[w:]
            if canConstruct(new_target, wordbank, memo):
                memo[target] = True
                return True
        elif word == back:
            new_target = target[:-w]
            if canConstruct(new_target, wordbank, memo):
                memo[target] = True
                return True
        
    memo[target] = False
    
    return False

def main(designs, patterns, pt2 = False):
    count = 0
    for target in designs:
        if not pt2:
            if canConstruct(target, patterns):
                count += 1
        else:
            count += howManyConstruct(target, patterns)

    return count


if __name__ == "__main__":
    # path = r"C:\AOC\2024\day_19\test_data.txt"
    path = r"C:\AOC\2024\day_19\data.txt"

    with open(path, "r") as f:
        patterns, designs = f.read().split("\n\n")
        
    patterns = [ch for ch in patterns.split(", ")]
    designs = designs.splitlines()

    print(main(designs, patterns, pt2=True))