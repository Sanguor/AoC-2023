def read_file_and_strip_newlines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = [line.rstrip('\n') for line in lines]
    return lines


def parse_lines(lines):
    parsed_lines = []
    for line in lines:
        splitted_line = line.split(' | ')
        parsed_lines.append((splitted_line[0].split(' '), splitted_line[1].split(' ')))
    return parsed_lines


def calculate_part1(parsed_lines):
    total_sum = 0

    for line in parsed_lines:
        match_count = 0
        owned_numbers = line[1]

        for winning_number in line[0]:
            match_count += owned_numbers.count(winning_number)
        total_sum += int(2**(match_count - 1))

    return total_sum


def create_new_array(parsed_lines):
    new_array = []

    for line in parsed_lines:
        match_count = 0
        winning_numbers = line[0]
        owned_numbers = line[1]

        for winning_number in winning_numbers:
            match_count += owned_numbers.count(winning_number)
        new_array.append([match_count, 1])

    return new_array


def calculate_part2(matches_and_copies):
    sum = len(matches_and_copies)
    for current_index, element in enumerate(matches_and_copies):
        current_matches = element[0]
        current_copies = element[1]
        sum += current_matches * current_copies
        for n in range(current_index + 1, current_index + current_matches + 1):
            if n < len(matches_and_copies):
                matches_and_copies[n][1] += current_copies

    return sum


def main(path):
    lines = read_file_and_strip_newlines(path)
    parsed_lines = parse_lines(lines)
    part1 = calculate_part1(parsed_lines)

    matches_and_copies = create_new_array(parsed_lines)
    part2 = calculate_part2(matches_and_copies)

    return part1, part2


if __name__ == "__main__":
    paul = './day04/paul/data.txt'
    example = './day04/paul/example.txt'
    result = main(paul)

    print('part 1 = ', result[0]) # 28250
    print('part 2 = ', result[1]) # ?????
