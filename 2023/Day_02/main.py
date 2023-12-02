def power(rounds):
    contents = {'red':0, 'green':0, 'blue':0}
    
    for round in rounds:
        for bag in round:
            qty, color = bag
            if qty > contents[color]:
                contents[color] = qty

    values = [i for i in contents.values()]
    power = 1

    for i in values:
        power = power * i
   
    return power

def enough(rounds,win):
    for round in rounds:
        for bag in round:
            qty, color = bag
            if qty > win[color]:
                return False
                
    return True

if __name__ == "__main__":
    # path = r'C:\AOC\2023\Day_02\test_data.txt'
    path = r'C:\AOC\2023\Day_02\data.txt'

    with open(path, 'r') as file:
        games = file.read().strip().split('\n')
        parsed_games = {}

        for game in games:
            game_id, game_contents = game.split(':')
            rounds = game_contents.split(';')
            _, game_num = game_id.split(' ')
            game_list = []
            for round in rounds:
                round_list = []
                blocks = round.strip().split(',')
                for block in blocks:
                    qty, color = block.strip().split(' ')
                    round_list.append((int(qty), color))
                game_list.append(round_list)
            parsed_games[int(game_num)] = game_list

    """ part one """
    # contents = {'red':12, 'green':13, 'blue':14}
    # count = 0
    # for k,v in parsed_games.items():
    #     if enough(v,contents):
    #         count += k
    # print(count)

    """ part two """
    count = 0
    for k,v in parsed_games.items():
        count += power(v)
    print(count)
