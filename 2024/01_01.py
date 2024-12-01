input = "01_01.txt"

list1 = []
list2 = []
osszeg = 0

with open(input,'r') as f:
    lines = f.readlines()
    for line in lines:
        a = int(line.split()[0])
        b = int(line.split()[1])
        list1.append(a)
        list2.append(b)
    list1.sort()
    list2.sort()

    for i in range(len(list1)):
        d = abs(int(list1[i]) - int(list2[i]))
        osszeg = osszeg + d
    print(osszeg)