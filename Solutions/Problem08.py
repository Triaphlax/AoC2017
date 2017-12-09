# ------Input----- #
answer1 = 0
answer2 = 0

print("Input the instruction list. Calculation will start on the first empty line.")
inputList = []

while True:
    inputString = input("")
    if inputString == "":
        break
    inputList.append(inputString)

instructions = list(map(lambda x: x.split(), inputList))
dictionary = dict()
highestValueEver = 0


# ------Parts 1 & 2------ #
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def findAndRetrieveRegisterValueIfDictionaryKey(name):
    if RepresentsInt(name):
        return int(name)
    elif name not in dictionary:
        dictionary[name] = 0
        return 0
    else:
        return dictionary[name]


while len(instructions) > 0:
    currentInstruction = instructions[0]

    # Find register
    registerName = currentInstruction[0]
    if registerName not in dictionary:
        dictionary[registerName] = 0

    # Check condition
    comparison = currentInstruction[5]
    value1 = findAndRetrieveRegisterValueIfDictionaryKey(currentInstruction[4])
    value2 = findAndRetrieveRegisterValueIfDictionaryKey(currentInstruction[6])
    conditionResult = {
        '>': lambda x, y: x > y,
        '<': lambda x, y: x < y,
        '>=': lambda x, y: x >= y,
        '<=': lambda x, y: x <= y,
        '==': lambda x, y: x == y,
        '!=': lambda x, y: x != y
    }[comparison](value1, value2)

    # Perform instruction
    if conditionResult:
        operation = currentInstruction[1]
        amount = int(currentInstruction[2])
        dictionary[registerName] = {
            'inc': lambda a, r: r + a,
            'dec': lambda a, r: r - a
        }[operation](amount, dictionary[registerName])
        if dictionary[registerName] > highestValueEver:
            highestValueEver = dictionary[registerName]

    del instructions[0]

answer1 = max(list(dictionary.values()))
answer2 = highestValueEver

# ------Output----- #
print("Answer 1: " + str(answer1))
print("Answer 2: " + str(answer2))
