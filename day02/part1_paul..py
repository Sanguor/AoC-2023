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
    print('splitted_lines= ', splitted_lines)
    for index, line in enumerate(splitted_lines):
        for el in line:
            if not is_possible(int(el[0]), el[1]):
                sum -= index + 1
                break
    return sum


if __name__ == "__main__":
    # file_path = './day02/sample.txt'
    file_path = './day02/data_paul.txt'
    result = main(file_path)
    print('result = ', result)