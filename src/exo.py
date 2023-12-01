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

lst = list()
nbr = ""
s = 0

filin = open("Yacine_input.txt", "r")
lst = filin.readlines()
filin.close()

for line in lst :
    for c in line :
        if c.isnumeric() :
            if len(nbr) < 2 :
                nbr += c
            else :
                tmp = list(nbr)
                tmp[1] = c
                nbr = "".join(tmp)
    if len(nbr) == 1 :
        nbr += nbr[0]
    if len(nbr) == 0 :
        nbr = "0"
    s += int(nbr)
    nbr = ""

print(s)

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

def Ajoute_nombre(c, nbr) :
    if len(nbr) < 2 :
        nbr += c
    else :
        tmp = list(nbr)
        tmp[1] = c
        nbr = "".join(tmp)


chiffre = {"zero" : "0", "one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}
lst = list()
nbr = ""
test = list()
s = 0

filin = open("input.txt", "r")
lst = filin.readlines()
filin.close()


for line in lst :
    for i in chiffre :
        if 
    for c in line :
        if c.isnumeric() :
            Ajoute_nombre(c, nbr)
        if c.isalpha() :
            
            
    if len(nbr) == 1 :
        nbr += nbr[0]
    if len(nbr) == 0 :
        nbr = "0"
    s += int(nbr)
    nbr = ""

print(s)

# likes = "Sammy likes to swim in the ocean, likes to spin up servers, and likes to smile."
# print(likes.find("likes"))