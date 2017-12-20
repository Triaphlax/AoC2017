import math
import re

# ------Input----- #
answer1 = 0
answer2 = 0

print("Input the firewall list. Calculation will start on the first empty line.")
inputList = []

while True:
    inputString = input("")
    if inputString == "":
        break
    inputList.append(inputString)


class Firewall:
    depth = 0
    length = 0
    position = 0

    def __init__(self, depth, length):
        self.depth = depth
        self.length = length

    def moveSteps(self, steps):
        self.position += steps

    @property
    def getRelativePosition(self):
        if self.length == 1:
            return 0
        else:
            segment = math.floor(self.position / (self.length - 1))
            posInSegment = self.position % (self.length - 1)
            if segment % 2 == 0:
                return posInSegment
            else:
                return (self.length - 1) - posInSegment


def parseString(string):
    splitUp = re.split(': ', string)

    return Firewall(int(splitUp[0]), int(splitUp[1]))


adjacencyList1 = list(map(parseString, inputList))
adjacencyList2 = list(map(parseString, inputList))

# ------Part 1------ #
currentPosition = -1

for i, currFW in enumerate(adjacencyList1):
    stepsToMove = currFW.depth - currentPosition
    if stepsToMove > 1:
        for fw in adjacencyList1:
            fw.moveSteps(stepsToMove-1)
    currentPosition += stepsToMove
    if currFW.getRelativePosition == 0:
        answer1 += currFW.depth * currFW.length
    for fw in adjacencyList1:
        fw.moveSteps(1)


# ------Part 2------ #
invalidStartingTimes = set()
currentTime = 0
highestCheckedValue = -1
stepSize = 100


def advanceTime(steps):
    global currentTime
    for step in range(steps):
        currentTime += 1
        for fireW in adjacencyList2:
            fireW.moveSteps(1)
            if fireW.getRelativePosition == 0:
                invalidStartingTimes.add(currentTime - fireW.depth)


def lowestMissingValue(start, end):
    global invalidStartingTimes
    valuesToCheck = range(start, end+1)
    possibleStartingPoints = set(valuesToCheck) - invalidStartingTimes
    if len(possibleStartingPoints) == 0:
        lowestValue = end+1
    else:
        lowestValue = min(set(valuesToCheck) - invalidStartingTimes)
    invalidStartingTimes = invalidStartingTimes - set(valuesToCheck)
    if lowestValue < end:
        return lowestValue
    else:
        return None


advanceTime(adjacencyList2[-1].depth)
answer2 = lowestMissingValue(0, 0)
highestCheckedValue = 0
while answer2 is None:
    advanceTime(stepSize)
    answer2 = lowestMissingValue(highestCheckedValue + 1, highestCheckedValue + stepSize)
    highestCheckedValue += stepSize

# ------Output----- #
print("Answer 1: " + str(answer1))
print("Answer 2: " + str(answer2))
