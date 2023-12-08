import math

def get_time_range(time, record):
    lower = 0.5*time - 0.5*(time**2 -4*record)**0.5
    upper = 0.5*time + 0.5*(time**2 -4*record)**0.5
    max_distance = time**2/4
    if record > max_distance:
        return None, None
    else:
        return math.ceil(lower), math.floor(upper)

# Part 1
result = 1
with open('2023/input_day6.txt', 'r') as f:
    lines = f.readlines()
    times = lines[0].replace('Time:', '')[:-1].split()
    records = lines[1].replace('Distance:', '').split()
    for time, record in zip(times, records):
        lower, upper = get_time_range(int(time), int(record))
        result *= (upper-lower+1)

print(result)

# Part 2
with open('2023/input_day6.txt', 'r') as f:
    lines = f.readlines()
    times = lines[0].replace('Time:', '')[:-1].split()
    records = lines[1].replace('Distance:', '').split()

    joined_time = int(''.join(times))
    joined_record = int(''.join(records))
    lower, upper = get_time_range(joined_time, joined_record)
    print(upper-lower+1)