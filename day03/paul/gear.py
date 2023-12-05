import re

def read_file_and_strip_newlines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = [line.rstrip('\n') for line in lines]
    return lines


def get_coordinates_of_non_alphanumeric(lines):
    coordinates = []
    symbols = []

    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if not char.isalnum() and not char == '.':
                symbols.append(char)
                coordinates.append((row, col))

    return coordinates


def find_numbers_with_bounded_surrounding_coordinates(lines):
    surroundings_coordinates = [
        (1, 0), (0, 1), (-1, 0), (0, -1),
        (1, 1), (1, -1), (-1, -1), (-1, 1)
    ]
    numbers_with_bounded_surrounding_coordinates = []

    for row_idx, line in enumerate(lines):
        for match in re.finditer(r'\b\d+\b', line):
            number = match.group()

            print('match =', match)
            print('match.group() =', match.group())

            col_start = match.start()
            digit_coordinates = [(row_idx, col_start + idx) for idx in range(len(number))]
            bounded_digit_surroundings = []

            for digit_coord in digit_coordinates:
                for dr, dc in surroundings_coordinates:
                    new_row, new_col = digit_coord[0] + dr, digit_coord[1] + dc
                    if 0 <= new_row < len(lines) and 0 <= new_col < len(line):
                        bounded_digit_surroundings.append((new_row, new_col))
            numbers_with_bounded_surrounding_coordinates.append({number: bounded_digit_surroundings})


    return numbers_with_bounded_surrounding_coordinates


def calculate_sum(symbol_coords, numbers_coords):
    sum = 0
    numbers = []
    for dict in numbers_coords:
        for number in dict:
            for coord in symbol_coords:
                if coord in dict[number]:
                    numbers.append(number)
                    sum += int(number)
                    break

    return sum


def main(path):
    lines = read_file_and_strip_newlines(path)
    symbol_coords = get_coordinates_of_non_alphanumeric(lines)
    numbers_coords = find_numbers_with_bounded_surrounding_coordinates(lines)

    result = calculate_sum(symbol_coords, numbers_coords)

    return result


if __name__ == "__main__":
    # file_path = './day03_paul/reduced_sample_paul.txt'
    # file_path = './day03_paul/sample_paul.txt'
    file_path = './day03_paul/data_paul.txt'
    result = main(file_path)
    print('part 1 = ', result)

