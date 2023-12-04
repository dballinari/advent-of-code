import re

# Part 1
def get_num_winning_numbers(row):
    row = re.sub('Card\s+[0-9]+:', '', row)
    row = row[:-1]
    number_columns = row.split('|')
    winning_numbers = number_columns[0].split()
    card_numbers = number_columns[1].split()
    matching_numbers = [num for num in card_numbers if num in winning_numbers]
    return len(matching_numbers)

total_points = 0
with open('2023/input_day4.txt') as f:
    for row in f.readlines():
        num_winning = get_num_winning_numbers(row)
        if num_winning>0:
            total_points+=2**(num_winning-1)
print(total_points)

# Part 2
with open('2023/input_day4.txt') as f:
    rows = f.readlines()
    cards_winning = [1]*len(rows)
    for i, row in enumerate(rows):
        num_winning = get_num_winning_numbers(row)
        for j in range(num_winning):
            cards_winning[i+j+1] += 1*cards_winning[i]
print(sum(cards_winning))

