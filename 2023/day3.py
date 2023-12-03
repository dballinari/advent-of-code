import re
from functools import reduce

# Part 1
number_sum = 0
with open('2023/input_day3.txt', 'r') as f:
    rows = f.readlines()
    n = len(rows)
    for i, row in enumerate(rows):
        # remove line break symbol
        row = row[:-1]
        # index of symbols around current row
        symbols_idx = [idx for idx, s in enumerate(row) if s!='.' and not s.isnumeric()]
        symbols_idx_before = [idx for idx, s in enumerate(rows[i-1][:-1]) if s!='.' and not s.isnumeric()] if i > 0 else []
        symbols_idx_after = [idx for idx, s in enumerate(rows[i+1][:-1]) if s!='.' and not s.isnumeric()] if i < n-1 else []
        symbols_idx_joint = set(symbols_idx+symbols_idx_before+symbols_idx_after)

        for num in re.finditer(r'[0-9]+', row):
            start, end = num.span()
            value = int(num.group())
            valid_number = False
            for valid_idx in range(start-1, end+1):
                valid_number = valid_idx in symbols_idx_joint
                if valid_number:
                    number_sum += value
                    break
                    
print(number_sum)

# Part 2
def find_numbers_in_row(row):
    return [(num.span(), num.group()) for num in re.finditer(r'[0-9]+', row)]

sum_gear_ratios = 0
with open('2023/input_day3.txt', 'r') as f:
    rows = f.readlines()
    n = len(rows)
    for i, row in enumerate(rows):
        # remove line break symbol
        row = row[:-1]
        # find numbers and their position in the current, previous and next row
        numbers = find_numbers_in_row(row)
        numbers_before = find_numbers_in_row(rows[i-1][:-1]) if i > 0 else []
        numbers_after = find_numbers_in_row(rows[i+1][:-1]) if i < n-1 else []
        # find position of "*" in the current row
        idx_gear = [idx for idx, s in enumerate(row[:-1]) if s=='*']
        for idx in idx_gear:
            gear_ratio_numbers = [int(num) for (start, end), num in numbers+numbers_after+numbers_before if idx >= start-1 and idx <= end]
            if len(gear_ratio_numbers)==2:
                sum_gear_ratios+=reduce(lambda x,y: x*y, gear_ratio_numbers)

print(sum_gear_ratios)