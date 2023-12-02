import re

# Part 1
bag = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def get_id(s):
    return int(re.search('(?<=Game\s)[0-9]+', s).group())

def is_game_valid(s):
    for c, n in bag.items():
        n_c = re.search(f'[0-9]+(?=\s{c})', s)
        if not n_c:
            continue
        n_c = int(n_c.group())
        if n_c > n:
            return False
    return True

ids = 0
with open('2023/input_day2.txt', 'r') as f:
    for row in f.readlines():
        id = get_id(row)
        games = re.sub('Game [0-9]+:', '', row).split(";")
        for game in games:
            valid_game = is_game_valid(game)
            if not valid_game:
                break
        if valid_game:
            ids+=id

print(ids)

# Part 2
def get_game_cubes(s):
    cubes = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    for c in cubes.keys():
        n_c = re.search(f'[0-9]+(?=\s{c})', s)
        if not n_c:
            continue
        cubes[c]= int(n_c.group())
    return cubes


power_sum = 0
with open('2023/input_day2.txt', 'r') as f:
    for row in f.readlines():
        games = re.sub('Game [0-9]+:', '', row).split(";")
        min_cubes = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        for game in games:
            cubes = get_game_cubes(game)
            for col, num in cubes.items():
                if min_cubes[col] < num:
                    min_cubes[col] = num
        power = 1
        for num in min_cubes.values():
            power*=num
        power_sum+=power    

print(power_sum)