def dividing(divisor, dividend):
    if dividend != divisor and dividend % divisor == 0:
        return dividend / divisor
    else:
        return 0


print("Input the second spreadsheet. Calculation will start on the first empty line.")
inputList = []

while True:
    inputString = input("")
    if inputString == "":
        break
    inputList.append(inputString)

answer = 0

for entry in inputList:
    cells = entry.split()
    numbers = list(map(int, cells))
    for n in numbers:
        dividedNumbers = list(map(lambda x: dividing(n, x), numbers))
        answer += int(sum(dividedNumbers))

print(answer)

