# ------Input----- #
answer1 = 0
answer2 = 0

print("Input the jump instruction list. Calculation will start on the first empty line.")
inputList = []

while True:
    inputString = input("")
    if inputString == "":
        break
    inputList.append(inputString)

inputNumbers1 = list(map(int, inputList))
inputNumbers2 = list(map(int, inputList))

# ------Part 1------ #
jumpIndex = 0
while 0 <= jumpIndex <= len(inputNumbers1) - 1:
    instruction = inputNumbers1[jumpIndex]
    inputNumbers1[jumpIndex] += 1
    jumpIndex += instruction
    answer1 += 1

# ------Part 2------ #
jumpIndex = 0
while 0 <= jumpIndex <= len(inputNumbers2) - 1:
    instruction = inputNumbers2[jumpIndex]
    inputNumbers2[jumpIndex] += 1 if instruction < 3 else -1
    jumpIndex += instruction
    answer2 += 1

# ------Output----- #
print("Answer 1: " + str(answer1))
print("Answer 2: " + str(answer2))
