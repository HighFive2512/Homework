uinput = input().split()
result = 0
for each_letter_set in uinput:
    firstletter, thenumber, secondletter = each_letter_set[0], int(each_letter_set[1:-1]), each_letter_set[-1]
    if firstletter.isupper():
        pos = (ord(firstletter) - ord('A') + 1)
        thenumber = thenumber / pos
    elif firstletter.islower():
        pos = (ord(firstletter) - ord('a') + 1)
        thenumber = thenumber * pos
    if secondletter.isupper():
        pos = (ord(secondletter) - ord('A') + 1)
        thenumber = thenumber - pos
    elif secondletter.islower():
        pos = (ord(secondletter) - ord('a') + 1)
        thenumber = thenumber + pos
    result += thenumber
print(*{"{:.2f}".format(result)})
