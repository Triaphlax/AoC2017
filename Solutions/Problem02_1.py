print("Input the first spreadsheet. Calculation will start on the first empty line.")
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
    answer += max(numbers) - min(numbers)

print(answer)
