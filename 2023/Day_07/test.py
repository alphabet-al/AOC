from collections import Counter

def check_hand(hand_tuple):
    # Hand ranking values
    hand_values = {
        "Five of a Kind": 7,
        "Four of a Kind": 6,
        "Full House": 5,
        "Three of a Kind": 4,
        "Two Pair": 3,
        "One Pair": 2,
        "High Card": 1
    }

    # Extract the hand (first element of the tuple)
    hand = hand_tuple[0]

    # Count occurrences of each card (excluding Jokers)
    counts = Counter(card for card in hand if card != 'J')
    num_jokers = hand.count('J')

    # Adjust counts with Jokers
    for _ in range(num_jokers):
        if counts:
            most_common_card, most_common_count = counts.most_common(1)[0]
            counts[most_common_card] += 1
        else:
            counts['J'] = num_jokers  # All cards are Jokers

    values_list = list(counts.values())

    # Check for each type of hand
    if 5 in values_list:
        return hand_values["Five of a Kind"]
    if 4 in values_list:
        return hand_values["Four of a Kind"]
    if 3 in values_list and 2 in values_list:
        return hand_values["Full House"]
    if 3 in values_list:
        return hand_values["Three of a Kind"]
    if values_list.count(2) == 2:
        return hand_values["Two Pair"]
    if 2 in values_list:
        return hand_values["One Pair"]


if __name__ == '__main__':
    path =  r'C:\AOC\2023\Day_07\test_data.txt'
    # path =  r'C:\AOC\2023\Day_07\data.txt'

    with open(path, 'r') as file:
        hands = [(x, int(y)) for x,y in (i.split() for i in file.read().splitlines())]

    value = check_hand(hands[1])
    print(value)
