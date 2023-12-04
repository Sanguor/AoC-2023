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

def browse_number(engine, y, x):
    nb = ""
    nb_pos = x

    while nb_pos < len(engine[y]) and engine[y][nb_pos].isnumeric():
        nb += engine[y][nb_pos]
        nb_pos += 1
    
    return [int(nb), nb_pos - 1]

def spot_symbol(engine, y, x):
    min_limit_x = x - 1 >= 0
    min_limit_y = y - 1 >= 0
    max_limit_y = y + 1 < len(engine)
    pos_x = x

    while engine[y][pos_x].isnumeric() and pos_x < len(engine[y]) :
        max_limit_x = pos_x + 1 < len(engine[y])

        # droite
        if max_limit_x and engine[y][pos_x + 1] != '.' and not engine[y][pos_x + 1].isnumeric():
            return True

        # gauche
        if pos_x == x and min_limit_x and engine[y][pos_x - 1] != '.' and not engine[y][pos_x - 1].isnumeric():
            return True

        # haut gauche
        if min_limit_y and min_limit_x and engine[y - 1][pos_x - 1] != '.' and not engine[y - 1][pos_x - 1].isnumeric():
            return True

        # bas gauche
        if max_limit_y and min_limit_x and engine[y + 1][pos_x - 1] != '.' and not engine[y + 1][pos_x - 1].isnumeric():
            return True

        # haut
        if min_limit_y and engine[y - 1][pos_x] != '.' and not engine[y - 1][pos_x].isnumeric():
            return True

        # bas
        if max_limit_y and engine[y + 1][pos_x] != '.' and not engine[y + 1][pos_x].isnumeric():
            return True

        # haut droite
        if min_limit_y and max_limit_x and engine[y - 1][pos_x + 1] != '.' and not engine[y - 1][pos_x + 1].isnumeric():
            return True

        # bas droite
        if max_limit_y and max_limit_x and engine[y + 1][pos_x + 1] != '.' and not engine[y + 1][pos_x + 1].isnumeric():
            return True
        
        pos_x += 1

    return False

def browse_engine_without_spoting_symbol(engine):
    sum = 0
    nb = list()
    line = 0

    for col in range(len(engine)):
        while line < len(engine[col]):
            if engine[col][line].isnumeric():
                nb = browse_number(engine, col, line)
                sum += nb[0]
                line = nb[1]
            line += 1
        line = 0
    return sum

def browse_engine(engine):
    sum = 0
    nb = list()
    line = 0

    for col in range(len(engine)):
        while line < len(engine[col]):
            if engine[col][line].isnumeric():
                nb = browse_number(engine, col, line)
                if spot_symbol(engine, col, line):
                    # if col == 12:
                    #     print(nb[0])
                    sum += nb[0]
                line = nb[1]
                # if col == 12:
                #     print(nb)
                #     print(line)
                #     print(engine[col][line])
            line += 1
        line = 0
    return sum

test = "test.txt"
yacine = "data_yacine.txt"
paul = "data_paul.txt"

engine = create_engine(yacine)

print("total :", browse_engine(engine))
print("total :", browse_engine_without_spoting_symbol(engine))
