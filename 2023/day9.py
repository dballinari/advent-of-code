# Part 1
with open('2023/input_day9.txt', 'r') as f:
    lines = f.read().splitlines()
    sum_next_numbers = 0
    for line in lines:
        numbers = [int(n) for n in line.split()]
        # Prediction of next numbers is the sum of the current number plus all first differences
        next_number = numbers[-1]
        while not all([n==0 for n in numbers]):
            numbers = [numbers[i] - numbers[i-1] for i in range(1, len(numbers))]
            next_number += numbers[-1]
        sum_next_numbers += next_number
 
print(sum_next_numbers)

# Part 2
with open('2023/input_day9.txt', 'r') as f:
    lines = f.read().splitlines()
    sum_previous_numbers = 0
    for line in lines:
        numbers = [int(n) for n in line.split()]
        # Prediction of previous number
        previous_number = numbers[0]
        j = 0
        while not all([n==0 for n in numbers]):
            j+=1
            numbers = [numbers[i] - numbers[i-1] for i in range(1, len(numbers))]
            previous_number = previous_number + (-1)**j * numbers[0]
        sum_previous_numbers += previous_number
 
print(sum_previous_numbers)