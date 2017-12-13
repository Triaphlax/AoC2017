# ------Input----- #
answer1 = 0
answer2 = 0

inputString = input("Input path taken on the hexagonal grid: ")

directionList = inputString.split(',')

# ------Parts 1 & 2------ #
currentCoordinates = (0, 0)
maxNumberOfStepsFromCenter = 0


def getOptimalSteps(coordinates):
    absFirst = abs(coordinates[0])
    absSecond = abs(coordinates[1])
    if absFirst >= absSecond:
        return absSecond + int((absFirst - absSecond)/2)
    else:
        return absSecond


for direction in directionList:
    coordinatesToAdd = {
        'n': (2, 0),
        'ne': (1, 1),
        'se': (-1, 1),
        's': (-2, 0),
        'sw': (-1, -1),
        'nw': (1, -1)
    }[direction]
    currentCoordinates = tuple(map(sum, zip(currentCoordinates, coordinatesToAdd)))
    maxNumberOfStepsFromCenter = max(maxNumberOfStepsFromCenter, getOptimalSteps(currentCoordinates))

answer1 = getOptimalSteps(currentCoordinates)
answer2 = maxNumberOfStepsFromCenter

# ------Output----- #
print("Answer 1: " + str(answer1))
print("Answer 2: " + str(answer2))
