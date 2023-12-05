import re

def read_file_and_strip_newlines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = [line.rstrip('\n') for line in lines]
    return lines


def split_lines(lines):
    for line in lines:
        return line.split(' | ')

def main(path):
    lines = read_file_and_strip_newlines(path)
    splitted_lines = split_lines(lines)

    return splitted_lines


if __name__ == "__main__":
    # file_path = './day03_paul/reduced_sample_paul.txt'
    # file_path = './day03_paul/sample_paul.txt'
    paul = './day04/paul/data.txt'
    result = main(paul)
    print('part 1 = ', result)

