import csv

with open("2015-100.csv") as file:
    arr = []
    reader = csv.reader(file, delimiter=",")
    count = 0

    for row in reader:

        r = []
        i = 0
        while(i < len(row)):
            r.append(row[count])
            i += 1
        
        arr.append(r)
        r = []
        i = 0
            
    print(arr)

