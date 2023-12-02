import re

### FUNCTIONS ###
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines


def split_line(line):
    return line.split(', ')


# def find_numbers(value_and_colour):
#     return re.findall(r'\d+', value_and_colour)


def split_val_and_col(val_and_col):
    return val_and_col.split(' ')


def is_possible(value, color):
    color = color.replace('\n', '')
    limit_dict = {
        "red" : 13,
        "green" : 14,
        "blue" : 15
    }
    impossible_value = limit_dict[color]
    if value >= impossible_value:
        return False
    else:
        return True


def main(path):
    lines = read_file(path)
    splitted_lines = []
    for index, line in enumerate(lines):
        splitted_lines.append(split_line(line))

    for i, line in enumerate(splitted_lines):
        for j, el in enumerate(line):
            splitted_lines[i][j] = split_val_and_col(el)

    sum = 5050
    for index, line in enumerate(splitted_lines):
        for el in line:
            if not is_possible(int(el[0]), el[1]):
                sum -= index + 1
                break


    power_sum = 0
    for line in splitted_lines:
        max_dict = {
            "red" : 0,
            "green" : 0,
            "blue" : 0
        }
        for el in line:
            el[1] = el[1].replace('\n', '')
            el[0] = el[0].replace('\n', '')
            if int(el[0]) >= int(max_dict[el[1]]):
                max_dict[el[1]] = int(el[0])
        print('max_dict = ', max_dict)
        power_sum += max_dict['red'] * max_dict['green'] * max_dict['blue']
    return sum, power_sum


if __name__ == "__main__":
    # file_path = './day02/sample.txt'
    file_path = './day02/data_paul.txt'
    result = main(file_path)
    print('part 1 = ', result[0]) # 2237
    print('part 2 = ', result[1]) # 66681