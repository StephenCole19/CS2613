import csv
import operator

def read_csv(csvF):
    '''Reads csv file into an array'''

    with open(csvF) as file:
        arr = []
        reader = csv.reader(file, delimiter=",")

        for row in reader:
            arr.append(row)
        
        return arr


table = read_csv("test1.csv")

def header_map(table):
    '''Maps headers into a dictionary'''

    hmap = {}
    i = 0

    while(i < len(table)):
        hmap[table[i]] = i 
        i += 1

    return hmap


def select(table, cols):
    '''Selects rows with certain headers contained in cols'''

    arr = []
    r = []

    count = 0
    hm = header_map(table[0])

    for x in cols:
        count = 0
        for y in hm:
            if(x == y):
                r.append(count)
            count += 1


    for row in table:
        cat = []
        for x in r:
            cat.append(row[x])

        arr.append(cat)

    return arr


def row2dict(hm, lst):
    '''converts a row of a table into a dictionary'''

    d = {}
    count = 0

    for key in hm:
        d[key] = lst[count]
        count += 1
    
    return d



def check_row(row, lst):
    '''Checks to see if the row is equal to the condtions in lst'''

    ops = {"==": operator.eq, '<=': operator.le, ">=": operator.ge, 'AND': operator.and_, 'OR': operator.or_}
    if isinstance(lst[2], int):
        try:
            return (ops[lst[1]](int(row[lst[0]]), int(lst[2])))
        except:
            return False
    elif isinstance(lst[2], str):
        try:
            return (ops[lst[1]](int(row[lst[0]]), int(lst[2])))
        except Exception:
            return (ops[lst[1]](str(row[lst[0]]), str(lst[2])))
    else:
        return (ops[lst[1]](check_row(row,lst[0]), check_row(row, lst[2])))

def filter_table(table, lst):
    '''filters the entire table based on a list of conditions'''

    output = []
    hmap = header_map(table[0])
    output.append(table[0])
    for row in table:
        if check_row(row2dict(hmap, row), lst):
            output.append(row)
    return output
