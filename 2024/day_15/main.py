
def main(robots):
    pass

if __name__ == "__main__":
    # path = r"C:\AOC\2024\day_15\test_data.txt" 
    path = r"C:\AOC\2024\day_15\data.txt" 

    with open(path, "r") as f:
        input = f.read().splitlines()
        robots = {}
        for i, row in enumerate(input):
            f,b = row.split(" ")
            p = list(map(int, f.split("=")[1].split(",") ))
            v = list(map(int, b.split("=")[1].split(",") ))
            robots[i] = [p,v]
    
    sf = main(robots)
    print(f"Safety Factor: {sf}")