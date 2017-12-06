# ------Input----- #
answer1 = 0
answer2 = 0

print("Input the spreadsheet. Calculation will start on the first empty line.")
inputList = []

while True:
    inputString = input("")
    if inputString == "":
        break
    inputList.append(inputString)

# ------Part 1------ #
for entry in inputList:
    cells = entry.split()
    numbers = list(map(int, cells))
    answer1 += max(numbers) - min(numbers)


# ------Part 2------ #
def dividing(divisor, dividend):
    if dividend != divisor and dividend % divisor == 0:
        return dividend / divisor
    else:
        return 0


for entry in inputList:
    cells = entry.split()
    numbers = list(map(int, cells))
    for n in numbers:
        dividedNumbers = list(map(lambda x: dividing(n, x), numbers))
        answer2 += int(sum(dividedNumbers))

# ------Output----- #
print("Answer 1: " + str(answer1))
print("Answer 2: " + str(answer2))
