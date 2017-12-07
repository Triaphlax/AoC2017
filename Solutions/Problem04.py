# ------Input----- #
answer1 = 0
answer2 = 0

print("Input the passphrase list. Calculation will start on the first empty line.")
inputList = []

while True:
    inputString = input("")
    if inputString == "":
        break
    inputList.append(inputString)


# ------Part 1------ #
def checkduplicates(passphrase, comparefunction):
    passwords = passphrase.split()
    for i, pw1 in enumerate(passwords):
        for j, pw2 in enumerate(passwords[i+1:]):
            if comparefunction(pw1, pw2):
                return 0
    return 1


def simplecompare(a, b):
    return a == b


answer1 = sum(map(lambda x: checkduplicates(x, simplecompare), inputList))


# ------Part 2------ #
def anagramcompare(a, b):
    return sorted(a) == sorted(b)


answer2 = sum(map(lambda x: checkduplicates(x, anagramcompare), inputList))

# ------Output----- #
print("Answer 1: " + str(answer1))
print("Answer 2: " + str(answer2))
