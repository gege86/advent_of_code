input = "02_01.txt"
#input = "sample.txt"


list1 = []
safeCount = 0

with open(input,'r') as f:
    lines = f.readlines()
    for line in lines:
        list1 = line.split()
        increasingBase = int(list1[0]) < int(list1[1])
        for i in range(len(list1)-1):
            increasing = int(list1[i]) < int(list1[i+1])
            if increasing != increasingBase:
                break
            diff = abs(int(list1[i]) - int(list1[i+1]))
            if diff > 3 or diff == 0:
                break
            if i == len(list1)-2:
                safeCount = safeCount + 1
    print(safeCount)
