inputString = input("Input string for first CAPTCHA: ")

answer = 0

for i, c in enumerate(inputString):
    if c == inputString[(i+1) % len(inputString)]:
        answer += int(inputString[i])

print(answer)
