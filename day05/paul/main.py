import re
import math

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


def solve_part1(maps, first_list):

    final_array = [first_list]
    for i in maps:
        new_array = final_array[-1].copy()
        for j in maps[i]:
            source_range = [i for i in range(j[1], j[1] + j[2])]
            destination_range = [i for i in range(j[0], j[0] + j[2])]
            for value_to_replace, new_value in zip(source_range, destination_range):
                index_to_replace = final_array[-1].index(value_to_replace)
                new_array[index_to_replace] = new_value
        final_array.append(new_array)
    seed = 0
    return seed


def split_range(chunk_size, range_size):
    number_of_chunks = math.ceil(range_size / chunk_size)
    # last_chunk_size = range_size % chunk_size

    return number_of_chunks

def solve_part1_v2(maps, seeds):

    final_array = [seeds]

    for i in maps:
        new_array = final_array[-1].copy()
        for j in maps[i]:
            source_range = range(j[1], j[1] + j[2])
            destination_range = range(j[0], j[0] + j[2])
            for value_to_replace in final_array[-1]:
                if value_to_replace in source_range:
                    source_index = source_range.index(value_to_replace)
                    new_value = destination_range[source_index]
                    index_to_replace = final_array[-1].index(value_to_replace)
                    new_array[index_to_replace] = new_value
        final_array.append(new_array)

    # print('final_array[-1] = ', final_array[-1])

    lowest_location = min(final_array[-1])

    return lowest_location


def solve_part2(maps, seeds):


    # print('maps =', maps)
    # print('seeds =', seeds)

    final_array = [seeds]

    for i in maps:
        new_array = final_array[-1].copy()
        for j in maps[i]:
            source_range = range(j[1], j[1] + j[2])
            destination_range = range(j[0], j[0] + j[2])
            for value_to_replace in final_array[-1]:
                if value_to_replace in source_range:
                    source_index = source_range.index(value_to_replace)
                    new_value = destination_range[source_index]
                    index_to_replace = final_array[-1].index(value_to_replace)
                    new_array[index_to_replace] = new_value
        final_array.append(new_array)
        if len(final_array[-1]) > 10:
            print('len(final_array[-1] =', len(final_array[-1]))
        if len(final_array) > 10:
            print('len(final_array =', len(final_array))


    lowest_location = min(final_array[-1])

    return lowest_location


def main(path):
    lines = read_file_and_strip_newlines(path)
    seeds, maps = get_seeds_and_map(lines)
    part1 = solve_part1_v2(maps, seeds)


    # seed_ranges = []
    # for index, seed in enumerate(seeds):
    #     if index%2 != 0:
    #         seed_ranges.append(list(range(seeds[index - 1], seeds[index - 1] + seed)))

    # possible_results = []
    # for seeds in seed_ranges:
    #     possible_results.append(solve_part2(maps, seeds))

    # # print('possible_results =', possible_results)
    # part2 = min(possible_results)

    ### NEW PART 2 ###
    print('__________________________________ START NEW PART 2 __________________________________')
    chunk_size = 10

    # seeds, maps = get_seeds_and_map(lines)
    part2 = 999999999999999999999999999999999999

    for index, seed in enumerate(seeds):
        print('seed =', seed)
        if index%2 != 0:
            range_start = seeds[index - 1]
            range_size = seed

            number_of_chunks = split_range(chunk_size, range_size)

            count = 1
            for i in range(0, number_of_chunks):
                if i > number_of_chunks // 1000 * count:
                    print(f'{0.1 * count}%')
                    count += 1
                my_range = range(range_start + i * chunk_size, range_start + i * chunk_size + chunk_size)
                chunked_list = []
                for j in my_range:
                    if j < range_start + range_size:
                        chunked_list.append(j)
                result = solve_part2(maps, chunked_list)

                if result < part2:
                    part2 =  result
                    print('part2 =', part2)
                # possible_results.append(solve_part2(maps, chunked_list))

    # part2 = min(possible_results)
    return part1, part2


if __name__ == "__main__":
    day_number = '05'

    example = f'./day{day_number}/paul/example.txt'
    paul = f'./day{day_number}/paul/data.txt'
    yacine = f'./day{day_number}/yacine/data.txt'

    result = main(paul)

    print('part 1 = ', result[0])
    print('part 2 = ', result[1])
