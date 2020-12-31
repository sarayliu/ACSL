# TJHSST, Intermediate 5, Sara Yao Liu, Grade 11, Python 3.7.0


def evaluate(prefixExp):
    stack = []
    binaryOperators = '+-*/'
    trinaryOperators = '@>'
    for op in prefixExp[::-1]:
        if op.isdigit():
            stack.append(int(op))
        elif op in binaryOperators:
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(binEval(num1, num2, op))
        elif op in trinaryOperators:
            num1 = stack.pop()
            num2 = stack.pop()
            num3 = stack.pop()
            stack.append(triEval(num1, num2, num3, op))
    return stack[0]


def binEval(num1, num2, op):
    if op == '+':
        return num1 + num2
    if op == '-':
        return num1 - num2
    if op == '*':
        return num1 * num2
    if op == '/':
        return num1 / num2


def triEval(num1, num2, num3, op):
    if op == '@':
        if num1 > 0:
            return num2
        return num3
    if op == '>':
        return max(num1, num2, num3)


print('What file would you like to use for ACSL Contest 4? (Include .txt)')
fileContent = open(input()).readlines()
i = 1
for eachLine in fileContent:
    if eachLine == '' or eachLine.isspace():
        continue
    expression = eachLine.strip().split()
    result = evaluate(expression)
    print('#' + str(i) + '. ', result)
    i += 1
