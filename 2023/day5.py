def get_map_from_line(map_line):
    map_line = map_line.split()
    range_length = int(map_line[2])
    return {'source_start': int(map_line[1]), 'source_end': int(map_line[1]) + range_length-1, 'start_destination': int(map_line[0])}

def get_map_from_block(map_block):
    maps = [get_map_from_line(map_line) for map_line in map_block]
    maps = sorted(maps, key=lambda x: x['source_start'])
    return maps

def get_destination(maps, input_number):
    for m in maps:
        if input_number >= m['source_start'] and input_number<=m['source_end']:
            output_number = m['start_destination']+(input_number-m['source_start'])
            break
    else:
        output_number = input_number
    return output_number

def get_final_destination(all_maps, number):
    for m in all_maps:
        number = get_destination(m, number)
    return number


def get_destination_from_range(maps, input_start, input_end):
    output_range = []
    for m in maps:
        if input_start >= m['source_start'] and input_start<=m['source_end']:
            output_start = m['start_destination']+(input_start-m['source_start'])
            input_overlap_end = min(input_end, m['source_end'])
            output_end = m['start_destination']+(input_overlap_end-m['source_start'])
        elif m['source_start'] > input_start:
            output_start = input_start
            input_overlap_end = min(input_end, m['source_start'])
            output_end = input_overlap_end
        else:
            continue
        output_range.append((output_start, output_end))
        input_start = input_overlap_end+1
        if input_start>input_end:
            return output_range
    if input_start <= input_end:
        output_range.append((input_start, input_end))
    return output_range



def get_final_destination_from_range(all_maps, input_start, input_end):
    ranges = [(input_start, input_end)]
    for m in all_maps:
        ranges = [get_destination_from_range(m, start, end) for start, end in ranges]
        ranges = [r for rg in ranges for r in rg]
    return ranges

with open('2023/input_day5.txt', 'r') as f:
    input = f.read()
    input_list = input.split('\n')
    # parse seeds
    seed_str = input_list[0]
    seeds = [int(s) for s in seed_str.replace('seeds:', '').split()]
    
    start_of_maps = [i for i, v in enumerate(input_list) if v.endswith('map:')]
    num_maps = len(start_of_maps)
    maps = []
    for i, idx_start in enumerate(start_of_maps):
        idx_end = start_of_maps[i+1]-1 if i+1 < num_maps else len(input_list)-1
        block = input_list[(idx_start+1):idx_end]
        maps.append(get_map_from_block(block))
    
    # part 1
    seeds_destination = [get_final_destination(maps, seed) for seed in seeds]
    
    # part 2
    destination_ranges = []
    for seed_start, seed_range in [(seeds[2*i], seeds[2*i+1]) for i in range(len(seeds)//2)]:
        destination_ranges += get_final_destination_from_range(maps, seed_start, seed_start+seed_range-1)

print(min([x[0] for x in destination_ranges]))