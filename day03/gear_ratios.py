###                             Part 1

'''
    The engine schematic (your puzzle input) consists of a visual
    representation of the engine. There are lots of numbers and symbols
    you don't really understand, but apparently any number adjacent to a
    symbol, even diagonally, is a "part number" and should be included
    in your sum. (Periods (.) do not count as a symbol.)

    Here is an example engine schematic:

    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..

    In this schematic, two numbers are not part numbers because they
    are not adjacent to a symbol: 114 (top right) and 58 (middle right).
    Every other number is adjacent to a symbol and so is a part number;
    their sum is 4361.

    Of course, the actual engine schematic is much larger.
    What is the sum of all of the part numbers in the engine schematic?
'''

def create_engine(text):
    file = open(text, "r")
    engine = file.readlines()
    file.close()

    for i, line in enumerate(engine):
        engine[i] = list(line)
    
    return engine

def spot_symbol(engine, y, x, nb, begin = True):
    # min_limit_x = x - 1 >= 0
    # min_limit_y = y - 1 >= 0
    # max_limit_x = x + 1 < len(engine[y])
    # max_limit_y = y + 1 < len(engine)

    # # droite
    # if max_limit_x :
    #     if engine[y][x + 1].isnumeric():
    #         return spot_symbol(engine, y, x + 1, nb + engine[y][x + 1], False)
    #     if engine[y][x + 1] != '.':
    #         # print(nb)
    #         return int(nb)

    # # gauche
    # if begin and min_limit_x and engine[y][x - 1] != '.' and not engine[y][x - 1].isnumeric():
    #     # print(nb)
    #     return int(nb)

    # # haut gauche
    # if min_limit_y and min_limit_x and engine[y - 1][x - 1] != '.' and not engine[y - 1][x - 1].isnumeric():
    #     # print(nb)
    #     return int(nb)

    # # bas gauche
    # if max_limit_y and min_limit_x and engine[y + 1][x - 1] != '.' and not engine[y + 1][x - 1].isnumeric():
    #     # print(nb)
    #     return int(nb)

    # # haut
    # if min_limit_y and engine[y - 1][x] != '.' and not engine[y - 1][x].isnumeric():
    #     # print(nb)
    #     return int(nb)

    # # bas
    # if max_limit_y and engine[y + 1][x] != '.' and not engine[y + 1][x].isnumeric():
    #     # print(nb)
    #     return int(nb)

    # # haut droite
    # if min_limit_y and max_limit_x and engine[y - 1][x + 1] != '.' and not engine[y - 1][x + 1].isnumeric():
    #     # print(nb)
    #     return int(nb)

    # # bas droite
    # if max_limit_y and max_limit_x and engine[y + 1][x + 1] != '.' and not engine[y + 1][x + 1].isnumeric():
    #     # print(nb)
    #     return int(nb)

    # return 0

    return 0

def browse_engine(engine):
    sum = 0
    tmp = 0
    nb = ""

    line = 0
    for col in range(len(engine)):
        while line < len(engine[col]):
            if engine[col][line].isnumeric():
                print(engine[col][line])
                tmp = spot_symbol(engine, col, line, nb.join(engine[col][line]))
                nb = ""
                line += len(str(tmp)) - 1
                sum += tmp
            line += 1
        line = 0
    return sum

test = "test.txt"
yacine = "data_yacine.txt"
paul = "data_paul.txt"

engine = create_engine(test)

print(browse_engine(engine))