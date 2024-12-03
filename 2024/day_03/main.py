import re

def parse(input):
    # part 1 criteria
    re_pattern = r"(?:mul\((\d{1,3}),(\d{1,3})\))"
    re_match = re.findall(re_pattern, input)
    
    # part 2 criteria
    # re_pattern = r"(?:don't\(\)(?:(?!do\(\)).)*)|(?:mul\((\d{1,3}),(\d{1,3})\))"
    # re_match = re.findall(re_pattern, input)
    # re_match = [match for match in re_match if all(match)]
        
    return sum([int(x) * int(y) for x,y in re_match])


def main(input):
    print(input)
    ans = 0
    for row in input:
        ans += parse(row)
    return ans 


if __name__ == "__main__":
    # path = 'test_data.txt'
    path = 'data.txt'
    
    with open(path, "r") as f:
        data = f.read().splitlines()
        long_string = ''.join(data)

    result = main(long_string)
    print(f"Result: {result}")