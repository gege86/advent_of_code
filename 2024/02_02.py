input = "02_01.txt"
#input = "sample.txt"

list1 = []
safeCount = 0

def testReport(inputReport):
    # test if a report is safe
    # return True or False
    increasingBase = int(inputReport[0]) < int(inputReport[1])
    for i in range(len(inputReport) - 1):
        increasing = int(inputReport[i]) < int(inputReport[i+1])
        if increasing != increasingBase:
            break
        diff = abs(int(inputReport[i]) - int(inputReport[i+1]))
        if diff > 3 or diff == 0:
            break
        if i == len(inputReport) - 2:
            print(inputReport)
            return True
    return False


with open(input,'r') as f:
    lines = f.readlines()
    for line in lines:
        list1 = line.split()
        if testReport(list1):
            safeCount = safeCount + 1
            continue
        for i in range(len(list1)):
            shorterList = list1.copy()
            shorterList.pop(i)
            if testReport(shorterList):
                safeCount = safeCount + 1
                break
    print(safeCount)


