import re

###                             Part 1

'''
    As far as the Elf has been able to figure out, you have to figure out
    which of the numbers you have appear in the list of winning numbers.
    The first match makes the card worth one point and each match after
    the first doubles the point value of that card.

    For example:

    Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
    
    In the above example, card 1 has five winning numbers (41, 48, 83, 86,
    and 17) and eight numbers you have (83, 86, 6, 31, 17, 9, 48, and 53).
    Of the numbers you have, four of them (48, 83, 17, and 86) are winning
    numbers! That means card 1 is worth 8 points (1 for the first match,
    then doubled three times for each of the three matches after the first).

    Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
    Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
    Card 4 has one winning number (84), so it is worth 1 point.
    Card 5 has no winning numbers, so it is worth no points.
    Card 6 has no winning numbers, so it is worth no points.
    So, in this example, the Elf's pile of scratchcards is worth 13 points.

    Take a seat in the large pile of colorful cards.
    How many points are they worth in total?
'''

def create_lists_by_file(text):
    lst_win = list()
    lst_mybingo = list()
    lst_win_res = list()
    lst_mybingo_res = list()
    file = open(text, "r")
    numbers = file.readlines()
    file.close()

    for i, line in enumerate(numbers):
        line = line.rstrip('\n')
        line_list = line.split()
        del line_list[:2]
        
        transition = False
        for j, nb in enumerate(line_list):
            if not transition:
                if nb == '|':
                    transition = True
                else:
                    lst_win.append(int(nb))
            else:
                lst_mybingo.append(int(nb))
        lst_win_res.append(lst_win)
        lst_mybingo_res.append(lst_mybingo)

    return lst_win_res, lst_mybingo_res

test = "test.txt"
yacine = "data_yacine.txt"

lst_win, lst_myturn = create_lists_by_file(test)

print(lst_win, lst_myturn, sep= "\n")
# print("win :")
# for i in range(len(lst_win)):
#     for j in range(len(lst_win[i])):
#         print(lst_win[i][j])

# print("\nmy turn :")
# for i in range(len(lst_myturn)):
#     for j in range(len(lst_myturn[i])):
#         print(lst_myturn[i][j])
