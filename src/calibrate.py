# my_module.py
def calculate_sum(path):
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


def calculate_sum_v2(path):
    return 29

yacine = "./src/Yacine_input.txt"
paul = "./src/Paul_input.txt"

calculate_sum(yacine)
