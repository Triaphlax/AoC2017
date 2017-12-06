inputString = input("Input string for second CAPTCHA: ")

answer = 0

for i, c in enumerate(inputString):
    if c == inputString[(i+int(len(inputString)/2)) % len(inputString)]:
        answer += int(inputString[i])

print(answer)
