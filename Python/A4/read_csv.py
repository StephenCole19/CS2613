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

def header_map(table):
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
    hm = header_map(table)

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

def row2dict(hm, lst):
    d = {}
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
    '>=': operator.ge,
    'AND': operator.and_,
    'OR' : operator.or_
}

class Condition:
    def __init__(self, value1, op, value2):
        self.value1 = value1
        self.op = op
        self.value2 = value2
        
    def test(self):
        return OPERATOR_SYMBOLS[self.op](self.value1, self.value2)


def check_row(d, lst):
   
    if(type(lst[0]) == tuple):
        arr = []
        for x in d:
            if(x == lst[0][0]):
                val = d[x]
                if(type(lst[0][2]) != str ):
                    val = int(d[x])
                cond = Condition(int(d[x]), lst[0][1], lst[0][2])
                arr.append(cond.test())

            if(x == lst[2][0]):
                val = d[x]
                if(type(lst[2][2]) != str ):
                    val = int(d[x])

                cond = Condition(val, lst[2][1], lst[2][2])
                arr.append(cond.test())

        cond = Condition(arr[0], lst[1], arr[1])
        return cond.test()

    else:
        for x in d:
            if(x == lst[0]):
                if(type(lst[2]) != str ):
                    val = int(d[x])

                cond = Condition(val, lst[1], lst[2])
                return cond.test()



#print(check_row(list2dict(table[1]), (('age', '==', 5),'OR',('eye colour', '==', 'blue'))))
print(check_row(row2dict(header_map(table), table[1]), ('age', '==', 5)))

s = (('age', '==', 5),'OR',('eye_colour', '==', 'blue'))
print(check_row(row2dict(header_map(table), table[1]), s))