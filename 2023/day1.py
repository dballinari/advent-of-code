import re

# Part 1
sum_first_last = 0
with open('2023/input_day1.txt') as f:
    for row in f.readlines():
        numbers = re.findall('[0-9]', row)
        sum_first_last += int(numbers[0]+numbers[-1])

print(sum_first_last)


# Part 2
str_nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
map_nums = {s: str(i+1) for i,s in enumerate(str_nums)}
expr = '|'.join(['[0-9]'] + str_nums)

def parse_number(num):
    if num.isnumeric():
        return num
    else:
        return map_nums[num]

def find_num_first(w):
    matched_num = re.findall(expr, w)[0]
    return parse_number(matched_num)
    
def find_num_last(w):
    w_rev_seq = ''
    for s in w[::-1]:
        w_rev_seq=s+w_rev_seq
        matched_num = re.findall(expr, w_rev_seq)
        if len(matched_num)==0:
            continue
        return parse_number(matched_num[-1])
        
sum_first_last = 0
with open('2023/input_day1.txt') as f:
    for row in f.readlines():
        first_number = find_num_first(row)
        last_number = find_num_last(row)
        sum_first_last += int(first_number+last_number)
print(sum_first_last)