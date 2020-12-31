# TJHSST, Intermediate 5, Sara Yao Liu, 11th grade, Python 3.7.0


def buildPath(row, col, pos, blocked):
    direction = ''
    if pos % col > 0:
        direction = 'left-to-right'
    elif pos % col == 0:
        direction = 'right-to-left'
    path = ''
    piece = ''
    loop = True
    while loop:
        piece, pos = nextPiece(row, col, piece, pos, blocked, direction)
        if direction == 'left-to-right':
            if pos % col == 0:
                loop = False
            pos += 1
        elif direction == 'right-to-left':
            if pos % col == 1:
                loop = False
            pos -= 1
        path += piece
    if direction == 'right-to-left':
        path = path[::-1]
    return path


def nextPiece(row, col, piece, pos, blocked, direction):
    loop = True
    pieceInfo = []
    while loop:
        if piece == '':
            piece = 'A'
        elif piece == 'A':
            piece = 'B'
        elif piece == 'B':
            piece = 'C'
        elif piece == 'C':
            piece = 'A'
        positions = calPiecePositions(col, piece, pos, direction)
        badPos = False
        for p in positions:
            if p in blocked:
                badPos = True
                break
        if badPos:
            continue
        if direction == 'left-to-right':
            if positions[-1] <= row * col:
                if positions[-1] % col == 0 or positions[-1] % col > pos % col:
                    loop = False
                    pieceInfo = [piece, positions[-1]]
        elif direction == 'right-to-left':
            if positions[-1] >= 1:
                if positions[-1] < pos:
                    loop = False
                    pieceInfo = [piece, positions[-1]]
    return pieceInfo


def calPiecePositions(col, piece, pos, direction):
    positions = []
    if direction == 'left-to-right':
        if piece == 'A':
            positions = [pos, pos+1, pos+2]
        elif piece == 'B':
            positions = [pos, pos+col, pos+col+1]
        elif piece == 'C':
            positions = [pos, pos+1, pos+1+col, pos+1+2*col]
    elif direction == 'right-to-left':
        if piece == 'A':
            positions = [pos, pos-1, pos-2]
        elif piece == 'B':
            positions = [pos, pos-1, pos-1-col]
        elif piece == 'C':
            positions = [pos, pos-col, pos-2*col, pos-2*col-1]
    return positions


print('What file would you like to use for ACSL Contest 3? (Include .txt)')
fileContent = open(input()).readlines()
i = 1
for eachLine in fileContent:
    grid = eachLine.strip().split()
    row = int(grid[0])
    col = int(grid[1])
    pos = int(grid[2])
    blocked = []
    for each in grid[4:]:
        blocked.append(int(each))
    result = buildPath(row, col, pos, blocked)
    print(str(i) + '. ', result)
    i += 1
