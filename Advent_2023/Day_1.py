import re

res = 0
digits = ['one','two','three','four','five','six','seven','eight','nine']
while True:
    uinput = input()

    if uinput == '':
        break

    digit = re.findall(r'\d',uinput)
    digit1,digit2 = digit[0], digit[-1]
    combined = digit1 + digit2
    res += int(combined)
print(res)