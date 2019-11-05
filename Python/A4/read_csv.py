import csv

def read_csv(csvF):
    with open(csvF) as file:
        arr = []
        reader = csv.reader(file, delimiter=",")

        for row in reader:
            arr.append(row)
        
        return arr


table = read_csv("test.csv")

def header_map():
    hmap = {}
    i = len(table) - 1

    for x in table[0]:
        hmap[i] = x
        i -= 1

    return hmap


def select(table, cols):
    arr = []
    r = []

    count = 0
    hm = header_map()

    for x in cols:
        count = 0
        while(count < len(table)-1):
            if(x == table[0][count]):
                r.append(count)
            count += 1

    for row in table:
        cat = []
        for x in r:
            cat.append(row[x])

        arr.append(cat)

    print(arr)




select(table, {'name', "eye_colour"})