inputString = input("Input string for first CAPTCHA: ")

# ------Part 1------ #
answer1 = 0

for i, c in enumerate(inputString):
    if c == inputString[(i+1) % len(inputString)]:
        answer1 += int(inputString[i])

print("Answer 1: " + str(answer1))


# ------Part 2------ #
answer2 = 0

for i, c in enumerate(inputString):
    if c == inputString[(i+int(len(inputString)/2)) % len(inputString)]:
        answer2 += int(inputString[i])

print("Answer 2: " + str(answer2))
