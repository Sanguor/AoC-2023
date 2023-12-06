def read_file_and_strip_newlines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = [line.rstrip('\n') for line in lines]
    return lines


def solve_part1(lines):
    sum = 0
    return sum


def solve_part2(lines):
    sum = 0
    return sum


def main(path):
    lines = read_file_and_strip_newlines(path)

    part1 = solve_part1(lines)
    part2 = solve_part2(lines)

    return part1, part2


if __name__ == "__main__":
    day_number = '99'

    example = f'./day{day_number}/paul/example.txt'
    paul = f'./day{day_number}/paul/data.txt'
    yacine = f'./day{day_number}/yacine/data.txt'

    result = main(example)

    print('part 1 = ', result[0])
    print('part 2 = ', result[1])
