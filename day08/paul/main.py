def read_file_and_strip_newlines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = [line.rstrip('\n') for line in lines]
    return lines

def parse_lines(lines):
    first_line = lines.pop(0)
    lines.pop(0)
    parsed_lines = {}

    for line in lines:
        for character in ['(', ')', ' ']:
            line = line.replace(character, '')
        head, tail = line.split('=')
        left, right = tail.split(',')
        parsed_lines[head] = (left, right)

    return first_line, parsed_lines


def find_strings_ending_with_a(my_map):
    locations = list(my_map.keys())
    indices = [string for string in locations if string.endswith('A')]
    return indices


def is_strings_ending_with_z(current_locations):
    for location in current_locations:
        if not location.endswith('Z'):
            return False
    return True


def solve_part1(instructions, my_map):
    directions = { 'L': 0, 'R': 1}
    goal = 'ZZZ'
    current_location = 'AAA'
    steps = 0

    while current_location != goal:
        for instruction in instructions:
            current_location = my_map[current_location][directions[instruction]]
            steps += 1

    return steps


def solve_part2(instructions, starting_locations, my_map):
    directions = { 'L': 0, 'R': 1}
    goal = 'ZZZ'
    current_locations = [current_location for current_location in starting_locations]
    steps = 0

    # print('current_locations =', current_locations)
    while not is_strings_ending_with_z(current_locations):
        for instruction in instructions:
            # print(is_strings_ending_with_z(current_locations))
            if is_strings_ending_with_z(current_locations):
                # print('ENTERING BREAK')
                break
            for index, current_location in enumerate(current_locations):
                current_locations[index] = my_map[current_location][directions[instruction]]
            print('current_locations =', current_locations)
            steps += 1
            # print('steps =', steps)
            # print('________________________________________')
        # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

    return steps

def main(path):
    lines = read_file_and_strip_newlines(path)
    instructions, my_map = parse_lines(lines)

    starting_locations = find_strings_ending_with_a(my_map)
    print('instructions =', instructions)
    print('my_map =', my_map)

    # part1 = solve_part1(instructions, my_map)
    # part1_with_part2 = solve_part2(instructions, ["AAA"], my_map)
    # print('part1 =', part1_with_part2)
    # print('part1_with_part2 =', part1_with_part2)
    part2 = solve_part2(instructions, starting_locations, my_map)

    return 'part1_with_part2', part2


if __name__ == "__main__":
    day_number = '08'

    example = f'./day{day_number}/paul/example.txt'
    example_2 = f'./day{day_number}/paul/example2.txt'
    example_3 = f'./day{day_number}/paul/example3.txt'
    example_4 = f'./day{day_number}/paul/example4.txt'
    paul = f'./day{day_number}/paul/data.txt'
    yacine = f'./day{day_number}/yacine/data.txt'

    result = main(example_3)

    print('part 1 = ', result[0])
    print('part 2 = ', result[1])
