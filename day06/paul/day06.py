### constants ### 

starting_speed = 0 # mm/ms
speed_increase = 1 # mm/ms

def read_file_and_strip_newlines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = [line.rstrip('\n') for line in lines]
    return lines


def parse_lines(lines):
    parsed_lines = []
    
    for line in lines:
        # _, l = line.split(':')
        res = [int(i) for i in line.split() if i.isdigit()]
        parsed_lines.append(res)

    return parsed_lines


def calculate_distances(duration):
    distances = []
    for time in range(1, duration):
        speed = starting_speed + time * speed_increase
        distance = speed * (duration - time)
        distances.append(distance)
    return distances


def find_winning_distances(race_distance, possible_distances):
    winning_distances = [int(i) for i in possible_distances if race_distance < i]
    return winning_distances


def solve_part1(parsed_lines):
    product = 1
    durations, distances = parsed_lines

    print('durations =', durations)
    print('distances =', distances)

    for race_duration, race_distance in zip(durations, distances):
        possible_distances = calculate_distances(race_duration)
        winning_distances = find_winning_distances(race_distance, possible_distances)
        product *= len(winning_distances) 

    return product


def solve_part2(lines):
    sum = 0
    return sum


def main(path):
    lines = read_file_and_strip_newlines(path)
    parsed_lines = parse_lines(lines)

    part1 = solve_part1(parsed_lines)
    part2 = solve_part2(lines)

    return part1, part2


if __name__ == "__main__":
    day_number = '06'

    example = f'./day{day_number}/paul/example.txt'
    example_part2 = f'./day{day_number}/paul/example2.txt'
    paul = f'./day{day_number}/paul/data.txt'
    paul_part2 = f'./day{day_number}/paul/data2.txt'
    yacine = f'./day{day_number}/yacine/data.txt'

    result = main(paul_part2)

    print('part 1 = ', result[0])
    print('part 2 = ', result[1])
