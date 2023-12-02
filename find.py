def calibrate_superior(path):

    filin = open(path, "r")
    lst = filin.readlines()
    lst = lst[0]
    # lst = 'eightwothree'
    print('lst =', lst)
    filin.close()

    myList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    chiffre = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    find_list = []
    rfind_list = []

    for i in myList:
        find_list.append(lst.find(i))

    for i in myList:
        rfind_list.append(lst.rfind(i))

    first_element = myList[rfind_list.index(min([i for i in find_list if i >= 0]))]
    last_element = myList[rfind_list.index(max(rfind_list))]

    print('first_element =', first_element)
    print('last_element =', last_element)

    if not first_element.isnumeric():
        first_element = chiffre[first_element]

    if not last_element.isnumeric():
        last_element = chiffre[last_element]

    return int(first_element + last_element)

