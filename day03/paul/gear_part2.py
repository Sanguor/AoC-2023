import re

def read_file_and_strip_newlines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = [line.rstrip('\n') for line in lines]
    return lines


def find_star_coordinates(lines):
    star_coordinates = []

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == '*':
                star_coordinates.append((i, j))

    return star_coordinates


def find_numbers_coordinates(lines):
    surroundings_coordinates = [
        (1, 0), (0, 1), (-1, 0), (0, -1),
        (1, 1), (1, -1), (-1, -1), (-1, 1)
    ]
    numbers_with_bounded_surrounding_coordinates = []

    for row_idx, line in enumerate(lines):
        for match in re.finditer(r'\b\d+\b', line):
            number = match.group()
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


def calculate_sum(starts_coords, numbers_coords):
    sum = 0

    for start_coord in starts_coords:
        count = 0
        duo = []
        for dict in numbers_coords:
            for number in dict:
                if start_coord in dict[number]:
                    count +=1
                    duo.append(number)
        if count == 2:
            sum += int(duo[0]) * int(duo[1])

    return sum


def main(path):
    lines = read_file_and_strip_newlines(path)
    starts_coords = find_star_coordinates(lines)
    number_coords = find_numbers_coordinates(lines)

    result = calculate_sum(starts_coords, number_coords)

    return result


if __name__ == "__main__":
    # file_path = './day03_paul/reduced_sample_paul.txt'
    # file_path = './day03_paul/sample_paul.txt'
    file_path = './day03_paul/data_paul.txt'
    # file_path = './day03/data_yacine.txt'
    result = main(file_path)
    print('part 2 = ', result)

