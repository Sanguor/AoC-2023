def read_file(path):
    filin = open(path, "r")
    content = filin.readlines()
    filin.close()
    return content


def calibrate_line(line):
    myList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    myDict = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    find_list = []
    rfind_list = []

    for i in myList:
        find_list.append(line.find(i))

    for i in myList:
        rfind_list.append(line.rfind(i))

    first_element = myList[find_list.index(min([i for i in find_list if i >= 0]))]
    last_element = myList[rfind_list.index(max(rfind_list))]

    if not first_element.isnumeric():
        first_element = myDict[first_element]

    if not last_element.isnumeric():
        last_element = myDict[last_element]

    return int(first_element + last_element)


def calibrate(path):
    lst = list()
    nbr = ""
    s = 0

    filin = open(path, "r")
    lst = filin.readlines()
    filin.close()

    for line in lst:
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
        s += int(nbr)
        nbr = ""

    print(s)

    return s


def calibrate_superior(path):
    lines = read_file(path)
    sum = 0

    for line in lines:
        partial_sum = calibrate_line(line)
        sum += partial_sum

    return sum


if __name__ == "__main__":
    yacine = "./src/Yacine_input.txt"
    paul = "./src/Paul_input.txt"

    print('Yacine exo 1 = ', calibrate(yacine))
    print('Yacine exo 2 = ', calibrate_superior(yacine))
    print('Paul exo 1 = ', calibrate(paul))
    print('Paul exo 2 = ', calibrate_superior(paul))