def read_file_and_strip_newlines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = [line.rstrip('\n') for line in lines]
    return lines


def parse_lines(lines):
    new_array = []
    for l in lines:
        new_el = []
        for str_nbr in l.split(' '):
            new_el.append(int(str_nbr))
        new_array.append(new_el)

    return new_array


def is_all_elements_zero(current_locations):
    for location in current_locations:
        if not location == 0:
            return False
    return True


def calculate_predictions(predictions_array):
    last_prediction = predictions_array[-1]
    if is_all_elements_zero(last_prediction):
        return predictions_array
    new_prediction = []
    for index, _ in enumerate(last_prediction):
        if index != 0:
            new_prediction.append(last_prediction[index] - last_prediction[index - 1])
    predictions_array.append(new_prediction)
    return calculate_predictions(predictions_array)


def calculate_next_value(predictions_array):
    reversed_array = list(reversed(predictions_array))
    for index, prediction in enumerate(reversed_array):
        if index != 0:
            next_value = prediction[-1] + reversed_array[index - 1][-1]
            reversed_array[index].append(next_value)
            # print('next_value RIGHT =', next_value)
    # print('________________________')

    return next_value


def calculate_next_value_part2(predictions_array):
    reversed_array = list(reversed(predictions_array))
    for index, prediction in enumerate(reversed_array):
        reversed_prediction = list(reversed(prediction))
        # print('reversed_prediction =', reversed_prediction)
        if index != 0:
            next_value =reversed_prediction[-1] - reversed_array[index - 1][-1]
            reversed_array[index].append(next_value)
            # print('next_value LEFT =', next_value)
    # print('________________________')

    return next_value


def solve_part1(lines):
    sum = 0
    for l in lines:
        predictions_array = calculate_predictions([l])
        predictions_array[-1].append(0)
        next_value = calculate_next_value(predictions_array)
        sum += next_value

    return sum


def solve_part2(lines):
    sum = 0
    for l in lines:
        predictions_array = calculate_predictions([l])
        predictions_array[-1].append(0)
        next_value = calculate_next_value_part2(predictions_array)
        sum += next_value

    return sum


def main(path):
    lines = read_file_and_strip_newlines(path)
    parsed_lines = parse_lines(lines)
    part1 = solve_part1(parsed_lines)
    parsed_lines = parse_lines(lines)
    part2 = solve_part2(parsed_lines)


    return part1, part2


if __name__ == "__main__":
    day_number = '09'

    example = f'./day{day_number}/paul/example.txt'
    paul = f'./day{day_number}/paul/data.txt'
    yacine = f'./day{day_number}/yacine/data.txt'

    result = main(paul)

    print('part 1 = ', result[0])
    print('part 2 = ', result[1])
