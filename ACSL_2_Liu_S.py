# TJHSST, Intermediate 5, Sara Yao Liu, Grade 11, Python 3.7.0


def commonStr(str1, str2):
    commonString = ''
    for ch in str1:
        idx = str2.find(ch)
        if idx != -1:
            commonString += ch
            str2 = str2[idx + 1:]
    return commonString


def abShared(str1, str2, str3, str4):
    sharedStr = ''
    for ch in str1:
        if ch in str2 and ch in str3 and ch in str4:
            sharedStr += ch
    abStr = ''.join(sorted(set(sharedStr)))
    return abStr if abStr != '' else 'NONE'


print('In what file would you like to find common substrings? (Include .txt)')
fileContent = open(input()).readlines()
line = 1
for eachLine in fileContent:
    if eachLine == '' or eachLine.isspace():
        continue
    strA, strB = eachLine.strip().split()
    result1 = commonStr(strA, strB)
    result2 = commonStr(strB, strA)
    result3 = commonStr(strA[::-1], strB[::-1])
    result4 = commonStr(strB[::-1], strA[::-1])
    print(str(line) + '. ', abShared(result1, result2, result3, result4))
    line += 1
