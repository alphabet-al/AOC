import numpy as np

def points(x):
    pts = 0

    for i in range(x):
        if i == 0:
            pts = 1
        else:
            pts = pts * 2

    return pts

def total(games):
    total = 0
    win_list = []

    for k,v in games.items():
        num_win = len(v[0].intersection(v[1]))
        win_list.append(num_win)
        if num_win > 0:
            total += points(num_win)

    return total, win_list

def lotsa_scratchcards(w_lst, cc):
    card_sum = np.sum(cc)
    prev_cc = cc
    curr_cc = cc
    
    while np.sum(curr_cc) != 0:
        curr_cc = np.zeros_like(cc)
        for ind, val in enumerate(prev_cc):
            for j in range(ind+1, ind + w_lst[ind]+1):
                curr_cc[j] += 1*val
        card_sum += np.sum(curr_cc)
        prev_cc = curr_cc

    print(int(card_sum))

if __name__ == '__main__':
    # path =  r'C:\AOC\2023\Day_04\test_data.txt'
    path =  r'C:\AOC\2023\Day_04\data.txt'

    with open(path, 'r') as file:
        cards = file.read().splitlines()
    
    scratch = {}

    for index, card in enumerate(cards, 1):
        _, numbers = card.split(': ')
        w, p = numbers.split(' | ')
        wins = {int(i) for i in w.split()}
        picks = {int(i) for i in p.split()}
        scratch[index] = [wins, picks]
    
    tot , win_list = total(scratch)
    cardcount = np.ones(len(win_list))
    
    lotsa_scratchcards(win_list, cardcount)

