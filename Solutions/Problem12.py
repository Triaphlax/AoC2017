import re

# ------Input----- #
answer1 = 0
answer2 = 0

print("Input the adjacency list. Calculation will start on the first empty line.")
inputList = []

while True:
    inputString = input("")
    if inputString == "":
        break
    inputList.append(inputString)


def parseString(string):
    splitUp = re.split(' <-> |, ', string)
    neighborsList = []
    for n in splitUp[1:]:
        if n != '':
            neighborsList.append(int(n))

    return [int(splitUp[0]), neighborsList, False]


adjacencyList = list(map(parseString, inputList))
numberOfNodes = len(adjacencyList)
numberOfDiscoveredNodes = 0
numberOfGroups = 0


# ------Parts 1 & 2------ #
def DFS(vertex):
    adjacencyList[vertex][2] = True
    for neighbor in adjacencyList[vertex][1]:
        if not wasDiscovered(neighbor):
            DFS(neighbor)


def wasDiscovered(vertex):
    return adjacencyList[vertex][2]


while numberOfDiscoveredNodes < numberOfNodes:
    indexFirstUndiscovered = list(map(wasDiscovered, range(numberOfNodes))).index(0)
    DFS(indexFirstUndiscovered)
    numberOfDiscoveredNodes = sum(list(map(wasDiscovered, range(numberOfNodes))))
    numberOfGroups += 1
    if indexFirstUndiscovered == 0:
        answer1 = numberOfDiscoveredNodes

answer2 = numberOfGroups

# ------Output----- #
print("Answer 1: " + str(answer1))
print("Answer 2: " + str(answer2))
