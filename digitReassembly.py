# Sara Yao Liu Grade 11


def digitReassembly(number, n):
    digList = []
    counter = 0
    while len(number) - counter >= n:
        nextNum = number[counter:counter + n]
        digList.append(nextNum)
        counter += 1
    return digList


fileContent = open('int-sample-input.txt').readlines()
i = 1
for eachLine in fileContent:
    eachList = digitReassembly(eachLine.strip().split()[0], int(eachLine.strip().split()[1]))
    sumNum = 0
    for eachInt in eachList:
        sumNum += int(eachInt)
    print(str(i) + '. ', sumNum)
    i += 1
