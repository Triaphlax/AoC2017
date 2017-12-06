# ------Input----- #
answer1 = 0
answer2 = 0

inputString = input("Input string for CAPTCHA: ")

# ------Part 1------ #
for i, c in enumerate(inputString):
    if c == inputString[(i+1) % len(inputString)]:
        answer1 += int(inputString[i])


# ------Part 2------ #
for i, c in enumerate(inputString):
    if c == inputString[(i+int(len(inputString)/2)) % len(inputString)]:
        answer2 += int(inputString[i])

# ------Output----- #
print("Answer 1: " + str(answer1))
print("Answer 2: " + str(answer2))
