res = 0
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
while True:
    temp_digits = []
    uinput = input().strip()

    if uinput == "":
        break
    for i, n in enumerate(uinput):
        if n.isdigit():
            temp_digits.append(n)
        for eachdigit, eachvalue in enumerate(digits):
            if uinput[i:].startswith(eachvalue):
                temp_digits.append(str(eachdigit + 1))

    res += int(temp_digits[0] + temp_digits[-1])
print(res)
