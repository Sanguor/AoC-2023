import re

###                         Part 1

'''
    The newly-improved calibration document consists of lines of text;
    each line originally contained a specific calibration value that
    the Elves now need to recover. On each line, the calibration value
    can be found by combining the first digit and the last digit
    (in that order) to form a single two-digit number.

    For example:

    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
    
    In this example, the calibration values of these four lines
    are 12, 38, 15, and 77. Adding these together produces 142.
'''

def calibrate(line):
    nbr = ""

    for c in line:
        if c.isnumeric():
            if len(nbr) < 2:
                nbr += c
            else:
                tmp = list(nbr)
                tmp[1] = c
                nbr = "".join(tmp)
    if len(nbr) == 1:
        nbr += nbr[0]
    if len(nbr) == 0:
        nbr = "0"

    return int(nbr)

###                         Part 2

'''
    Your calculation isn't quite right. It looks like some of the
    digits are actually spelled out with letters: one, two, three,
    four, five, six, seven, eight, and nine also count as
    valid "digits".

    Equipped with this new information, you now need to find the
    real first and last digit on each line. For example:

    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen

    In this example, the calibration values are 29, 83, 13, 24,
    42, 14, and 76. Adding these together produces 281.
'''

def calibrate_superior(line):
    chiffre = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    myList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    find_list = list()
    rfind_list = list()

    for i in myList:
        find_list.append(line.find(i))

    for i in myList:
        rfind_list.append(line.rfind(i))

    first_element = myList[find_list.index(min([i for i in find_list if i >= 0]))]
    last_element = myList[rfind_list.index(max(rfind_list))]

    if not first_element.isnumeric():
        first_element = chiffre[first_element]

    if not last_element.isnumeric():
        last_element = chiffre[last_element]

    return int(first_element + last_element)

###                     Main

yacine = "./src/Yacine_input.txt"
paul = "./src/Paul_input.txt"
sY_1 = 0
sY_2 = 0
sP_1 = 0
sP_2 = 0

file_yacine = open(yacine, "r")
lst_yacine = file_yacine.readlines()
file_yacine.close()

file_paul = open(paul, "r")
lst_paul = file_paul.readlines()
file_paul.close()

for line in lst_yacine:
    sY_1 += calibrate(line)
    sY_2 += calibrate_superior(line)


for line in lst_paul:
    sP_1 += calibrate(line)
    sP_2 += calibrate_superior(line)

##      Part 1
print("La somme de la méthode en partie 1 pour Yacine est", sY_1)
print("La somme de la méthode en partie 1 pour Paul est", sP_1)

##      Part 2
print("La somme de la méthode en partie 2 pour Yacine est", sY_2)
print("La somme de la méthode en partie 2 pour Paul est", sP_2)
