import functools

# ------Input----- #
answer1 = 0
answer2 = 0

inputString = input("Input list: ")
try:
    regularLengths = list(map(int, inputString.split(',')))
except ValueError:
    regularLengths = []
ASCIIlengths = list(map(ord, inputString))
ASCIIlengths.extend([17, 31, 73, 47, 23])


# ------Part 1------ #
def knotHash(lengths, rounds):
    theList = [x for x in range(256)]
    currentPosition = 0
    skipSize = 0
    for roundNumber in range(rounds):
        lengthsIndex = 0
        while lengthsIndex < len(lengths):
            currentLength = lengths[lengthsIndex]
            beginReversalPosition = currentPosition
            endReversalPosition = currentPosition + currentLength - 1
            while endReversalPosition > beginReversalPosition:
                correctedBegin = beginReversalPosition % len(theList)
                correctedEnd = endReversalPosition % len(theList)
                tempSwitchVariable = theList[correctedBegin]
                theList[correctedBegin] = theList[correctedEnd]
                theList[correctedEnd] = tempSwitchVariable
                beginReversalPosition += 1
                endReversalPosition -= 1
            lengthsIndex += 1
            currentPosition += currentLength + skipSize
            skipSize += 1
    return theList


knot1 = knotHash(regularLengths, 1)
answer1 = knot1[0] * knot1[1]

# ------Part 2------ #
knot2 = knotHash(ASCIIlengths, 64)

XORs = []
for xorNumber in range(16):
    XORs.append(functools.reduce(lambda x, y: x ^ y, knot2[xorNumber * 16:(xorNumber + 1) * 16], 0))

hexes = list(map(lambda dec: "{0:#0{1}x}".format(dec, 4).split('x')[-1], XORs))

answer2 = ''.join(hexes)

# ------Output----- #
print("Answer 1: " + str(answer1))
print("Answer 2: " + str(answer2))
