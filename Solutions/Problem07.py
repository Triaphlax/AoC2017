import re

# ------Input----- #
answer1 = 0
answer2 = 0

print("Input the list. Calculation will start on the first empty line.")
inputList = []

while True:
    inputString = input("")
    if inputString == "":
        break
    inputList.append(inputString)


def parseString(string):
    splitUp = re.split(' \(|\) -> |\)|, ', string)
    childrensList = []
    for n in splitUp[2:]:
        if n != '':
            childrensList.append(n)

    weights = []
    legacy = []
    if not childrensList:
        weights = [0, 0, 0]
        legacy = [0, 0, 0]

    return splitUp[0], int(splitUp[1]), childrensList, weights, legacy


bestList = list(map(parseString, inputList))


# ------Parts 1 and 2------ #
def part2Answer(megaTuple):
    sortedWeights = sorted(megaTuple[3])
    numberOfWeights = len(sortedWeights)
    if sortedWeights[0] < sortedWeights[1]:
        difference = sortedWeights[1] - sortedWeights[0]
        wrongValue = sortedWeights[0]
    else:
        difference = sortedWeights[numberOfWeights-2] - sortedWeights[numberOfWeights-1]
        wrongValue = sortedWeights[numberOfWeights-1]
    return megaTuple[4][megaTuple[3].index(wrongValue)] + difference


while len(bestList) > 1:
    for i, entry in enumerate(bestList):
        if not entry[2]:
            thirds = [i[2] for i in bestList]
            for j, l in enumerate(thirds):
                if entry[0] in l:
                    bestList[j][2].remove(entry[0])
                    bestList[j][3].append(entry[1] + sum(entry[3]))
                    bestList[j][4].append(entry[1])
                    del bestList[i]
                    if len(set(entry[3])) > 1:
                        if answer2 == 0:
                            answer2 = part2Answer(entry)
                    break
            break

answer1 = bestList[0][0]

if answer2 == 0:
    answer2 = part2Answer(bestList[0])

# ------Output----- #
print("Answer 1: " + str(answer1))
print("Answer 2: " + str(answer2))
