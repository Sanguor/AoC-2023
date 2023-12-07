import re
import numpy as np

def read_file_and_strip_newlines(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
        data = [line.rstrip('\n') for line in data]
    return data


def get_seeds_and_map(data):
    maps = {}
    current_map = None

    first_line = data.pop(0)
    seeds = [int(num_str) for num_str in re.findall(r'\d+', first_line)]

    for line in data:
        if line:
            if ':' in line:
                current_map = line.strip().replace(':', '')
                maps[current_map] = []
            else:
                values = list(map(int, line.strip().split()))
                maps[current_map].append(values)

    return seeds, maps


# def find_max(seeds, maps):
#     max_value = max(seeds)

#     for i in maps:
#         for j in maps[i]:
#             temp_max = max([j[0] + j[2], j[1] + j[2]]) - 1
#             max_value = temp_max if max_value < temp_max else max_value

#     return max_value


# def find_min(seeds, maps):
#     if 0 in seeds:
#         seeds.remove(0)
#     min_value = min(seeds)

#     for i in maps:
#         for j in maps[i]:
#             if j[0] != 0 and j[1] != 0:
#                 temp_min = min([j[0], j[1]])
#                 min_value = temp_min if min_value > temp_min else min_value

#     return min_value


# def find_max_interval(maps):
#     max_value = 0

#     for i in maps:
#         for j in maps[i]:
#             max_value = j[2] if max_value < j[2] else max_value

#     return max_value


def solve_part1(maps, first_list):

    final_array = [first_list]
    for i in maps:
        new_array = final_array[-1].copy()
        for j in maps[i]:
            # print(j)
            source_range = [i for i in range(j[1], j[1] + j[2])]
            destination_range = [i for i in range(j[0], j[0] + j[2])]

            # print('source_range =', source_range)
            # print('destination_range =', destination_range)

            # print('final_array[-1] = ', final_array[-1])


            for value_to_replace, new_value in zip(source_range, destination_range):
                index_to_replace = final_array[-1].index(value_to_replace)
                # if new_array == list(range(0, 100)):
                # print('value_to_replace =', value_to_replace)
                # print('new_value =', new_value)
                # print('index_to_replace= ', index_to_replace)
                new_array[index_to_replace] = new_value
                # print('_______________________________________________')

            # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        # print('len(new_array) =', len(new_array))
        final_array.append(new_array)
        # print('*****************************************************')

    # print('len(final_array) =', len(final_array))
    # print('final_array[0] =', final_array[0])
    # print('final_array[1] =', final_array[1])

    # print('final_array =', final_array[-1])
    print('final_array =', final_array[1])
    seed = 0
    return seed


def solve_part1_v2(maps, seeds):

    final_array = [seeds]

    for i in maps:
        # print('i =', i)
        new_array = final_array[-1].copy()
        for j in maps[i]:
            source_range = range(j[1], j[1] + j[2])
            destination_range = range(j[0], j[0] + j[2])
            # print('source_range =', source_range)
            for value_to_replace in final_array[-1]:
                # print('value_to_replace =', value_to_replace)
                if value_to_replace in source_range:
                    source_index = source_range.index(value_to_replace)
                    new_value = destination_range[source_index]
                    index_to_replace = final_array[-1].index(value_to_replace)
                    new_array[index_to_replace] = new_value
            # print('_____________________________________')
        final_array.append(new_array)
    print('final_array =', final_array)
    # print('final_array[0] =', final_array[0])
    # print('final_array[-1] =', final_array[-1])

    lowest_location = min(final_array[-1])
    print('lowest_location = ', lowest_location)
    # lowest_location_index = final_array[-1].index(lowest_location)
    # print('lowest_location_index = ', lowest_location_index)

    # result = final_array[0][lowest_location_index]
    # print('result = ', result)

    return lowest_location


def solve_part2(lines):
    sum = 0
    return sum


def main(path):
    lines = read_file_and_strip_newlines(path)
    seeds, maps = get_seeds_and_map(lines)
    # min_value = find_min(seeds, maps)  # 25 112 293
    # max_value = find_max(seeds, maps) # 4 294 967 295
    # max_interval = find_max_interval(maps) # 889 292 891
    # max possible : 536 870 912

    # first_list = list(range(0, max_value + 1))
    # part1 = solve_part1(maps, first_list)
    # part1 = solve_part1_v2(maps, seeds)

    seed_sum = 0

    seed_ranges = []
    for index, seed in enumerate(seeds):
        if index%2 != 0:
            seed_ranges.append(list(range(seeds[index - 1], seeds[index - 1] + seed)))

    print('seed_ranges = ', seed_ranges)
    possible_results = []
    for seeds in seed_ranges:
        possible_results.append(solve_part1_v2(maps, seeds))


    part2 = min(possible_results)

    return 'part1', part2


if __name__ == "__main__":
    day_number = '05'

    example = f'./day{day_number}/paul/example.txt'
    paul = f'./day{day_number}/paul/data.txt'
    yacine = f'./day{day_number}/yacine/data.txt'

    result = main(paul)

    print('part 1 = ', result[0])
    print('part 2 = ', result[1])
