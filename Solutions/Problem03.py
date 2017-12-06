# ------Input----- #
answer1 = 0
answer2 = 0

inputString = input("Input location to get data from: ")
inputValue = int(inputString)

# ------Part 1------ #
location = inputValue
numbersPerRow = 1
possibleDirections = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while pow(numbersPerRow, 2) < location:
    numbersPerRow += 2

currentCoordinates = map(int, ((numbersPerRow-1)/2, -(numbersPerRow-1)/2))
currentLocation = pow(numbersPerRow, 2)
stepsBeforeChangingDirection = numbersPerRow - 1
direction = 0

while currentLocation != location:
    currentLocation -= 1
    stepsBeforeChangingDirection -= 1
    currentCoordinates = tuple(map(sum, zip(currentCoordinates, possibleDirections[direction])))
    if stepsBeforeChangingDirection == 0:
        stepsBeforeChangingDirection = numbersPerRow - 1
        direction += 1

answer1 = int(sum(map(abs, currentCoordinates)))

# ------Part 2------ #
ringIndex = 0
innerRing = [1]
outerRing = []
outerIndex = 0
segmentIndex = 0
segmentNumber = 0
ghostIndex = 1
entriesPerSegment = 2
outerRingEntries = 4 * entriesPerSegment

relevantValues = []

while outerRingEntries != 0:

    # Get relevant inner values
    relevantOldSegment = []
    if ringIndex == 0:
        relevantOldSegment = innerRing
    else:
        oldEntriesPerSegment = max(entriesPerSegment - 2, 1)
        indexFrom = oldEntriesPerSegment * segmentNumber - 1
        if indexFrom < 0:
            indexFrom = 0
        indexTo = oldEntriesPerSegment * (segmentNumber + 1) - 1
        relevantOldSegment = innerRing[indexFrom:indexTo+1]

        if segmentNumber == 0:
            relevantOldSegment = [innerRing[len(innerRing) - 1]] + relevantOldSegment

    for v in [0, 1, 2]:
        if 0 <= ghostIndex - v <= len(relevantOldSegment) - 1:
            relevantValues.append(relevantOldSegment[ghostIndex - v])

    # Get relevant outer values
    if outerIndex - 1 >= 0:
        relevantValues.append(outerRing[outerIndex - 1])
        if segmentIndex == 0 and outerIndex - 2 >= 0:
            relevantValues.append(outerRing[outerIndex - 2])

    if segmentNumber == 3 and entriesPerSegment - 2 <= segmentIndex <= entriesPerSegment - 1:
        relevantValues.append(outerRing[0])

    # Find cell value
    valueToWrite = sum(relevantValues)
    outerRing.append(valueToWrite)
    if valueToWrite > inputValue:
        answer2 = valueToWrite
        break

    # Update variables
    relevantValues = []
    outerIndex += 1
    segmentIndex += 1
    ghostIndex += 1

    if outerIndex == outerRingEntries:
        ringIndex += 1
        innerRing = outerRing
        outerRing = []
        outerIndex = 0
        segmentIndex = 0
        segmentNumber = 0
        entriesPerSegment += 2
        outerRingEntries = 4 * entriesPerSegment
        ghostIndex = 1

    elif segmentIndex == entriesPerSegment:
        segmentIndex = 0
        segmentNumber += 1
        ghostIndex = 1

# ------Output----- #
print("Answer 1: " + str(answer1))
print("Answer 2: " + str(answer2))
