import csv
import operator

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
    i = 1

    for x in table[0]:
        hmap[i] = x
        i += 1

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

        return arr

def list2dict(lst):
    d = {}
    hm = header_map()

    count = 1
    for x in lst:
        title = hm[count]
        d[title] = x
        count += 1
    
    return d

OPERATOR_SYMBOLS = {
    '<': operator.lt,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne,
    '>': operator.gt,
    '>=': operator.ge
}

class Condition:
    def __init__(self, value1, op, value2):
        self.value1 = value1
        self.op = op
        self.value2 = value2
        
    def test(self):
        return OPERATOR_SYMBOLS[self.op](self.value1, self.value2)


def check_row(d, lst):
    for x in d:
        if(x == lst[0]):
            if(type(lst[2]) != str ):

                cond = Condition(int(d[x]), lst[1], lst[2])

                if(cond.test()):
                    return True
                else:
                    return False
            else:

                cond = Condition((d[x]), lst[1], lst[2])

                if(cond.test()):
                    return True
                else:
                    return False

#print(list2dict(table[1]))
#print(header_map())
print(check_row(list2dict(table[1]), ('age', '>', 4)))