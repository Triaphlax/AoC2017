# ------Input----- #
answer1 = 0
answer2 = 0

inputString = input("Initial memory state: ")
blocks = list(map(int, (inputString.strip().split())))

statesList = []


# ------Parts 1 and 2------ #
def performMemoryAlloc(memory):
    indexToRedistribute = memory.index(max(memory))
    memoryToReallocate = memory[indexToRedistribute]
    memory[indexToRedistribute] = 0
    currentIndex = indexToRedistribute
    while memoryToReallocate > 0:
        currentIndex = (currentIndex + 1) % len(memory)
        memory[currentIndex] += 1
        memoryToReallocate -= 1


seenThisBefore = False
while not seenThisBefore:
    answer1 += 1
    performMemoryAlloc(blocks)
    if blocks in statesList:
        seenThisBefore = True
        answer2 = answer1 - (statesList.index(blocks) + 1)
    else:
        statesList.append(list(blocks))

# ------Output----- #
print("Answer 1: " + str(answer1))
print("Answer 2: " + str(answer2))
