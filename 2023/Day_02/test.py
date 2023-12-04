path = r'C:\AOC\2023\Day_02\test_data.txt'


with open(path, 'r') as file:
    games = file.read().splitlines()
    
    for i, game in enumerate(games, 1):
        g = game.strip().split(': ')[1].split("; ")

        print(i, g)