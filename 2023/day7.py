# Part 1
card_rank = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, **{str(i): i for i in range(9,0,-1)}}

def get_number_repetitions(x: list):
    unique_values = set(x)
    return sorted([x.count(u) for u in unique_values], reverse=True)

def get_hand_value(hand: list):
    card_value = [card_rank.get(c) for c in hand]
    hand_rank = [(6, [5]), (5, [4,1]), (4, [3,2]), (3, [3,1,1]), (2, [2,2,1]), (1, [2, 1, 1, 1]), (0, [1]*5)]
    unique_values = get_number_repetitions(hand)
    hand_value = None
    for value, comb in hand_rank:
        if unique_values == comb:
            hand_value = value
            break

    return [hand_value] + card_value

with open('2023/input_day7.txt', 'r') as f:
    all_hands = []
    for line in f.readlines():
        hand = [c for c in line.split()[0]]
        bid = int(line.split()[1])
        hand_value = get_hand_value(hand)
        all_hands.append((bid, hand_value, hand))

sorted_hands = sorted(all_hands, key=lambda x: tuple(x[1]))
print(sum([(i+1)*bid for i, (bid, _, _) in enumerate(sorted_hands)]))


# Part 2
card_rank = {'A': 13, 'K': 12, 'Q': 11, 'T': 10, **{str(i): i for i in range(9,0,-1)}, 'J': 0}

def get_value_type(x):
    num_rep = get_number_repetitions(x)
    hand_rank = [(6, [5]), (5, [4,1]), (4, [3,2]), (3, [3,1,1]), (2, [2,2,1]), (1, [2, 1, 1, 1]), (0, [1]*5)]
    for value, comb in hand_rank:
        if num_rep == comb:
            return value

def get_hand_value(hand: list):
    card_value = [card_rank.get(c) for c in hand]
    unique_values = set(hand)
    if 'J' not in unique_values or len(unique_values)==1:
        # if there is no joker or only one type of card is in the hand, we compute normally the value
        hand_value = get_value_type(hand)
    else:
        # otherwise, replace each of the unique values that are not a joker in the hand, trying to fund the best hand value
        hand_value = 0
        for u in unique_values:
            if u == 'J':
                continue
            candidate_value = get_value_type([c if c!='J' else u for c in hand])
            if candidate_value > hand_value:
                hand_value = candidate_value
        
    return [hand_value] + card_value


with open('2023/input_day7.txt', 'r') as f:
    all_hands = []
    for line in f.readlines():
        hand = [c for c in line.split()[0]]
        bid = int(line.split()[1])
        hand_value = get_hand_value(hand)
        all_hands.append((bid, hand_value, hand))

# sort by the entire tuple made of hand value, card 1 value, card 2 value, ...
sorted_hands = sorted(all_hands, key=lambda x: tuple(x[1]))
print(sum([(i+1)*bid for i, (bid, _, _) in enumerate(sorted_hands)]))