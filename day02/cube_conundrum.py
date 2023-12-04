import re

###                             Part 1

'''
    As you walk, the Elf shows you a small bag and some cubes which are
    either red, green, or blue. Each time you play this game, he will
    hide a secret number of cubes of each color in the bag, and your goal
    is to figure out information about the number of cubes.

    To get information, once a bag has been loaded with cubes, the Elf
    will reach into the bag, grab a handful of random cubes, show them to
    you, and then put them back in the bag. He'll do this a few times per
    game.

    You play several games and record the information from each game
    (your puzzle input). Each game is listed with its ID number (like
    the 11 in Game 11: ...) followed by a semicolon-separated list of
    subsets of cubes that were revealed from the bag (like 3 red,
    5 green, 4 blue).

    For example, the record of a few games might look like this:

    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    
    In game 1, three sets of cubes are revealed from the bag (and then put
    back again). 
    The first set is 3 blue cubes and 4 red cubes;
    the second set is 1 red cube, 2 green cubes, and 6 blue cubes;
    the third set is only 2 green cubes.

    The Elf would first like to know which games would have been possible
    if the bag contained only 12 red cubes, 13 green cubes, and 14 blue
    cubes?

    In the example above, games 1, 2, and 5 would have been possible if the
    bag had been loaded with that configuration. However, game 3 would have
    been impossible because at one point the Elf showed you 20 red cubes
    at once; similarly, game 4 would also have been impossible because the
    Elf showed you 15 blue cubes at once. If you add up the IDs of the
    games that would have been possible, you get 8.

    Determine which games would have been possible if the bag had been
    loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes.
    What is the sum of the IDs of those games?
'''

# def find_color(cube_color, color)
#     if color

def game_impossible(game_list):
    for i, s in enumerate(game_list):
        if not s.isnumeric():
            if s == "red":
                if int(game_list[i - 1]) > 12:
                    return True
            if s == "green":
                if int(game_list[i - 1]) > 13:
                    return True
            if s == "blue":
                if int(game_list[i - 1]) > 14:
                    return True
    return False

def Create_game_list(game):
    game_list = re.findall(r'\w+', game)
    del game_list[:2]

    return game_list

def game_verif(game, id):
    game_split = Create_game_list(game)

    if game_impossible(game_split):
        return id + 1
    return 0

###                             Part 2

'''
    As you continue your walk, the Elf poses a second question: in each game
    you played, what is the fewest number of cubes of each color that could
    have been in the bag to make the game possible?

    Again consider the example games from earlier:

    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    
    - In game 1, the game could have been played with as few as 4 red,
    2 green, and 6 blue cubes. If any color had even one fewer cube, the
    game would have been impossible.
    - Game 2 could have been played with a minimum of 1 red, 3 green, and 4
    blue cubes.
    - Game 3 must have been played with at least 20 red, 13 green, and 6
    blue cubes.
    - Game 4 required at least 14 red, 3 green, and 15 blue cubes.
    - Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in
    the bag.
    
    The power of a set of cubes is equal to the numbers of red, green, and
    blue cubes multiplied together. The power of the minimum set of cubes
    in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively.
    Adding up these five powers produces the sum 2286.

    For each game, find the minimum set of cubes that must have been present.
    What is the sum of the power of these sets?
'''

def max_color_knew(game_list):
    max_red = 0
    max_green = 0
    max_blue = 0

    for i, s in enumerate(game_list):
        if not s.isnumeric():
            if s == "red":
                if int(game_list[i - 1]) > max_red:
                    max_red = int(game_list[i - 1])
            if s == "green":
                if int(game_list[i - 1]) > max_green:
                    max_green = int(game_list[i - 1])
            if s == "blue":
                if int(game_list[i - 1]) > max_blue:
                    max_blue = int(game_list[i - 1])

    return max_red * max_green * max_blue

def game_power(game):
    game_split = Create_game_list(game)

    return max_color_knew(game_split)

# lst = [
#     "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
#     "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
#     "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
#     "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
#     "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
# ]
# sum_id = ((len(lst) + 1) * len(lst)) // 2

yacine = "data_yacine.txt"
paul = "data_paul.txt"

file_yacine = open(yacine, "r")
lst_yacine = file_yacine.readlines()
file_yacine.close()

file_paul = open(paul, "r")
lst_paul = file_paul.readlines()
file_paul.close()

##      Part 1
sum_IDY = ((len(lst_yacine) + 1) * len(lst_yacine)) // 2
sum_IDP = ((len(lst_paul) + 1) * len(lst_paul)) // 2

for id, game in enumerate(lst_yacine):
    sum_IDY -= game_verif(game, id)

for id, game in enumerate(lst_paul):
    sum_IDP -= game_verif(game, id)

# for id, game in enumerate(lst):
#     sum_id -= game_verif(game, id)

print("La somme des id de Yacine est", sum_IDY)
print("La somme des id de Paul est", sum_IDP)
# print(sum_id)

##      Part 2
# sum_power = 0
sum_powerY = 0
sum_powerP = 0

for game in lst_yacine:
    sum_powerY += game_power(game)

for game in lst_paul:
    sum_powerP += game_power(game)

# for game in lst:
#     sum_power += game_power(game)

print("La somme du pouvoir des parties de Yacine est", sum_powerY)
print("La somme du pouvoir des parties de Paul est", sum_powerP)
# print(sum_power)


