import sys

# ------Input----- #
answer1 = 0
answer2 = 0

inputString = input("Input character stream: ")


# ------Parts 1 & 2------ #
def findGroups(depth):
    global stringIndex
    global answer2
    nestedScore = 0
    isGarbage = False
    while stringIndex < len(inputString):
        currentChar = inputString[stringIndex]
        stringIndex += 1
        if not isGarbage:
            if currentChar == '{':
                nestedScore += findGroups(depth + 1)
            elif currentChar == '}':
                return nestedScore + depth
            elif currentChar == '<':
                isGarbage = True
                continue
        else:
            if currentChar == '>':
                isGarbage = False
                continue
            if currentChar != '!':
                answer2 += 1
        if currentChar == '!':
            stringIndex += 1
    return nestedScore


stringIndex = 0
answer1 = findGroups(0)

# ------Output----- #
print("Answer 1: " + str(answer1))
print("Answer 2: " + str(answer2))
