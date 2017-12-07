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
    splitUp = re.split(" \(|\) -> |\)|, ", string)
    childrensList = []
    for n in splitUp[2:]:
        if n != '':
            childrensList.append(n)
    return splitUp[0], splitUp[1], childrensList


betterInputList = list(map(parseString, inputList))

# ------Part 1------ #
part1List = list(betterInputList)
while len(part1List) > 1:
    for i, entry in enumerate(part1List):
        if not entry[2]:
            thirds = [i[2] for i in part1List]
            for j, l in enumerate(thirds):
                if entry[0] in l:
                    part1List[j][2].remove(entry[0])
                    del part1List[i]
                    break
            break

answer1 = part1List[0][0]

# ------Part 2------ #

# ------Output----- #
print("Answer 1: " + str(answer1))
print("Answer 2: " + str(answer2))
